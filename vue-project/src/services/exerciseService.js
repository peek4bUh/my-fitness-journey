import { Endpoints } from '@/constants/endpoints'
import apiClient from '../api.js'

export class ExerciseService {
  constructor() {}

  async getExercises() {
    try {
      const response = await apiClient.get(Endpoints.EXERCISES)
      return response.data
    } catch (err) {
      throw new Error(`Failed to load exercises: ${err.response?.data?.message || err.message}`)
    }
  }

  async getExerciseLevels() {
    try {
      const response = await apiClient.get(Endpoints.EXERCISE_LEVELS)
      return response.data
    } catch (err) {
      throw new Error(
        `Failed to load exercise levels: ${err.response?.data?.message || err.message}`,
      )
    }
  }
}
