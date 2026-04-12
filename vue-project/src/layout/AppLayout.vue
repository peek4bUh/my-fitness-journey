<script setup>
import AppSidebar from './components/AppSidebar.vue'
import AppTopbar from './components/AppTopbar.vue'
import Backdrop from '../components/Backdrop.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <AppSidebar />
    <Backdrop />
    <div class="flex-1 bg-gray-50 transition-all duration-300 ease-in-out lg:ml-80">
      <AppTopbar />
      <div class="mx-auto max-w-(--breakpoint-3xl) p-4 sm:p-6 lg:p-10">
        <slot />
      </div>
    </div>
  </div>
</template>
