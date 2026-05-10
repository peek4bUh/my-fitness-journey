import apiClient from './index.js'

export class UserService {
  constructor() {}

  async getUserInfo() {
    try {
      const response = await apiClient.get('users/me')
      return response.data
    } catch (err) {
      throw new Error(`Failed to load user info: ${err.response?.data?.message || err.message}`)
    }
  }
}
