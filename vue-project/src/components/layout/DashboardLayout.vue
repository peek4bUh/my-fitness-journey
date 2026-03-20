<script setup>
import Sidebar from './SidebarLayout.vue'
import Header from './HeaderLayout.vue'
import Backdrop from '../Backdrop.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <Sidebar />
    <Backdrop />
    <div class="flex-1 bg-white transition-all duration-300 ease-in-out lg:ml-80">
      <Header />
      <div class="mx-auto max-w-(--breakpoint-2xl) p-4 md:p-6">
        <slot />
      </div>
    </div>
  </div>
</template>
