# 前后端分离项目：用户管理系统

## 项目概述

这是一个基于Spring Boot和Vue 3的前后端分离项目，实现了基本的用户管理功能，包括用户的添加、查询、编辑和删除操作。

## 技术栈

### 后端
- Java 17
- Spring Boot 3.2.0
- Spring Data JPA
- H2数据库

### 前端
- Vue 3
- Vite
- Axios

## 项目结构

```
├── backend/                # Java后端项目
│   ├── src/
│   │   └── main/
│   │       ├── java/com/example/backend/
│   │       │   ├── BackendApplication.java   # 应用入口
│   │       │   ├── controller/               # 控制器层
│   │       │   ├── service/                  # 业务逻辑层
│   │       │   ├── repository/               # 数据访问层
│   │       │   └── entity/                   # 实体类
│   │       └── resources/
│   │           └── application.properties    # 配置文件
│   └── pom.xml                               # Maven配置
├── frontend/               # Vue前端项目
│   ├── src/
│   │   ├── App.vue          # 根组件
│   │   └── main.js          # 应用入口
│   ├── index.html           # HTML模板
│   ├── vite.config.js       # Vite配置
│   └── package.json         # 依赖配置
└── README.md                # 项目说明
```

## 运行步骤

### 1. 运行后端项目

#### 前提条件
- 已安装JDK 17或以上版本
- 已安装Maven 3.6或以上版本

#### 步骤

1. 进入后端项目目录：
   ```bash
   cd backend
   ```

2. 编译并运行项目：
   ```bash
   mvn spring-boot:run
   ```

3. 后端服务将在 http://localhost:8080 启动

4. 可以通过以下地址访问H2数据库控制台：
   - 地址：http://localhost:8080/h2-console
   - JDBC URL：jdbc:h2:mem:testdb
   - 用户名：sa
   - 密码：（空）

### 2. 运行前端项目

#### 前提条件
- 已安装Node.js 16或以上版本
- 已安装npm或yarn

#### 步骤

1. 进入前端项目目录：
   ```bash
   cd frontend
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

4. 前端应用将在 http://localhost:5173 启动

## 功能测试

### 1. 添加用户
1. 在前端页面的表单中填写用户信息（姓名、邮箱、密码）
2. 点击"添加"按钮
3. 成功后，用户列表将显示新添加的用户

### 2. 查看用户列表
1. 页面加载后，用户列表将自动显示所有用户
2. 添加、编辑或删除用户后，列表会自动刷新

### 3. 编辑用户
1. 点击用户列表中某个用户的"编辑"按钮
2. 表单将显示该用户的当前信息
3. 修改信息后点击"更新"按钮
4. 成功后，用户列表将显示更新后的信息

### 4. 删除用户
1. 点击用户列表中某个用户的"删除"按钮
2. 该用户将从列表中移除

## API接口

后端提供了以下RESTful API接口：

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | /api/users | 获取所有用户 |
| GET | /api/users/{id} | 根据ID获取用户 |
| POST | /api/users | 创建新用户 |
| PUT | /api/users/{id} | 更新用户信息 |
| DELETE | /api/users/{id} | 删除用户 |

## 跨域配置

后端已配置跨域支持，允许来自 http://localhost:3000 和 http://localhost:5173 的请求访问API接口。

## 注意事项

1. 确保后端服务先启动，再启动前端服务
2. 前端通过Vite代理将/api请求转发到后端服务
3. H2数据库是内存数据库，服务重启后数据会丢失
4. 生产环境中建议使用持久化数据库（如MySQL、PostgreSQL等）

## 开发建议

1. 后端可以添加更多的业务逻辑，如用户认证、权限管理等
2. 前端可以添加更多的UI组件和交互效果
3. 可以添加单元测试和集成测试
4. 可以使用Docker容器化部署项目

## 许可证

MIT