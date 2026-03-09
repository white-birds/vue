# AIHOM 智能审批系统 - 前端项目

<div align="center">
  <h1>🚀 AIHOM Approval System</h1>
  <p>现代化、高效的企业审批管理平台</p>
</div>

## ✨ 特性

- 🎨 **现代化 UI** - 基于 Ant Design Vue 4.x，美观易用
- 📱 **响应式设计** - 完美适配桌面端和移动端
- 🔥 **Vue 3 + TypeScript** - 使用最新的前端技术栈
- ⚡ **Vite 构建** - 极速的开发体验
- 📊 **BI 集成** - 集成 Apache Superset 数据可视化
- 🔐 **权限管理** - 完善的权限控制体系

## 📦 功能模块

- 🏠 **首页** - 系统概览和快速入口
- 📊 **数据分析** - 基于 Superset 的 BI 数据可视化
- 👤 **用户认证** - 登录/注册功能

## 🛠️ 技术栈

- **框架**: Vue 3.4+
- **构建工具**: Vite 5.0+
- **UI 组件**: Ant Design Vue 4.1+
- **路由**: Vue Router 4.2+
- **HTTP 客户端**: Axios 1.6+
- **语言**: TypeScript 5.3+
- **样式**: SCSS

## 📁 项目结构

```
approval-frontend/
├── public/                 # 静态资源
├── src/
│   ├── api/               # API 接口
│   ├── layout/            # 布局组件
│   ├── router/            # 路由配置
│   ├── styles/            # 全局样式
│   ├── utils/             # 工具函数
│   │   └── http.ts        # HTTP 请求封装
│   ├── views/             # 页面组件
│   │   ├── home/          # 首页
│   │   ├── bi/            # BI 数据分析
│   │   ├── Login.vue      # 登录页
│   │   └── Register.vue   # 注册页
│   ├── App.vue            # 根组件
│   └── main.ts            # 入口文件
├── index.html             # HTML 模板
├── package.json           # 依赖配置
├── tsconfig.json          # TypeScript 配置
└── vite.config.ts         # Vite 配置
```

## 🚀 快速开始

### 环境要求

- Node.js >= 16.0.0
- npm >= 8.0.0 或 pnpm >= 8.0.0

### 启动前检查

1. **确认后端服务运行中**  
   后端应该已经在 `http://localhost:8081/approval-boot/` 运行

2. **安装依赖（首次运行必须执行）**

```bash
cd approval-frontend
npm install
```

> ⚠️ **重要**：如果你还没运行 `npm install`，前端肯定启动不了！这是安装所有依赖包的关键步骤。

### 开发模式

```bash
npm run dev
```

访问 http://localhost:5173

### 生产构建

```bash
npm run build
```

构建产物在 `dist` 目录

### 预览构建

```bash
npm run preview
```

## 🔧 配置说明

### API 代理配置

在 `vite.config.ts` 中配置后端 API 代理：

```typescript
server: {
  port: 5173,
  proxy: {
    '/api': {
      target: 'http://localhost:8081/approval-boot',
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, ''),
    },
  },
}
```

### 环境变量

创建 `.env.development` 和 `.env.production` 文件：

```bash
# .env.development
VITE_API_BASE_URL=http://localhost:8081/approval-boot

# .env.production
VITE_API_BASE_URL=https://your-domain.com/approval-boot
```

## 🔌 API 接口

### 用户认证

```typescript
// 登录
POST /api/sys/login
{
  "username": "admin",
  "password": "admin"
}

// 注册
POST /api/sys/register
```

### Superset 集成

```typescript
// 获取仪表板列表
GET /api/superset/dashboards

// 获取 Guest Token
GET /api/superset/system-token?dashboardId=xxx
```

## 🐛 常见问题

### 问题1：菜单不显示 / 页面点不动
**原因**：没有安装依赖  
**解决**：运行 `npm install`

### 问题2：端口被占用
**错误信息**：`Port 5173 is already in use`  
**解决**：关闭占用5173端口的进程，或修改 `vite.config.ts` 中的端口号

### 问题3：连接后端失败
**错误信息**：`Network Error` 或 `404`  
**解决**：
1. 确认后端服务在 `http://localhost:8081/approval-boot/` 运行
2. 检查 `src/utils/http.ts` 中的 `baseURL` 配置

### 问题4：白屏 / 报错
**解决**：
1. 打开浏览器控制台（F12）查看具体错误
2. 确保 Node.js 版本 >= 16
3. 删除 `node_modules` 文件夹，重新运行 `npm install`

## 🚢 部署

### 方式 1：Nginx 部署

#### 1. 构建生产版本

```bash
npm run build
```

#### 2. 上传到服务器

```bash
# 使用 scp
scp -r dist/* user@server:/var/www/approval-frontend/

# 或使用 rsync
rsync -avz dist/ user@server:/var/www/approval-frontend/
```

#### 3. Nginx 配置

创建 `/etc/nginx/conf.d/approval.conf`：

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    root /var/www/approval-frontend;
    index index.html;
    
    # 开启 gzip 压缩
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
    gzip_min_length 1000;
    
    # 前端路由
    location / {
        try_files $uri $uri/ /index.html;
        add_header Cache-Control "no-cache";
    }
    
    # 静态资源缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # API 代理
    location /api/ {
        proxy_pass http://localhost:8081/approval-boot/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # 超时设置
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
```

#### 4. 重启 Nginx

```bash
nginx -t
systemctl restart nginx
```

### 方式 2：Docker 部署

#### 1. 创建 Dockerfile

```dockerfile
# 构建阶段
FROM node:18-alpine as builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 生产阶段
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### 2. 创建 nginx.conf

```nginx
server {
    listen 80;
    server_name localhost;
    
    root /usr/share/nginx/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    location /api/ {
        proxy_pass http://approval-backend:8081/approval-boot/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 3. 构建并运行

```bash
# 构建镜像
docker build -t approval-frontend .

# 运行容器
docker run -d -p 80:80 --name approval-frontend approval-frontend
```

### 方式 3：Docker Compose 部署

创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  frontend:
    build: .
    container_name: approval-frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - approval-network

  backend:
    image: approval-backend:latest
    container_name: approval-backend
    ports:
      - "8081:8081"
    networks:
      - approval-network

networks:
  approval-network:
    driver: bridge
```

启动服务：

```bash
docker-compose up -d
```

## 📝 开发规范

### 代码风格
- 使用 TypeScript 严格模式
- 遵循 Vue 3 Composition API 规范
- 使用 ESLint 进行代码检查

### 命名规范
- 组件名：PascalCase
- 文件名：kebab-case
- 变量名：camelCase
- 常量名：UPPER_SNAKE_CASE

### Git 提交规范
```
feat: 新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整
refactor: 重构
test: 测试相关
chore: 构建/工具链相关
```

---

<div align="center">
  <p>Made with ❤️ by AIHOM Team</p>
</div>
