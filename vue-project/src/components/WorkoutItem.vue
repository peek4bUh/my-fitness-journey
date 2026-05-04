<script setup>
defineProps({
  name: String,
  duration: String,
  time: String,
})
</script>

<template>
  <div class="flex items-center justify-between py-3 md:py-4">
    <div>
      <p class="text-sm font-medium md:text-base">{{ name }}</p>
      <p class="text-xs text-gray-600 md:text-sm">{{ duration }}</p>
    </div>
    <span class="text-xs text-gray-600 md:text-sm">{{ time }}</span>
  </div>
</template>
