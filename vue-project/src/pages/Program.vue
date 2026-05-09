<script setup>
import ProgramCard from '@/components/ProgramCard.vue'
import BaseLayout from '@/layouts/BaseLayout.vue'
import { ProgramService } from '@/services/programService'
import { onMounted, ref } from 'vue'

const programService = new ProgramService()
const programs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await programService.getPrograms()
    programs.value = response.data
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load programs'
    console.error(error.value)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <BaseLayout>
    <!-- Loading State -->
    <div v-if="loading" class="space-y-6">
      <div class="mb-6">
        <div class="mb-2 h-7 w-32 animate-pulse rounded bg-gray-200"></div>
        <div class="h-4 w-64 animate-pulse rounded bg-gray-200"></div>
      </div>
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="i in 6" :key="i" class="rounded-xl border border-gray-200 bg-white p-5">
          <div class="mb-3 flex items-start gap-3">
            <div class="h-12 w-12 animate-pulse rounded-lg bg-gray-200"></div>
            <div class="flex-1">
              <div class="mb-2 h-5 w-24 animate-pulse rounded bg-gray-200"></div>
              <div class="h-3 w-16 animate-pulse rounded bg-gray-200"></div>
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5">
            <div class="h-5 w-16 animate-pulse rounded-full bg-gray-200"></div>
            <div class="h-5 w-20 animate-pulse rounded-full bg-gray-200"></div>
          </div>
          <div class="mt-2 border-t pt-3">
            <div class="flex items-center justify-between">
              <div class="h-3 w-20 animate-pulse rounded bg-gray-200"></div>
              <div class="h-3 w-12 animate-pulse rounded bg-gray-200"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="rounded-lg border border-red-200 bg-red-50 p-6 text-center">
      <div class="mb-2 text-red-600">
        <svg class="mx-auto h-12 w-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
        </svg>
      </div>
      <p class="font-medium">{{ error }}</p>
      <button
        @click="() => window.location.reload()"
        class="mt-4 rounded-lg bg-red-600 px-4 py-2 text-white transition-colors hover:bg-red-700"
      >
        Try Again
      </button>
    </div>

    <!-- Programs Content -->
    <div v-else>
      <!-- Header -->
      <div class="mb-6 hidden lg:block">
        <h1 class="text-xl font-semibold tracking-tight md:text-2xl">Programs</h1>
        <p class="md:text-normal mt-0.5 text-sm text-gray-600">Browse the programs library</p>
      </div>

      <!-- Programs Grid -->
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 auto-rows-fr">
        <ProgramCard
          v-for="program in programs"
          :key="program.id"
          :title="program.title"
          :description="program.description"
          time-range="45-60 min"
          :duration-weeks="8"
          :times-per-week="3"
          :total-exercises="8"
        />
      </div>
    </div>
  </BaseLayout>
</template>
