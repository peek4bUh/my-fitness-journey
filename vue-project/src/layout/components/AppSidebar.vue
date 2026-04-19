<script setup>
import { useRoute } from 'vue-router'

import { GridIcon, PageIcon, TableIcon, ListIcon, BoxCubeIcon } from '../../icons'
import { useSidebar } from '@/composables/useSidebar'
import SiteLogo from '../../components/SiteLogo.vue'
import { CrossIcon } from '@/icons'
import AppUserMenu from './AppUserMenu.vue'

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
      },
      {
        icon: PageIcon,
        name: 'Programs',
        path: 'programs',
      },
      {
        icon: ListIcon,
        name: 'Workouts',
        path: null,
      },
      {
        icon: BoxCubeIcon,
        name: 'Exercises',
        path: 'exercises',
      },
      {
        icon: TableIcon,
        name: 'Body Weights',
        path: null,
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
      <AppUserMenu />
    </div>
  </aside>
</template>
