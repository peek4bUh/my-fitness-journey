import axios from 'axios'
import { computed, ref } from 'vue'

const user = ref(null)
const isAuthenticated = ref(false)
const isInitialCheckDone = ref(false)

const login = async (username, password) => {
  try {
    await axios.post('auth/login', { username, password })
    // After login, we need to fetch the user data
    return await checkAuth()
  } catch (error) {
    return {
      success: false,
      error: error.response?.data?.detail || error.response?.data?.Invalid || 'Login failed',
    }
  }
}

const checkAuth = async (force = false) => {
  // If we already checked and aren't forcing a refresh, skip the network call
  if (isInitialCheckDone.value && !force) return { success: isAuthenticated.value }

  try {
    const response = await axios.get('users')
    user.value = response.data
    isAuthenticated.value = true
    isInitialCheckDone.value = true
    return { success: true }
  } catch (error) {
    user.value = null
    isAuthenticated.value = false
    isInitialCheckDone.value = true
    return { success: false }
  }
}

const logout = async () => {
  try {
    await axios.post('auth/logout')
    return true
  } catch (error) {
    console.error('Logout error:', error)
    return false
  } finally {
    user.value = null
    isAuthenticated.value = false
    isInitialCheckDone.value = false
  }
}

export const useAuth = () => {
  return {
    isAuthenticated: computed(() => isAuthenticated.value),
    user: computed(() => user.value),
    isInitialCheckDone: computed(() => isInitialCheckDone.value),
    login,
    logout,
    checkAuth,
  }
}
