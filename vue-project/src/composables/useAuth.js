import { AuthService } from '@/services/authService'
import { UserService } from '@/services/userService'
import { computed, ref } from 'vue'

const authService = new AuthService()
const userService = new UserService()
const user = ref(JSON.parse(localStorage.getItem('user')) || null)
const isAuthenticated = ref(false)

const login = async (username, password) => {
  try {
    await authService.signIn(username, password)
    user.value = await userService.getUserInfo()
    isAuthenticated.value = true
    return { success: true }
  } catch (error) {
    return {
      success: false,
      error: error.response?.data?.detail || 'Login error',
    }
  }
}

const logout = async () => {
  try {
    await authService.signOut()
    return true
  } catch (error) {
    console.error('Logout error:', error)
    return false
  } finally {
    user.value = null
    isAuthenticated.value = false
  }
}

const checkAuth = async () => {
  if (!user.value) {
    try {
      user.value = await userService.getUserInfo()
      isAuthenticated.value = true
    } catch {
      user.value = null
      localStorage.removeItem('user')
      isAuthenticated.value = false
    }
  }
}

export const useAuth = () => {
  return {
    isAuthenticated: computed(() => !!user.value),
    login,
    logout,
    checkAuth,
  }
}
