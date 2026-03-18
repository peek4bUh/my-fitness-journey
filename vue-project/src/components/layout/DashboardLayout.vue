<template>
  <div class="min-h-screen xl:flex">
    <Sidebar />
    <Backdrop />
    <div
      class="flex-1 transition-all duration-300 ease-in-out"
      :class="[isExpanded ? 'lg:ml-80' : 'lg:ml-[90px]']"
    >
      <Header />
      <div class="mx-auto max-w-(--breakpoint-2xl) p-4 md:p-6">
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
import Sidebar from './SidebarLayout.vue'
import Header from './HeaderLayout.vue'
import { useSidebar } from '@/composables/useSidebar'

const { isExpanded } = useSidebar()
</script>
