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

    <!-- 右侧注册区 -->
    <div class="aihom-right">
      <div class="aihom-form-container">
        <!-- Logo区域 -->
        <div class="aihom-form-logo">
          <img src="/logo.png" alt="logo" style="height:36px;width:auto;object-fit:contain;" />
          <span class="aihom-form-title">AIHOM 系统注册</span>
        </div>

        <h2 class="aihom-login-heading">创建账户</h2>
        <p class="aihom-login-sub">填写以下信息完成注册</p>

        <!-- 真实姓名 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            真实姓名
          </label>
          <input
              type="text"
              v-model="registerForm.realname"
              placeholder="请输入真实姓名"
              @keyup.enter="handleRegister"
          />
        </div>

        <!-- 用户名 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="3" width="20" height="14" rx="2"/>
              <path d="M8 21h8M12 17v4"/>
            </svg>
            用户名
          </label>
          <input
              type="text"
              v-model="registerForm.username"
              placeholder="请输入用户名（字母/数字）"
              @keyup.enter="handleRegister"
          />
        </div>

        <!-- 密码 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            密码
          </label>
          <div class="aihom-password-wrap">
            <input
                :type="showPassword ? 'text' : 'password'"
                v-model="registerForm.password"
                placeholder="请输入密码（至少6位）"
                @keyup.enter="handleRegister"
            />
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

        <!-- 确认密码 -->
        <div class="aihom-field">
          <label>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 12l2 2 4-4"/>
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            确认密码
          </label>
          <div class="aihom-password-wrap">
            <input
                :type="showConfirmPassword ? 'text' : 'password'"
                v-model="registerForm.confirmPassword"
                placeholder="请再次输入密码"
                @keyup.enter="handleRegister"
                :class="{ 'input-error': passwordMismatch }"
            />
            <button type="button" class="aihom-eye-btn" @click="showConfirmPassword = !showConfirmPassword">
              <svg v-if="!showConfirmPassword" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                <circle cx="12" cy="12" r="3"/>
              </svg>
              <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/>
                <line x1="1" y1="1" x2="23" y2="23"/>
              </svg>
            </button>
          </div>
          <!-- 密码不一致提示 -->
          <p v-if="passwordMismatch" class="aihom-error-tip">两次输入的密码不一致</p>
        </div>

        <!-- 注册按钮 -->
        <button class="aihom-submit-btn" @click="handleRegister" :disabled="loading">
          <span>{{ loading ? '注册中...' : '立即注册' }}</span>
          <svg v-if="!loading" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M5 12h14"/>
            <path d="m12 5 7 7-7 7"/>
          </svg>
        </button>

        <!-- 已有账号，去登录 -->
        <div class="aihom-register-row">
          已有账户？
          <a href="#" @click.prevent="router.push('/login')" class="aihom-register-link">立即登录</a>
        </div>

        <p class="aihom-footer">© 2025 AIHOM 智能审批系统 · 保留所有权利</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { http } from '@/utils/http'

const router = useRouter()
const showPassword = ref(false)
const showConfirmPassword = ref(false)
const loading = ref(false)

const registerForm = reactive({
  realname: '',
  username: '',
  password: '',
  confirmPassword: ''
})

// 密码不一致实时校验
const passwordMismatch = computed(() => {
  return registerForm.confirmPassword.length > 0 &&
      registerForm.password !== registerForm.confirmPassword
})

const handleRegister = async () => {
  if (!registerForm.realname || !registerForm.username || !registerForm.password || !registerForm.confirmPassword) {
    message.warning('请填写所有必填项')
    return
  }
  if (registerForm.password.length < 6) {
    message.warning('密码长度不能少于6位')
    return
  }
  if (registerForm.password !== registerForm.confirmPassword) {
    message.warning('两次输入的密码不一致')
    return
  }

  loading.value = true
  try {
    const res: any = await http.post('/sys/register', {
      username: registerForm.username,
      password: registerForm.password,
      realname: registerForm.realname
    })

    console.log('注册返回数据:', res)

    const token = res?.token || res?.result?.token
    const userInfo = res?.userInfo || res?.result?.userInfo

    if (token) {
      localStorage.setItem('systemToken', token)
      if (userInfo) {
        localStorage.setItem('userInfo', JSON.stringify(userInfo))
      }
      message.success('注册成功，正在跳转...')
      router.push('/dashboard')
    } else {
      message.error(res?.message || '注册失败，请稍后重试')
    }
  } catch (error) {
    console.error('注册请求错误:', error)
    message.error('接口请求失败，请检查后端是否启动')
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

/* ===== 左侧 ===== */
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

/* ===== 右侧 ===== */
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

/* ===== 表单字段 ===== */
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

.aihom-field input.input-error {
  border-color: #e53e3e;
  box-shadow: 0 0 0 3px rgba(229, 62, 62, 0.1);
}

.aihom-error-tip {
  font-size: 12px;
  color: #e53e3e;
  margin-top: 6px;
  margin-left: 2px;
}

/* ===== 密码显示切换 ===== */
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

/* ===== 按钮 ===== */
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
  margin-top: 8px;
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

/* ===== 已有账户跳转 ===== */
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

/* ===== 底部版权 ===== */
.aihom-footer {
  text-align: center;
  font-size: 12px;
  color: #cbd5e0;
  margin-top: 32px;
}

/* ===== 动画 ===== */
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

/* ===== 移动端适配 ===== */
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