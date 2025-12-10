<script setup>
import LogoutIcon from '@/components/icons/IconLogout.vue'
import PreferencesIcon from '@/components/icons/IconPreferences.vue'
import UserIcon from '@/components/icons/IconUser.vue'
</script>

<template>
  <header
    class="bg-white border-b border-gray-200 px-4 py-2.5 sm:py-2 fixed left-0 right-0 top-0 z-50 md:ml-72"
  >
    <div class="flex justify-between items-center">
      <div class="flex items-center gap-3">
        <!-- Hamburger -->
        <button id="hamburger-sidebar" class="md:hidden border rounded-md border-gray-200 p-1.25">
          <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

        <!-- Section Name -->
        <p class="md:hidden text-sm font-semibold">Overview</p>
      </div>

      <!-- Profile -->
      <div class="relative">
        <button
          id="user-profile"
          class="flex items-center gap-2 p-1.5 rounded-lg hover:bg-gray-100 cursor-pointer"
        >
          <div
            class="w-8 h-8 bg-gray-900 rounded-full flex items-center justify-center text-white text-sm font-medium"
          >
            JD
          </div>
          <div class="hidden sm:block text-left">
            <p class="text-sm font-medium text-gray-900">John Doe</p>
            <p class="text-xs text-gray-500">johndoe@email.com</p>
          </div>
        </button>

        <div
          id="user-profile-dialog"
          class="hidden absolute right-0 mt-3 w-56 origin-top-right rounded-xl bg-white shadow-lg border border-gray-200 py-1 z-50"
        >
          <div class="sm:hidden px-4 py-3 border-b border-gray-200">
            <p class="text-sm font-medium text-gray-900">John Doe</p>
            <p class="text-xs text-gray-600 mt-0.5">johndoe@email.com</p>
          </div>
          <div class="py-1">
            <a
              class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors hover:bg-gray-100 text-gray-700"
              href="#"
            >
              <UserIcon class="w-4 h-4 text-gray-800" />
              Your Profile
            </a>
            <a
              class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors hover:bg-gray-100 text-gray-700"
              href="#"
            >
              <PreferencesIcon class="w-4 h-4 text-gray-800" />
              Settings
            </a>
          </div>
          <div class="py-1 border-t border-gray-200">
            <a
              class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors hover:bg-gray-100 text-gray-700"
              href="#"
            >
              <LogoutIcon class="w-4 h-4 text-red-600" />
              Sign Out
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
