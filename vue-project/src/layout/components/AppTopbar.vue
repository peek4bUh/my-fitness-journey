<script setup>
import { HamburgerIcon } from '@/icons'
import { useSidebar } from '@/composables/useSidebar'

const { toggleSidebar } = useSidebar()
</script>

<template>
  <div class="sticky top-0 z-50 flex w-full border-b border-gray-200 bg-white">
    <div class="flex w-full items-center justify-between p-3 lg:justify-end lg:px-5 lg:py-4">
      <div class="flex w-fit items-center gap-2 lg:hidden">
        <button
          @click="toggleSidebar()"
          class="flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg text-gray-500 hover:bg-gray-100"
        >
          <HamburgerIcon />
        </button>

        <h2 class="text-lg font-semibold">SectionName</h2>
      </div>
    </div>
  </div>
</template>
