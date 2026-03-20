<script setup>
import { useSidebar } from '@/composables/useSidebar'
const { toggleMobileSidebar, isMobileOpen } = useSidebar()
</script>

<template>
  <div
    v-if="isMobileOpen"
    class="fixed inset-0 z-40 bg-gray-900/50 lg:hidden"
    @click="toggleMobileSidebar"
  ></div>
</template>
