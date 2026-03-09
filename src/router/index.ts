import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import Layout from '@/layout/index.vue'

// 假设你刚才写的登录页放在 views/Login.vue
// 如果路径不对，请修改这里
import Login from '@/views/Login.vue'

const routes: RouteRecordRaw[] = [
  // ✅ 新增：恢复登录页路由
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { title: '登录', requiresAuth: false }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/Register.vue'),
    meta: { title: '注册', requiresAuth: false }
  },
  {
    path: '/',
    component: Layout,
    redirect: '/home',
    children: [
      // 首页
      {
        path: 'home',
        name: 'Home',
        component: () => import('@/views/home/index.vue'),
        meta: { title: '首页', icon: 'HomeOutlined' },
      },
      // 数据分析
      {
        path: 'bi-superset',
        name: 'BISuperset',
        component: () => import('@/views/bi/superset.vue'),
        meta: { title: '数据分析', icon: 'LineChartOutlined' },
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// ✅ 重写：基于 systemToken 的原生路由守卫
router.beforeEach((to, from, next) => {
  // 1. 获取我们自己存的 token (注意 key 要和 Login.vue 里一致)
  const token = localStorage.getItem('systemToken')

  // 2. 如果去的是登录页
  if (to.path === '/login'|| to.path === '/register') {
    if (token) {
      // 已经登录了，就踢回首页
      return next('/')
    }
    // 没登录，允许访问登录页
    return next()
  }

  // 3. 如果去的是其他页面（需要认证）
  if (!token) {
    // 没 Token，强制跳转到我们自己的登录页
    return next('/login')
  }

  // 4. 有 Token，放行
  next()
})

export default router