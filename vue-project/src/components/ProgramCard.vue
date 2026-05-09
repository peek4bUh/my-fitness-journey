<script setup>
import Card from 'primevue/card'

defineProps({
  title: { type: String, required: true },
  description: { type: String, required: true },
  timeRange: { type: String, required: true },
  durationWeeks: { type: Number, required: true },
  timesPerWeek: { type: Number, required: true },
  totalExercises: { type: Number, required: true },
})
</script>

<template>
  <Card
    :pt="{
      root: 'bg-white rounded-2xl shadow-md border border-gray-200 overflow-hidden transition hover:shadow-lg',
      header: 'px-6 pt-6 pb-2',
      body: 'px-6 pb-6',
      content: 'space-y-4',
      title: 'text-xl font-bold text-gray-800',
      subtitle: 'text-sm text-gray-500',
    }"
  >
    <template #title>{{ title }}</template>
    <template #content>
      <p class="text-gray-600 leading-relaxed">{{ description }}</p>

      <!-- Stat grid: time, duration, sessions/week, total exercises -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4">
        <div class="flex flex-col items-center p-3 bg-gray-50 rounded-xl">
          <span class="text-xs font-medium text-gray-500 uppercase tracking-wide">Time</span>
          <span class="mt-1 font-semibold text-gray-800">{{ timeRange }}</span>
        </div>
        <div class="flex flex-col items-center p-3 bg-gray-50 rounded-xl">
          <span class="text-xs font-medium text-gray-500 uppercase tracking-wide">Duration</span>
          <span class="mt-1 font-semibold text-gray-800">{{ durationWeeks }} weeks</span>
        </div>
        <div class="flex flex-col items-center p-3 bg-gray-50 rounded-xl">
          <span class="text-xs font-medium text-gray-500 uppercase tracking-wide">Per Week</span>
          <span class="mt-1 font-semibold text-gray-800">{{ timesPerWeek }}x</span>
        </div>
        <div class="flex flex-col items-center p-3 bg-gray-50 rounded-xl">
          <span class="text-xs font-medium text-gray-500 uppercase tracking-wide">Exercises</span>
          <span class="mt-1 font-semibold text-gray-800">{{ totalExercises }}</span>
        </div>
      </div>
    </template>
  </Card>
</template>
