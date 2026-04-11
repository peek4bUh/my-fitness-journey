<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

import AppLayout from '../../layout/AppLayout.vue'

const exercises = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get('exercises')
    exercises.value = response.data
    console.log(response.data)
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load exercises'
    console.error(error.value)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <AppLayout>
    <div class="bg-inherit p-4 md:p-6 lg:p-8">
      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center py-12">
        <div
          class="h-8 w-8 animate-spin rounded-full border-4 border-gray-200 border-t-gray-900"
        ></div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="rounded-lg border border-red-200 bg-red-50 p-4 text-red-600">
        {{ error }}
      </div>

      <!-- Exercises Grid -->
      <div v-else class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <RouterLink
          v-for="exercise in exercises"
          :key="exercise.id"
          :to="`/dashboard/exercises/${exercise.id}`"
          class="group block"
        >
          <div
            class="h-full overflow-hidden rounded-xl border border-gray-200 bg-white transition-all duration-200 hover:border-gray-300 hover:shadow-lg"
          >
            <div class="p-5">
              <div class="flex items-start gap-4">
                <!-- Exercise Info -->
                <div class="min-w-0 flex-1">
                  <h4
                    class="font-semibold text-gray-900 transition-colors group-hover:text-gray-600"
                  >
                    {{ exercise.name }}
                  </h4>

                  <p class="mt-1 line-clamp-2 text-sm text-gray-500">
                    {{ exercise.description || 'No description available' }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </RouterLink>
      </div>

      <!-- Empty State -->
      <div
        v-if="!loading && !error && exercises.length === 0"
        class="flex flex-col items-center justify-center rounded-xl border border-dashed border-gray-300 bg-gray-50 py-12"
      >
        <div class="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-gray-200">
          <svg class="h-6 w-6 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
            />
          </svg>
        </div>
        <p class="text-gray-500">No exercises found</p>
      </div>
    </div>
  </AppLayout>
</template>
