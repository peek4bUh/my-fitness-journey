<script setup>
import BaseNavbar from '@/components/BaseNavbar.vue'
import { CrossIcon } from '@/components/icons'
import SiteLogo from '@/components/SiteLogo.vue'
import UserInfo from '@/components/UserInfo.vue'
import { useSidebar } from '@/composables/useSidebar'
import { UserService } from '@/services/userService'
import { onMounted, ref } from 'vue'

const userService = new UserService()

const user = ref(null)
const { isMobileOpen, toggleSidebar } = useSidebar()

onMounted(async () => {
  try {
    user.value = await userService.getUserInfo()
  } catch (err) {
    console.error('Failed to load user info:', err)
  }
})
</script>

<template>
  <aside
    class="fixed top-0 left-0 z-95 flex h-screen w-full max-w-112.5 flex-col border-r border-gray-200 bg-white text-gray-900 transition-all duration-300 ease-in-out lg:top-0 lg:w-80 lg:translate-x-0"
    :class="[
      {
        'translate-x-0': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
      },
    ]"
  >
    <div
      class="flex justify-between border-b border-gray-200 bg-inherit px-4 py-3 lg:border-0 lg:px-5 lg:pt-8 lg:pb-4"
    >
      <div class="flex items-center gap-3">
        <SiteLogo />
        <RouterLink :to="{ name: 'dashboard' }" class="flex items-center">
          <h1 class="text-lg font-semibold">MyFitnessJourney</h1>
        </RouterLink>
      </div>

      <button
        @click="toggleSidebar()"
        class="flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg text-gray-500 hover:bg-gray-100"
      >
        <CrossIcon class="lg:hidden" />
      </button>
    </div>

    <BaseNavbar />

    <div class="fixed bottom-0 left-0 w-full border-t border-gray-200 px-4 py-2">
      <UserInfo />
    </div>
  </aside>
</template>
