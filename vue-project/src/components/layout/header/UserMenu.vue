<script setup>
import { UserCircleIcon, LogoutIcon, SettingsIcon } from '@/icons'
import { RouterLink } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import { useAuth } from '@/composables/useAuth.js'

const { logout, user } = useAuth()

const dropdownOpen = ref(false)
const dropdownRef = ref(null)

const menuItems = [
  { href: '/profile', icon: UserCircleIcon, text: 'Edit profile' },
  { href: '/chat', icon: SettingsIcon, text: 'Account settings' },
]

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const closeDropdown = () => {
  dropdownOpen.value = false
}

const signOut = () => {
  logout()
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
  <div class="relative" ref="dropdownRef">
    <button class="flex cursor-pointer items-center" @click.prevent="toggleDropdown">
      <div
        class="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 text-sm font-semibold text-gray-800"
      >
        AA
      </div>
    </button>

    <!-- Dropdown Start -->
    <div
      v-if="dropdownOpen"
      class="absolute right-0 mt-2 flex w-[260px] flex-col rounded-2xl border border-gray-200 bg-white p-3"
    >
      <div class="mb-3">
        <p class="font-medium text-gray-700">{{ user?.username || 'User' }}</p>
        <p class="mt-0.5 text-gray-500">{{ user?.email || '' }}</p>
      </div>

      <ul class="flex flex-col gap-1 border-y border-gray-200 pt-3 pb-3">
        <li v-for="item in menuItems" :key="item.href">
          <router-link
            :to="item.href"
            class="group flex items-center gap-3 rounded-lg px-3 py-2 font-medium text-gray-700 hover:bg-gray-100 hover:text-gray-700"
          >
            <component :is="item.icon" class="text-gray-500 group-hover:text-gray-700" />
            {{ item.text }}
          </router-link>
        </li>
      </ul>
      <router-link
        to="/login"
        @click="signOut"
        class="group mt-3 flex items-center gap-3 rounded-lg px-3 py-2 font-medium text-gray-700 hover:bg-gray-100 hover:text-gray-700"
      >
        <LogoutIcon class="text-gray-500 group-hover:text-gray-700" />
        Sign out
      </router-link>
    </div>
    <!-- Dropdown End -->
  </div>
</template>
