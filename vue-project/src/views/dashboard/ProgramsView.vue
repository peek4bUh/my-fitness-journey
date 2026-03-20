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
      <div v-else-if="error" class="rounded-lg border border-red-200 bg-red-50 p-4 text-red-600">
        {{ error }}
      </div>

      <!-- Programs Grid -->
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div
          v-for="program in programs"
          :key="program.id"
          class="group overflow-hidden rounded-xl border border-gray-200 bg-white transition-all duration-200 hover:border-gray-300 hover:shadow-lg"
        >
          <!-- Card Header -->
          <div class="p-5 pb-3">
            <div class="mb-2 flex items-start justify-between gap-3">
              <RouterLink
                :to="`/dashboard/programs/${program.id}`"
                class="line-clamp-2 text-lg font-semibold text-gray-900 transition-colors hover:text-blue-600"
              >
                {{ program.title }}
              </RouterLink>
              <span
                class="shrink-0 rounded-full bg-blue-50 px-2.5 py-1 text-xs font-medium text-blue-700"
              >
                {{ program.duration_weeks }} Weeks
              </span>
            </div>
            <p class="line-clamp-2 text-sm leading-relaxed text-gray-600">
              {{ program.description }}
            </p>
          </div>

          <!-- Card Footer -->
          <div
            class="flex items-center justify-between border-t border-gray-100 bg-gray-50 px-5 py-3"
          >
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
              class="opacity-0 transition-opacity group-hover:opacity-100"
            />
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>
