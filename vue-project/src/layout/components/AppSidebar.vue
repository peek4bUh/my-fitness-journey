<script setup>
import { useRoute } from 'vue-router'

import { useAuth } from '@/composables/useAuth.js'
import { useSidebar } from '@/composables/useSidebar'
import { CrossIcon } from '@/icons'
import SiteLogo from '../../components/SiteLogo.vue'
import {
  BoxCubeIcon,
  GridIcon,
  ListIcon,
  LogoutIcon,
  PageIcon,
  SettingsIcon,
  UserCircleIcon,
} from '../../icons'

const { logout, user } = useAuth()
const { isMobileOpen, toggleSidebar } = useSidebar()
const route = useRoute()
const isActive = (itemPath) => route.path === `/${itemPath}`
const menuGroups = [
  {
    title: 'Menu',
    items: [
      {
        icon: GridIcon,
        name: 'Dashboard',
        path: 'dashboard',
        onClick: null,
      },
      {
        icon: PageIcon,
        name: 'Programs',
        path: 'programs',
        onClick: null,
      },
      {
        icon: ListIcon,
        name: 'Workouts',
        path: null,
        onClick: null,
      },
      {
        icon: BoxCubeIcon,
        name: 'Exercises',
        path: 'exercises',
        onClick: null,
      },
    ],
  },
  {
    title: 'Account',
    items: [
      {
        icon: UserCircleIcon,
        name: 'Profile',
        path: null,
        onClick: null,
      },
      {
        icon: SettingsIcon,
        name: 'Settings',
        path: null,
        onClick: null,
      },
      {
        icon: LogoutIcon,
        name: 'Logout',
        path: 'login',
        onClick: logout,
      },
    ],
  },
]
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
        <router-link :to="{ name: 'dashboard' }" class="flex items-center">
          <h1 class="text-lg font-semibold">MyFitnessJourney</h1>
        </router-link>
      </div>

      <button
        @click="toggleSidebar()"
        class="flex h-10 w-10 cursor-pointer items-center justify-center rounded-lg text-gray-500 hover:bg-gray-100"
      >
        <CrossIcon class="lg:hidden" />
      </button>
    </div>

    <div class="px-4 py-5 lg:px-5 lg:py-6">
      <div class="no-scrollbar overflow-y-autoduration-300 flex flex-col ease-linear">
        <nav class="mb-6">
          <div class="flex flex-col gap-4">
            <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
              <h2
                class="mb-4 flex text-xs leading-5 font-semibold tracking-widest text-gray-400 uppercase"
              >
                {{ menuGroup.title }}
              </h2>
              <ul class="flex flex-col gap-1.5">
                <li v-for="item in menuGroup.items" :key="item.name">
                  <router-link
                    :to="{
                      name: item.subItems?.length ? item.subItems[0].path : item.path,
                    }"
                    class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5"
                    :class="[
                      isActive(item.subItems ? item.subItems[0]?.path : item.path)
                        ? 'bg-primary text-white'
                        : 'text-gray-900 hover:bg-gray-100',
                    ]"
                    @click="item.onClick ? item.onClick() : null"
                  >
                    <span class="flex items-center">
                      <component :is="item.icon" />
                    </span>
                    <span>{{ item.name }}</span>
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>

    <div class="fixed bottom-0 left-0 w-full border-t border-gray-200 px-4 py-2">
      <!-- User Info -->
      <div class="flex w-full items-center gap-3 rounded-lg px-4 pt-2 pb-1.5">
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
      </div>
    </div>
  </aside>
</template>
