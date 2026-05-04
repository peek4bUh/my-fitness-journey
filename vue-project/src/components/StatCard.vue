<script setup>
defineProps({
  title: String,
  value: String,
  subtitle: String,
})
</script>

<template>
  <div class="rounded-md border border-gray-200 bg-white p-4">
    <div class="mb-4 flex items-center justify-between">
      <div>
        <h3 class="text-sm font-medium text-gray-600">{{ title }}</h3>

        <p class="text-2xl font-bold text-gray-900">{{ value }}</p>
      </div>
    </div>

    <p class="text-sm text-gray-600">{{ subtitle }}</p>
  </div>
</template>
