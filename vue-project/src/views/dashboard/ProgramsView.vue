<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import AdminLayout from '@/components/layout/DashboardLayout.vue'

import Button from 'primevue/button'

const programs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/programs/')
    programs.value = response.data
    console.log(response.data)
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load programs'
    console.error(error.value)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <AdminLayout>
    <div class="bg-gray-50 p-4 md:p-6 lg:p-8">
      <div v-if="loading" class="text-center text-gray-500">Loading...</div>
      <div v-else-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-600">
        {{ error }}
      </div>

      <!-- Programs Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <div
          v-for="program in programs"
          :key="program.id"
          class="group bg-white rounded-xl border border-gray-200 overflow-hidden hover:shadow-lg hover:border-gray-300 transition-all duration-200"
        >
          <!-- Card Header -->
          <div class="p-5 pb-3">
            <div class="flex items-start justify-between gap-3 mb-2">
              <RouterLink
                :to="`/dashboard/programs/${program.id}`"
                class="text-lg font-semibold text-gray-900 hover:text-blue-600 transition-colors line-clamp-2"
              >
                {{ program.title }}
              </RouterLink>
              <span class="shrink-0 px-2.5 py-1 text-xs font-medium bg-blue-50 text-blue-700 rounded-full">
                {{ program.duration_weeks }} Weeks
              </span>
            </div>
            <p class="text-sm text-gray-600 line-clamp-2 leading-relaxed">
              {{ program.description }}
            </p>
          </div>

          <!-- Card Footer -->
          <div class="px-5 py-3 bg-gray-50 border-t border-gray-100 flex items-center justify-between">
            <div class="flex items-center gap-4 text-xs text-gray-500">
              <span v-if="program.days_per_week" class="flex items-center gap-1">
                <i class="pi pi-calendar text-gray-400"></i>
                {{ program.days_per_week }}x/week
              </span>
              <span v-if="program.exercises_count" class="flex items-center gap-1">
                <i class="pi pi-list text-gray-400"></i>
                {{ program.exercises_count }} exercises
              </span>
            </div>
            <Button
              icon="pi pi-trash"
              severity="danger"
              text
              rounded
              size="small"
              class="opacity-0 group-hover:opacity-100 transition-opacity"
            />
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>
