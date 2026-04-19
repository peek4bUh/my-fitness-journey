<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterLink } from 'vue-router'

import { UserCircleIcon, LogoutIcon, SettingsIcon } from '@/icons'
import { useAuth } from '@/composables/useAuth.js'

const { logout, user } = useAuth()
const dropdownOpen = ref(false)
const dropdownRef = ref(null)

const menuItems = [
  { href: '/profile', icon: UserCircleIcon, text: 'Edit profile', onClick: null },
  { href: '/chat', icon: SettingsIcon, text: 'Account settings', onClick: null },
  { href: '/login', icon: LogoutIcon, text: 'Sign out', onClick: logout },
]

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const closeDropdown = () => {
  dropdownOpen.value = false
}

const handleClickOutside = (event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    closeDropdown()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <button
    class="flex w-full cursor-pointer items-center gap-3 rounded-lg px-4 pt-2 pb-1.5 hover:bg-gray-100"
    @click.prevent="toggleDropdown"
    ref="dropdownRef"
  >
    <div
      class="flex h-9 w-9 items-center justify-center rounded-full bg-gray-200 text-sm font-semibold text-gray-800"
    >
      AA
    </div>

    <div>
      <p class="text-color text-left text-sm leading-5 font-medium">
        {{ user?.username || 'John Doe' }}
      </p>
      <p class="text-muted-color mt-1 text-xs leading-4">
        {{ user?.email || 'john.doe@email.com' }}
      </p>
    </div>
  </button>

  <!-- Dropdown Start -->
  <div
    v-if="dropdownOpen"
    class="absolute bottom-16 left-1/2 mb-1 flex w-[calc(100%-32px)] -translate-x-1/2 transform flex-col rounded-md border border-gray-200 bg-white p-3"
  >
    <ul class="flex flex-col gap-1">
      <li v-for="item in menuItems" :key="item.href">
        <router-link
          :to="item.href"
          @click="item.onClick ? item.onClick() : null"
          class="group flex items-center gap-3 rounded-lg px-3 py-2 font-medium text-gray-700 hover:bg-gray-100 hover:text-gray-700"
        >
          <component :is="item.icon" class="text-gray-500 group-hover:text-gray-700" />
          {{ item.text }}
        </router-link>
      </li>
    </ul>
  </div>
  <!-- Dropdown End -->
</template>
