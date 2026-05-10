<script setup>
import Backdrop from '@/components/Backdrop.vue'
import LeftSidebarLayout from '@/layouts/LeftSidebarLayout.vue'
import TopbarLayout from '@/layouts/TopbarLayout.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <LeftSidebarLayout />
    <Backdrop />
    <div class="flex-1 bg-gray-50 transition-all duration-300 ease-in-out lg:ml-80">
      <TopbarLayout />
      <div class="mx-auto max-w-(--breakpoint-3xl) p-6 lg:p-8">
        <RouterView />
      </div>
    </div>
  </div>
</template>
