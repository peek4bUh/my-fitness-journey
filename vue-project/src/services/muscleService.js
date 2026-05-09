import { Endpoints } from '@/constants/endpoints'
import apiClient from '../api.js'

export class MuscleService {
  constructor() {}

  async getMuscleGroups() {
    try {
      const response = await apiClient.get(Endpoints.MUSCLE_GROUPS)
      console.log('Muscle groups response:', response.data)
      return response.data
    } catch (err) {
      throw new Error(`Failed to load muscle groups: ${err.response?.data?.message || err.message}`)
    }
  }
}
