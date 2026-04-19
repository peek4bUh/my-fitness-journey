<script setup>
import Card from 'primevue/card'

defineProps({
  title: {
    type: String,
    required: true,
  },
  overview: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
  difficulty: {
    type: String,
    required: true,
  },
  targetMuscle: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <Card
    class="rounded-lg border border-gray-100 shadow-none transition-colors hover:border-gray-200"
  >
    <template #title>
      <h3 class="font-medium text-gray-900">{{ title }}</h3>
    </template>

    <template #subtitle>
      <div class="flex items-center gap-2 text-xs">
        <span class="text-gray-600">{{ type }}</span>
        <span class="text-gray-300">•</span>
        <span class="text-gray-500">{{ difficulty }}</span>
      </div>
    </template>

    <template #content>
      <p class="text-sm leading-relaxed text-gray-500">
        {{ overview }}
      </p>
    </template>

    <template #footer>
      <span class="text-xs text-gray-500">
        <span class="text-gray-400">Target: </span>
        {{ targetMuscle }}
      </span>
    </template>
  </Card>
</template>
