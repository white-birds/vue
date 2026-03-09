import axios from 'axios'
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import { message } from 'ant-design-vue'

class HttpRequest {
  private instance: AxiosInstance

  constructor() {
    this.instance = axios.create({
      baseURL: '/api',
      timeout: 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    this.setupInterceptors()
  }

  private setupInterceptors() {
    // 请求拦截器
    this.instance.interceptors.request.use(
      (config) => {
        // 可以在这里添加 token
        const token = localStorage.getItem('token')
        if (token) {
          config.headers.Authorization = `Bearer ${token}`
        }
        return config
      },
      (error) => {
        return Promise.reject(error)
      }
    )

    // 响应拦截器
    this.instance.interceptors.response.use(
      (response: AxiosResponse) => {
        const { data } = response
        
        console.log('🔥 API Response:', response.config.url, data)
        
        // 根据后端返回的数据结构调整
        if (data.success === false) {
          // 业务错误，只在这里显示一次错误提示
          message.error(data.message || '请求失败')
          return Promise.reject(data)
        }
        
        // JeecgBoot 返回结构：{ success: true, result: {...}, message: '' }
        return data.result !== undefined ? data.result : data
      },
      (error) => {
        // 网络错误或 HTTP 状态码错误
        if (error.response) {
          const { status } = error.response
          
          // 只在真正的 HTTP 错误时显示提示（不是业务错误）
          switch (status) {
            case 401:
              message.error('未授权，请重新登录')
              break
            case 403:
              message.error('拒绝访问')
              break
            case 404:
              message.error('接口请求404或网络异常，请检查后端是否启动')
              break
            case 500:
              message.error('服务器错误')
              break
            default:
              // 其他 HTTP 错误不显示提示，让业务代码处理
              break
          }
        } else if (error.request) {
          // 请求已发出但没有收到响应
          message.error('网络错误，请检查网络连接')
        }
        // 如果是业务错误（success: false），不在这里显示，已经在上面显示过了
        
        return Promise.reject(error)
      }
    )
  }

  public get<T = any>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return this.instance.get(url, config)
  }

  public post<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return this.instance.post(url, data, config)
  }

  public put<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<T> {
    return this.instance.put(url, data, config)
  }

  public delete<T = any>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return this.instance.delete(url, config)
  }
}

export const http = new HttpRequest()

