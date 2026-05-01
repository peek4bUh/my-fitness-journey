<script setup>
import Backdrop from '../components/Backdrop.vue'
import AppSidebar from './components/AppSidebar.vue'
import AppTopbar from './components/AppTopbar.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <AppSidebar />
    <Backdrop />
    <div class="flex-1 bg-gray-50 transition-all duration-300 ease-in-out lg:ml-80">
      <AppTopbar />
      <div class="mx-auto max-w-(--breakpoint-3xl) p-6 lg:p-8">
        <slot />
      </div>
    </div>
  </div>
</template>
