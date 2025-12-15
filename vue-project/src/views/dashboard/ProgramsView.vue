<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'

import Button from 'primevue/button'
import DataView from 'primevue/dataview'

const programs = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:7777/api/v0/programs', {
      headers: { 'x-api-key': 'a4067f9f41bbd3c8ada4114fa9cae8e3210c41e3f41d4fd010474132767dbfa9' },
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

      <div v-else class="bg-white rounded-lg p-6 border border-gray-200">
        <DataView :value="programs">
          <template #list="slotProps">
            <div class="flex flex-col">
              <div
                v-for="(program, index) in slotProps.items"
                :key="program.id"
                class="flex flex-col sm:flex-row p-4 sm:items-center"
                :class="{ 'border-t border-surface-200': index !== 0 }"
              >
                <div class="flex flex-col md:flex-row justify-between md:items-center flex-1 gap-6">
                  <div>
                    <RouterLink
                      :to="`/dashboard/programs/${program.id}`"
                      class="block text-lg font-semibold mb-1 hover:underline cursor-pointer"
                    >
                      {{ program.title }}
                    </RouterLink>
                    <span class="inline-block font-medium text-surface-500 text-sm mb-2">
                      {{ program.duration_weeks }} Weeks
                    </span>
                    <p>{{ program.description }}</p>
                  </div>
                  <div class="flex flex-col md:items-end gap-2">
                    <Button icon="pi pi-trash" severity="danger" />
                  </div>
                </div>
              </div>
            </div>
          </template>
        </DataView>
      </div>
    </div>
  </main>
</template>
