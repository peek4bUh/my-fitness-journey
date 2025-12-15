<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import Header from '@/components/Header.vue'
import Sidebar from '@/components/Sidebar.vue'

import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import Button from 'primevue/button'

const route = useRoute()
const id = route.params.id
const program = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await axios.get(`http://localhost:7777/api/v0/programs/${id}`, {
      headers: { 'x-api-key': 'a4067f9f41bbd3c8ada4114fa9cae8e3210c41e3f41d4fd010474132767dbfa9' },
    })
    program.value = res.data
    console.log('Program data:', program.value)
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load program'
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

      <div v-else-if="program" class="space-y-6">
        <!-- Header -->
        <div
          class="p-6 bg-white border border-gray-200 rounded-lg flex flex-col sm:flex-row sm:items-center justify-between gap-4"
        >
          <div>
            <h1 class="mb-2 text-2xl font-bold text-gray-900">{{ program.title }}</h1>
            <p class="mb-2 text-sm text-gray-600">{{ program.description }}</p>
            <p class="text-xs text-gray-500">
              Duration: {{ program.duration_weeks }} week<span v-if="program.duration_weeks !== 1"
                >s</span
              >
            </p>
          </div>

          <Button icon="pi pi-plus" label="Add Section" severity="contrast" />
        </div>

        <div class="space-y-4">
          <div
            v-for="(section, sIndex) in program.sections || []"
            :key="sIndex"
            class="bg-white rounded-lg p-6 border border-gray-200"
          >
            <div class="flex flex-col gap-2">
              <h2 class="font-semibold text-base mb-4">{{ section.name }}</h2>
              <DataTable :value="section.exercises || []">
                <Column field="name" header="Exercise" />
                <Column field="sets" header="Sets" />
                <Column field="reps" header="Reps" />
                <Column field="rpe" header="RPE" />
                <Column field="rest_seconds" header="Rest (s)" />
              </DataTable>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
