<template>
  <div class="relative" ref="dropdownRef">
    <button
      class="cursor-pointer flex items-center text-gray-700"
      @click.prevent="toggleDropdown"
    >
      <div class="flex items-center justify-center rounded-full h-9 w-9 lg:h-10 lg:w-10 bg-gray-200 text-gray-800 font-semibold text-sm lg:mr-3">
        AA
      </div>

      <p class="hidden text-sm">Angel Andrade</p>
    </button>

    <!-- Dropdown Start -->
    <div
      v-if="dropdownOpen"
      class="absolute right-0 mt-2 flex w-[260px] flex-col rounded-2xl border border-gray-200 bg-white p-3"
    >
      <div class="mb-3">
        <p class="font-medium text-gray-700">
          Musharof Chowdhury
        </p>
        <p class="mt-0.5 text-gray-500">
          aandradeb99@gmail.com
        </p>
      </div>

      <ul class="flex flex-col gap-1 pt-3 pb-3 border-y border-gray-200">
        <li v-for="item in menuItems" :key="item.href">
          <router-link
            :to="item.href"
            class="flex items-center gap-3 px-3 py-2 font-medium text-gray-700 rounded-lg group hover:bg-gray-100 hover:text-gray-700"
          >
            <component
              :is="item.icon"
              class="text-gray-500 group-hover:text-gray-700"
            />
            {{ item.text }}
          </router-link>
        </li>
      </ul>
      <router-link
        to="/signin"
        @click="signOut"
        class="flex items-center gap-3 px-3 py-2 mt-3 font-medium text-gray-700 rounded-lg group hover:bg-gray-100 hover:text-gray-700"
      >
        <LogoutIcon
          class="text-gray-500 group-hover:text-gray-700"
        />
        Sign out
      </router-link>
    </div>
    <!-- Dropdown End -->
  </div>
</template>

<script setup>
import { UserCircleIcon, LogoutIcon, SettingsIcon } from '@/icons'
import { RouterLink } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue'

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
  // Implement sign out logic here
  console.log('Signing out...')
  closeDropdown()
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
