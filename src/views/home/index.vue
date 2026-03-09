<template>
  <div class="home-container">
    <div class="background-decoration">
      <div class="circle circle-1"></div>
      <div class="circle circle-2"></div>
      <div class="circle circle-3"></div>
    </div>
    
    <div class="content-wrapper">
      <div class="logo-section">
        <div class="logo-container">
          <img src="/logo.png" alt="AIHOM Cloud" class="logo-image" />
        </div>
      </div>
      
      <div class="text-section">
        <h1 class="main-title">
          <span class="gradient-text">AIHOM BI</span>
          数据分析系统
        </h1>
        <p class="subtitle">智能化数据分析平台 · 让数据驱动决策</p>
        
        <div class="features">
          <div class="feature-item">
            <div class="feature-icon">📊</div>
            <div class="feature-text">实时数据分析</div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🎯</div>
            <div class="feature-text">智能可视化</div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">🚀</div>
            <div class="feature-text">高效决策支持</div>
          </div>
        </div>
        
        <div class="action-buttons">
          <a-button type="primary" size="large" @click="goToAnalysis">
            开始分析
            <template #icon><LineChartOutlined /></template>
          </a-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { LineChartOutlined } from '@ant-design/icons-vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const goToAnalysis = () => {
  router.push('/bi-superset')
}
</script>

<style scoped>
.home-container {
  position: relative;
  min-height: calc(100vh - 64px);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.background-decoration {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  animation: float 20s infinite ease-in-out;
}

.circle-1 {
  width: 300px;
  height: 300px;
  top: -100px;
  left: -100px;
  animation-delay: 0s;
}

.circle-2 {
  width: 200px;
  height: 200px;
  bottom: -50px;
  right: 10%;
  animation-delay: 5s;
}

.circle-3 {
  width: 150px;
  height: 150px;
  top: 50%;
  right: -50px;
  animation-delay: 10s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-30px) rotate(180deg);
  }
}

.content-wrapper {
  position: relative;
  z-index: 1;
  max-width: 1200px;
  width: 100%;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  padding: 60px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.logo-section {
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo-container {
  position: relative;
  padding: 30px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.logo-container:hover {
  transform: translateY(-10px);
}

.logo-image {
  max-width: 100%;
  height: auto;
  display: block;
  border-radius: 12px;
}

.text-section {
  text-align: left;
}

.main-title {
  font-size: 42px;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 20px;
  line-height: 1.3;
}

.gradient-text {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  display: inline-block;
  margin-right: 10px;
}

.subtitle {
  font-size: 18px;
  color: #7f8c8d;
  margin-bottom: 40px;
  line-height: 1.6;
}

.features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}

.feature-item {
  text-align: center;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.feature-item:hover {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
}

.feature-item:hover .feature-icon,
.feature-item:hover .feature-text {
  color: white;
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 10px;
  transition: transform 0.3s ease;
}

.feature-item:hover .feature-icon {
  transform: scale(1.2);
}

.feature-text {
  font-size: 14px;
  color: #2c3e50;
  font-weight: 500;
  transition: color 0.3s ease;
}

.action-buttons {
  display: flex;
  gap: 15px;
}

.action-buttons :deep(.ant-btn-primary) {
  height: 48px;
  padding: 0 40px;
  font-size: 16px;
  border-radius: 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
  transition: all 0.3s ease;
}

.action-buttons :deep(.ant-btn-primary:hover) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

@media (max-width: 968px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 40px;
    padding: 40px 30px;
  }
  
  .text-section {
    text-align: center;
  }
  
  .main-title {
    font-size: 32px;
  }
  
  .features {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    justify-content: center;
  }
}
</style>
