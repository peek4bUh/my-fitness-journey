<script setup>
import Backdrop from '@/components/Backdrop.vue'
import BaseHeader from '@/components/layouts/BaseHeader.vue'
import BaseSidebar from '@/components/layouts/BaseSidebar.vue'
</script>

<template>
  <div class="min-h-screen xl:flex">
    <BaseSidebar />
    <Backdrop />
    <div class="flex-1 bg-gray-50 transition-all duration-300 ease-in-out lg:ml-80">
      <BaseHeader />
      <main class="mx-auto max-w-(--breakpoint-3xl) p-6 lg:p-8">
        <RouterView />
      </main>
    </div>
  </div>
</template>
