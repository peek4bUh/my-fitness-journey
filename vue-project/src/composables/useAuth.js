import { ref, computed } from 'vue'
import axios from 'axios'

const isAuthenticated = ref(false)
const user = ref(null)
const isLoading = ref(false)

// Check authentication status by making a request to a protected endpoint
const checkAuth = async () => {
  try {
    isLoading.value = true
    const response = await axios.get('users')
    user.value = response.data
    isAuthenticated.value = true
    return true
  } catch (error) {
    user.value = null
    isAuthenticated.value = false
    return false
  } finally {
    isLoading.value = false
  }
}

const login = async (username, password) => {
  try {
    isLoading.value = true
    const response = await axios.post('users/login', {
      username,
      password,
    })

    // Login successful - cookies are set, router guard will verify authentication
    // Don't call checkAuth() here to avoid duplicate requests
    return { success: true }
  } catch (error) {
    return {
      success: false,
      error: error.response?.data?.Invalid || 'Login failed',
    }
  } finally {
    isLoading.value = false
  }
}

const logout = async () => {
  try {
    await axios.post('users/logout')
  } catch (error) {
    console.error('Logout error:', error)
  } finally {
    // Clear local state regardless of API response
    isAuthenticated.value = false
    user.value = null
    // Redirect to login
    window.location.href = '/login'
  }
}

// Set up axios interceptor to handle 401 responses
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid, clear auth state
      isAuthenticated.value = false
      user.value = null
      // Redirect to login if not already there
      if (window.location.pathname !== '/login') {
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  },
)

export const useAuth = () => {
  return {
    isAuthenticated: computed(() => isAuthenticated.value),
    user: computed(() => user.value),
    isLoading: computed(() => isLoading.value),
    login,
    logout,
    checkAuth,
  }
}
