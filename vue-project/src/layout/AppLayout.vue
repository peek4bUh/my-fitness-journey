<script setup>
import Sidebar from './components/AppSidebar.vue'
import Header from './components/AppTopbar.vue'
import Backdrop from '../components/Backdrop.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <Sidebar />
    <Backdrop />
    <div class="flex-1 bg-gray-50 transition-all duration-300 ease-in-out lg:ml-80">
      <Header />
      <div class="mx-auto max-w-(--breakpoint-2xl) p-4 md:p-6">
        <slot />
      </div>
    </div>
  </div>
</template>
