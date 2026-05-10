import apiClient from './index.js'

export class AuthService {
  constructor() {}

  async signIn(username, password) {
    try {
      await apiClient.post('auth/login', { username, password })
    } catch (err) {
      throw new Error(`Failed to sign in: ${err.response?.data?.message || err.message}`)
    }
  }

  async signOut() {
    try {
      await apiClient.post('auth/logout')
    } catch (err) {
      throw new Error(`Failed to sign out: ${err.response?.data?.message || err.message}`)
    }
  }
}
