#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os

def main():
    """主函数，处理路径检查逻辑"""
    if len(sys.argv) != 2:
        print("Usage: python check1.py <path>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    # 模拟脚本执行过程
    print(f"正在检查路径: {path}")
    time.sleep(1)
    
    # 检查路径是否存在
    if os.path.exists(path):
        print(f"路径存在: {path}")
        time.sleep(0.5)
        
        # 检查是文件还是目录
        if os.path.isfile(path):
            print(f"这是一个文件")
            time.sleep(0.5)
            # 获取文件大小
            size = os.path.getsize(path)
            print(f"文件大小: {size} 字节")
            time.sleep(0.5)
            # 获取文件修改时间
            mtime = os.path.getmtime(path)
            print(f"最后修改时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))}")
        elif os.path.isdir(path):
            print(f"这是一个目录")
            time.sleep(0.5)
            # 获取目录中的文件数量
            try:
                files = os.listdir(path)
                print(f"目录包含 {len(files)} 个条目")
                time.sleep(0.5)
                # 显示前5个文件
                if files:
                    print("前5个条目:")
                    for i, file in enumerate(files[:5]):
                        full_path = os.path.join(path, file)
                        if os.path.isdir(full_path):
                            print(f"  {i+1}. {file}/")
                        else:
                            print(f"  {i+1}. {file}")
                        time.sleep(0.2)
                    if len(files) > 5:
                        print(f"  ... 还有 {len(files) - 5} 个条目")
            except PermissionError:
                print("没有权限访问此目录")
    else:
        print(f"路径不存在: {path}")
    
    time.sleep(1)
    print("检查完成")

if __name__ == "__main__":
    main()