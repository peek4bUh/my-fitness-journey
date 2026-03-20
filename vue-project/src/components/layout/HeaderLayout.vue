<script setup>
import { RouterLink } from 'vue-router'

import { useSidebar } from '@/composables/useSidebar'
import UserMenu from './header/UserMenu.vue'
import { HamburgerIcon, CrossIcon } from '@/icons'

const { toggleSidebar, toggleMobileSidebar, isMobileOpen } = useSidebar()

const handleToggle = () => {
  if (window.innerWidth >= 1024) {
    toggleSidebar()
  } else {
    toggleMobileSidebar()
  }
}
</script>

<template>
  <header class="sticky top-0 z-90 flex w-full border-b border-gray-200 bg-inherit">
    <div class="flex w-full items-center justify-between p-3 lg:justify-end lg:px-5 lg:py-4">
      <div class="flex w-fit items-center gap-2.5 lg:hidden">
        <button
          @click="handleToggle"
          class="flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg border-gray-200 text-gray-500 hover:bg-gray-100"
        >
          <HamburgerIcon v-if="!isMobileOpen" />
          <CrossIcon v-else />
        </button>

        <RouterLink to="/dashboard/overview" class="text-lg font-semibold">
          MyFitnessJourney
        </RouterLink>
      </div>

      <UserMenu />
    </div>
  </header>
</template>
