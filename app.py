from flask import Flask, render_template, request
import subprocess
import threading
import time
import queue

app = Flask(__name__)

# 用于存储脚本输出的队列
output_queues = {}

@app.route('/')
def index():
    """渲染主页面"""
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    """处理表单提交，启动脚本执行"""
    path = request.form.get('path', '')
    if not path:
        return "请输入路径", 400
    
    # 生成唯一的会话ID
    session_id = str(time.time())
    # 创建输出队列
    output_queues[session_id] = queue.Queue()
    
    # 启动线程执行脚本
    threading.Thread(target=execute_script, args=(path, session_id)).start()
    
    return session_id

@app.route('/stream/<session_id>')
def stream(session_id):
    """提供Server-Sent Events流，实时返回脚本输出"""
    def generate():
        queue = output_queues.get(session_id)
        if not queue:
            yield f"data: 无效的会话ID\n\n"
            return
        
        # 发送初始消息
        yield f"data: 开始执行脚本，路径: {request.args.get('path', '')}\n\n"
        
        while True:
            try:
                # 从队列获取输出，超时1秒
                line = queue.get(timeout=1)
                if line is None:  # 脚本执行结束
                    yield f"data: 脚本执行完成\n\n"
                    break
                # 发送输出行
                yield f"data: {line}\n\n"
            except queue.Empty:
                continue
            except Exception as e:
                yield f"data: 错误: {str(e)}\n\n"
                break
        
        # 清理队列
        if session_id in output_queues:
            del output_queues[session_id]
    
    return app.response_class(generate(), mimetype='text/event-stream')

def execute_script(path, session_id):
    """执行check1.py脚本并将输出放入队列"""
    queue = output_queues.get(session_id)
    if not queue:
        return
    
    try:
        # 执行脚本，捕获输出
        process = subprocess.Popen(
            ['python', 'check1.py', path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        # 读取实时输出
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            if line:
                queue.put(line.strip())
        
        # 等待进程结束
        process.wait()
        
        # 发送退出码
        queue.put(f"退出码: {process.returncode}")
    except Exception as e:
        queue.put(f"执行错误: {str(e)}")
    finally:
        # 发送结束信号
        queue.put(None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)