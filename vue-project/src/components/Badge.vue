<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <span class="px-4 py-2 border border-gray-300 rounded-full">
    {{ msg }}
  </span>
</template>
