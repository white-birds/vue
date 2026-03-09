<template>
  <div class="aihom-wrapper">
    <!-- 左侧介绍区 -->
    <div class="aihom-left">
      <div class="aihom-left-inner">
        <div class="aihom-brand">
          <div class="aihom-logo-large">
            <img src="/logo.png" alt="logo" style="height:64px;width:auto;object-fit:contain;filter:brightness(0) invert(1);" />
          </div>

          <p class="aihom-brand-sub">智能数据分析平台</p>
        </div>
        <div class="aihom-features">
          <div class="aihom-feature-item">
            <span class="feature-dot"></span>
            <span>安全可靠的身份认证</span>
          </div>
          <div class="aihom-feature-item">
            <span class="feature-dot"></span>
            <span>统一单点登录管理</span>
          </div>
          <div class="aihom-feature-item">
            <span class="feature-dot"></span>
            <span>企业级权限控制</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 右侧登录区 -->
    <div class="aihom-right">
      <div class="aihom-form-container">
        <!-- Logo区域 -->
        <div class="aihom-form-logo">
          <img src="/logo.png" alt="logo" style="height:36px;width:auto;object-fit:contain;" />
          <span class="aihom-form-title">AIHOM 系统登录</span>
        </div>

        <h2 class="aihom-login-heading">欢迎回来</h2>
        <p class="aihom-login-sub">请登录您的账户以继续</p>

        <!-- 账号输入框 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            用户名
          </label>
          <input type="text" v-model="loginForm.username" placeholder="请输入用户名" @keyup.enter="handleLogin"/>
        </div>

        <!-- 密码输入框 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            密码
          </label>
          <div class="aihom-password-wrap">
            <input :type="showPassword ? 'text' : 'password'" v-model="loginForm.password" placeholder="请输入密码"
                   @keyup.enter="handleLogin"/>
            <button type="button" class="aihom-eye-btn" @click="showPassword = !showPassword">
              <svg v-if="!showPassword" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/>
                <line x1="1" y1="1" x2="23" y2="23"/>
              </svg>
            </button>
          </div>
        </div>

        <div class="aihom-options">
          <label class="aihom-checkbox">
            <input type="checkbox"> 记住我
          </label>
          <a href="#" class="aihom-forgot">忘记密码？</a>
        </div>

        <!-- 登录按钮 -->
        <button class="aihom-submit-btn" @click="handleLogin" :disabled="loading">
          <span>{{ loading ? '登录中...' : '登 录' }}</span>
          <svg v-if="!loading" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M5 12h14"/>
            <path d="m12 5 7 7-7 7"/>
          </svg>
        </button>

        <!-- 去注册 -->
        <div class="aihom-register-row">
          没有账户？
          <a href="#" @click.prevent="router.push('/register')" class="aihom-register-link">立即注册</a>
        </div>

        <p class="aihom-footer">© 2025 AIHOM 智能审批系统 · 保留所有权利</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref, reactive} from 'vue'
import {useRouter} from 'vue-router'
import {message} from 'ant-design-vue'
import {http} from '@/utils/http'

const router = useRouter()
const showPassword = ref(false)
const loading = ref(false)

const loginForm = reactive({
  username: '',
  password: ''
})

const handleLogin = async () => {
  if (!loginForm.username || !loginForm.password) {
    message.warning('请输入用户名和密码')
    return
  }

  loading.value = true
  try {
    const res: any = await http.post('/sys/login', loginForm)

    console.log("后端返回完整数据:", res)

    const token = res?.token || res?.result?.token;
    const userInfo = res?.userInfo || res?.result?.userInfo;

    if (token) {
      localStorage.setItem('systemToken', token)
      if (userInfo) {
        localStorage.setItem('userInfo', JSON.stringify(userInfo))
      }
      console.log("✅ 登录成功，Token 已保存")
      message.success('登录成功')
      router.push('/dashboard')
    } else {
      console.error("❌ 未找到 Token, res结构:", res)
      message.error(res?.message || '登录失败，账号或密码错误')
    }
  } catch (error: any) {
    // 如果是业务错误（success: false），http.ts 已经显示过错误了，这里不再显示
    // 只处理真正的网络错误
    if (!error.message && !error.success) {
      console.error('网络请求错误:', error)
      // 网络错误已经在 http.ts 中处理了，这里不再重复显示
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.aihom-wrapper {
  display: flex;
  min-height: 100vh;
  width: 100vw;
  background: #f5f7fa;
  color: #1a202c;
  font-family: 'Noto Sans SC', sans-serif;
}

.aihom-left {
  flex: 1;
  background: linear-gradient(145deg, #1a56db 0%, #1e40af 50%, #1e3a8a 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px;
  position: relative;
  overflow: hidden;
}

.aihom-left::before {
  content: '';
  position: absolute;
  top: -100px;
  right: -100px;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
}

.aihom-left::after {
  content: '';
  position: absolute;
  bottom: -80px;
  left: -80px;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
}

.aihom-left-inner {
  position: relative;
  z-index: 1;
  color: white;
  max-width: 420px;
}

.aihom-brand {
  margin-bottom: 60px;
}

.aihom-logo-large {
  margin-bottom: 20px;
  animation: fadeInDown 0.8s ease;
}

.aihom-brand-name {
  font-size: 42px;
  font-weight: 700;
  letter-spacing: 4px;
  margin-bottom: 8px;
  animation: fadeInDown 0.9s ease;
}

.aihom-brand-sub {
  font-size: 16px;
  font-weight: 300;
  opacity: 0.8;
  letter-spacing: 2px;
  animation: fadeInDown 1s ease;
}

.aihom-features {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.aihom-feature-item {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 15px;
  font-weight: 300;
  opacity: 0.9;
  animation: fadeInLeft 1.1s ease;
}

.feature-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.7);
  border: 2px solid rgba(255, 255, 255, 0.4);
  flex-shrink: 0;
}

.aihom-right {
  width: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  padding: 60px 48px;
}

.aihom-form-container {
  width: 100%;
  max-width: 360px;
  animation: fadeInRight 0.8s ease;
}

.aihom-form-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 36px;
}

.aihom-form-title {
  font-size: 17px;
  font-weight: 600;
  color: #1a202c;
  letter-spacing: 0.5px;
}

.aihom-login-heading {
  font-size: 26px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 8px;
}

.aihom-login-sub {
  font-size: 14px;
  color: #718096;
  margin-bottom: 32px;
}

.aihom-field {
  margin-bottom: 20px;
}

.aihom-field label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: #4a5568;
  margin-bottom: 8px;
}

.aihom-field label svg {
  color: #a0aec0;
}

.aihom-field input {
  width: 100%;
  height: 46px;
  padding: 0 16px;
  border: 1.5px solid #e2e8f0;
  border-radius: 10px;
  font-size: 14px;
  font-family: inherit;
  color: #1a202c;
  background: #fafafa;
  transition: all 0.2s ease;
  outline: none;
  box-sizing: border-box;
}

.aihom-field input:focus {
  border-color: #1a56db;
  background: #fff;
  box-shadow: 0 0 0 3px rgba(26, 86, 219, 0.1);
}

.aihom-field input::placeholder {
  color: #cbd5e0;
}

.aihom-password-wrap {
  position: relative;
}

.aihom-password-wrap input {
  padding-right: 46px;
}

.aihom-eye-btn {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  color: #a0aec0;
  padding: 4px;
  display: flex;
  align-items: center;
  transition: color 0.2s;
}

.aihom-eye-btn:hover {
  color: #4a5568;
}

.aihom-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.aihom-checkbox {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #4a5568;
  cursor: pointer;
  user-select: none;
}

.aihom-checkbox input[type="checkbox"] {
  width: 16px;
  height: 16px;
  accent-color: #1a56db;
  cursor: pointer;
}

.aihom-forgot {
  font-size: 13px;
  color: #1a56db;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.aihom-forgot:hover {
  color: #1e40af;
  text-decoration: underline;
}

.aihom-submit-btn {
  width: 100%;
  height: 48px;
  background: linear-gradient(135deg, #1a56db 0%, #1e40af 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  font-family: inherit;
  letter-spacing: 2px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: all 0.2s ease;
  box-shadow: 0 4px 15px rgba(26, 86, 219, 0.35);
}

.aihom-submit-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(26, 86, 219, 0.45);
  background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
}

.aihom-submit-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(26, 86, 219, 0.3);
}

.aihom-submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.aihom-register-row {
  text-align: center;
  margin-top: 20px;
  font-size: 13px;
  color: #718096;
}

.aihom-register-link {
  color: #1a56db;
  font-weight: 600;
  text-decoration: none;
  margin-left: 4px;
  transition: color 0.2s;
}

.aihom-register-link:hover {
  color: #1e40af;
  text-decoration: underline;
}

.aihom-footer {
  text-align: center;
  font-size: 12px;
  color: #cbd5e0;
  margin-top: 40px;
}

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInLeft {
  from { opacity: 0; transform: translateX(-20px); }
  to   { opacity: 1; transform: translateX(0); }
}

@keyframes fadeInRight {
  from { opacity: 0; transform: translateX(20px); }
  to   { opacity: 1; transform: translateX(0); }
}

@media (max-width: 768px) {
  .aihom-left {
    display: none;
  }
  .aihom-right {
    width: 100%;
    padding: 40px 24px;
  }
}
</style>