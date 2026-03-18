<template>
  <header
    class="sticky top-0 flex w-full bg-white border-gray-200 z-90 lg:border-b lg:hidden"
  >
      <div
        class="flex items-center justify-between w-full px-3.5 py-4 border-b border-gray-200 lg:justify-normal lg:border-b-0 lg:px-0 lg:py-4"
      >
        <button
          @click="handleToggle"
          class="flex items-center justify-center w-9 h-9 text-gray-500 border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 lg:h-9 lg:w-9"
          :class="[
            isMobileOpen
              ? 'lg:bg-transparent bg-gray-100'
              : '',
          ]"
        >
          <svg
            v-if="isMobileOpen"
            class="fill-current"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M6.21967 7.28131C5.92678 6.98841 5.92678 6.51354 6.21967 6.22065C6.51256 5.92775 6.98744 5.92775 7.28033 6.22065L11.999 10.9393L16.7176 6.22078C17.0105 5.92789 17.4854 5.92788 17.7782 6.22078C18.0711 6.51367 18.0711 6.98855 17.7782 7.28144L13.0597 12L17.7782 16.7186C18.0711 17.0115 18.0711 17.4863 17.7782 17.7792C17.4854 18.0721 17.0105 18.0721 16.7176 17.7792L11.999 13.0607L7.28033 17.7794C6.98744 18.0722 6.51256 18.0722 6.21967 17.7794C5.92678 17.4865 5.92678 17.0116 6.21967 16.7187L10.9384 12L6.21967 7.28131Z"
              fill=""
            />
          </svg>
          <!-- <svg
            v-else
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 20"
            width="20"
            height="20"
            color="currentColor"
          >
            <path
              fill="currentColor"
              d="M15 1.25a5 5 0 0 1 5 5v7.5a5 5 0 0 1-5 5H5a5 5 0 0 1-5-5v-7.5a5 5 0 0 1 5-5zM7.5 17.1875h7.5A3.4375 3.4375 0 0 0 18.4375 13.75v-7.5A3.4375 3.4375 0 0 0 15 2.8125H7.5zM5 2.8125A3.4375 3.4375 0 0 0 1.5625 6.25v7.5A3.4375 3.4375 0 0 0 5 17.1875h0.9375V2.8125z"
            />
          </svg> -->
          <svg v-else viewBox="0 -0.5 25 25" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M5.5 7.75C5.08579 7.75 4.75 8.08579 4.75 8.5C4.75 8.91421 5.08579 9.25 5.5 9.25V7.75ZM19.5 9.25C19.9142 9.25 20.25 8.91421 20.25 8.5C20.25 8.08579 19.9142 7.75 19.5 7.75V9.25ZM5.5 11.75C5.08579 11.75 4.75 12.0858 4.75 12.5C4.75 12.9142 5.08579 13.25 5.5 13.25V11.75ZM17.5 13.25C17.9142 13.25 18.25 12.9142 18.25 12.5C18.25 12.0858 17.9142 11.75 17.5 11.75V13.25ZM5.5 15.75C5.08579 15.75 4.75 16.0858 4.75 16.5C4.75 16.9142 5.08579 17.25 5.5 17.25V15.75ZM12.5 17.25C12.9142 17.25 13.25 16.9142 13.25 16.5C13.25 16.0858 12.9142 15.75 12.5 15.75V17.25ZM5.5 9.25H19.5V7.75H5.5V9.25ZM5.5 13.25H17.5V11.75H5.5V13.25ZM5.5 17.25H12.5V15.75H5.5V17.25Z" fill="#000000"></path> </g></svg>
        </button>

        <RouterLink to="/dashboard/overview" class="text-lg font-semibold">MyFitnessJourney</RouterLink>

        <div class="cursor-pointer lg:px-3 lg:py-2 lg:fixed lg:left-0 lg:bottom-0 lg:w-full lg:border-t lg:border-gray-200 ">
          <div
            class="lg:px-3 lg:pt-2 lg:pb-1.5 rounded-lg lg:hover:bg-gray-100 lg:border-top lg:border-gray-200"
          >
            <UserMenu />
          </div>
        </div>
    </div>
  </header>
</template>

<script setup>
import { useSidebar } from '@/composables/useSidebar'
import UserMenu from './header/UserMenu.vue'
import { RouterLink } from 'vue-router'

const { toggleSidebar, toggleMobileSidebar, isMobileOpen } = useSidebar()

const handleToggle = () => {
  if (window.innerWidth >= 1024) {
    toggleSidebar()
  } else {
    toggleMobileSidebar()
  }
}
</script>
