import { Endpoints } from '@/constants/endpoints'
import apiClient from '../api.js'

export class ProgramService {
  constructor() {}

  async getPrograms() {
    try {
      const response = await apiClient.get(Endpoints.PROGRAM_LIST)
      return response.data
    } catch (err) {
      throw new Error(`Failed to load programs: ${err.response?.data?.message || err.message}`)
    }
  }
}
