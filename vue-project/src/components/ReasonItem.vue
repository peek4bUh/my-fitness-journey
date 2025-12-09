<script setup>
import CircleCheckIcon from '../components/icons/IconCircleCheck.vue'

defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="flex items-center gap-3">
    <CircleCheckIcon class="w-4 text-green-500" />
    <p class="text-gray-700">{{ msg }}</p>
  </div>
</template>
