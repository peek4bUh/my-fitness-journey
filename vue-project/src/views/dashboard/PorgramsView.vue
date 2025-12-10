<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'

const programs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:7777/api/v0/programs', {
      headers: {
        'x-api-key': 'a4067f9f41bbd3c8ada4114fa9cae8e3210c41e3f41d4fd010474132767dbfa9',
      },
    })
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
  <Header />

  <main class="bg-gray-50 md:pl-72 pt-[65px]">
    <Sidebar />

    <div id="content" class="p-4 md:p-6 lg:p-8">
      <div v-if="loading" class="text-center text-gray-500">Loading...</div>
      <div v-else-if="error" class="p-4 bg-red-50 border border-red-200 rounded-lg text-red-600">
        {{ error }}
      </div>

      <div v-else class="bg-white rounded-lg border border-gray-200 overflow-hidden">
        <div
          v-for="program in programs"
          :key="program.id"
          class="flex items-center p-4 border-b border-gray-200 hover:bg-gray-50 transition-colors group"
        >
          <div class="grow min-w-0">
            <RouterLink
              :to="`/dashboard/programs/${program.id}`"
              class="text-base font-medium text-gray-900 hover:underline cursor-pointer"
            >
              {{ program.title }}
            </RouterLink>
            <p class="text-xs text-gray-500 mt-0.5 mb-1">{{ program.duration_weeks }} weeks</p>
            <p class="text-sm text-gray-600 line-clamp-1">{{ program.description }}</p>
          </div>

          <button
            type="button"
            class="p-2 bg-red-500 hover:bg-red-600/90 rounded-sm cursor-pointer"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </main>
</template>
