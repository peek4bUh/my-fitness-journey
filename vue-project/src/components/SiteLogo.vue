<script setup>
import DumbellIcon from '../components/icons/IconDumbell.vue'

defineProps({
  url: {
    type: String,
    required: true,
    default: '/',
  },
})
</script>

<template>
  <RouterLink :to="url" class="flex items-center gap-2 lg:gap-3 w-fit">
    <span class="w-7 h-7 lg:w-9 lg:h-9 bg-black rounded-lg flex items-center justify-center">
      <DumbellIcon class="w-4 h-4 lg:w-5 lg:h-5 text-white" />
    </span>
    <p class="lg:text-xl font-semibold">MyFitnessJourney</p>
  </RouterLink>
</template>
