<script setup>
import SiteLogo from '../components/SiteLogo.vue'

defineProps({
  title: String,
  subtitle: String,
})
</script>

<template>
  <div class="flex justify-center bg-[#fafafa] p-4 sm:h-screen sm:items-center">
    <div
      class="flex max-w-3xl grow flex-col items-center gap-16 rounded-xl sm:border sm:border-gray-300 sm:bg-white sm:p-12"
    >
      <RouterLink
        :to="{ name: 'login' }"
        class="flex w-fit items-center gap-3 self-start text-xl font-medium"
      >
        <SiteLogo />
        MyFitnessJourney
      </RouterLink>

      <div class="flex w-full flex-col items-center gap-8">
        <RouterView />
      </div>
    </div>
  </div>
</template>
