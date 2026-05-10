<script setup>
import { useSidebar } from '@/composables/useSidebar'
import { useRoute } from 'vue-router'

const { toggleSidebar } = useSidebar()
const route = useRoute()
const titlePage = route.meta.title

document.title = titlePage + ' | MyFitnessJourney'
</script>

<template>
  <header
    class="sticky top-0 z-50 flex w-full border-b border-gray-200 bg-white lg:hidden lg:bg-inherit"
  >
    <div class="flex w-full items-center justify-between px-4 py-3 sm:px-6">
      <div class="flex w-fit items-center gap-2">
        <button
          @click="toggleSidebar()"
          class="flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg text-gray-500 hover:bg-gray-100"
        >
          <span class="pi pi-bars before:text-2xl"></span>
        </button>

        <h2 class="text-lg font-semibold">MyFitnessJourney</h2>
      </div>
    </div>
  </header>
</template>
