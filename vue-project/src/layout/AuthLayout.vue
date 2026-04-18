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
      <router-link to="/" class="flex w-fit items-center gap-3 self-start text-xl font-medium">
        <SiteLogo />
        MyFitnessJourney
      </router-link>

      <div class="flex w-full flex-col items-center gap-8">
        <div class="text-center">
          <h2 class="mb-2 text-3xl font-bold text-black lg:text-4xl">
            {{ title }}
          </h2>
          <p class="max-w-md text-gray-600 lg:text-lg">
            {{ subtitle }}
          </p>
        </div>

        <slot />
      </div>
    </div>
  </div>
</template>
