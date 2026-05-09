import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
  withCredentials: true,
})

// Interceptor de respuesta: si recibimos 401, intentamos refrescar
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      try {
        await apiClient.post('/auth/refresh/') // Refresca la cookie httpOnly del access token
        return apiClient(originalRequest) // Reintenta la petición original
      } catch (refreshError) {
        // El refresh también falló → redirigir al login
        localStorage.removeItem('user')
        window.location.href = '/login'
        return Promise.reject(refreshError)
      }
    }
    return Promise.reject(error)
  },
)

export default apiClient
