<template>
  <aside
    class="fixed top-0 left-0 z-100 flex h-screen w-screen flex-col bg-white px-3.5 text-gray-900 transition-all duration-300 ease-in-out lg:border-r lg:border-gray-200 lg:px-5"
    :class="[
      {
        'lg:w-[320px]': isExpanded,
        'lg:w-[90px]': !isExpanded,
        'w-screen translate-x-0': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
        'lg:translate-x-0': true,
      },
    ]"
  >
    <div
      class="mb-px flex justify-between py-4"
      :class="[!isExpanded ? 'lg:justify-center' : 'justify-start']"
    >
      <router-link to="/dashboard/overview">
        <div v-if="isExpanded || isMobileOpen" class="flex w-fit items-center gap-2.5 lg:gap-3">
          <SiteLogo />
          <p class="text-lg font-semibold">MyFitnessJourney</p>
        </div>
        <SiteLogo v-else />
      </router-link>
      <button
        @click="handleToggle"
        class="z-110 flex h-9 w-9 cursor-pointer items-center justify-center rounded-lg border-gray-200 text-gray-500 hover:bg-gray-100 lg:hidden lg:h-9 lg:w-9"
      >
        <CrossIcon />
      </button>
    </div>
    <div class="no-scrollbar flex flex-col overflow-y-auto duration-300 ease-linear">
      <nav class="mb-6">
        <div class="flex flex-col gap-4">
          <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
            <h2
              :class="[
                'mb-4 flex text-xs leading-5 text-gray-400 uppercase',
                !isExpanded ? 'lg:justify-center' : 'justify-start',
              ]"
            >
              <template v-if="isExpanded || isMobileOpen">
                {{ menuGroup.title }}
              </template>
              <HorizontalDots v-else />
            </h2>
            <ul class="flex flex-col gap-0.5">
              <li v-for="item in menuGroup.items" :key="item.name">
                <router-link
                  :to="item.subItems ? item.subItems[0]?.path : item.path"
                  :class="[
                    'flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-gray-900 hover:bg-gray-100',
                    isActive(item.subItems ? item.subItems[0]?.path : item.path)
                      ? 'bg-gray-100'
                      : '',
                  ]"
                >
                  <span class="flex items-center">
                    <component :is="item.icon" />
                  </span>
                  <span v-if="isExpanded || isMobileOpen">{{ item.name }}</span>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <div class="fixed bottom-0 left-0 hidden w-full border-t border-gray-200 px-3 py-2 lg:block">
      <div
        class="border-top w-full cursor-pointer rounded-lg border-gray-200 px-3 pt-2 pb-1.5 hover:bg-gray-100"
      >
        <UserMenu />
      </div>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'

import { GridIcon, HorizontalDots, PageIcon, TableIcon, ListIcon, CrossIcon } from '../../icons'
import { useSidebar } from '@/composables/useSidebar'
import UserMenu from './header/UserMenu.vue'
import SiteLogo from '../SiteLogo.vue'

const { toggleSidebar, toggleMobileSidebar, isMobileOpen, isExpanded } = useSidebar()

const handleToggle = () => {
  if (window.innerWidth >= 1024) {
    toggleSidebar()
  } else {
    toggleMobileSidebar()
  }
}

const route = useRoute()
const menuGroups = [
  {
    title: 'Menu',
    items: [
      {
        icon: GridIcon,
        name: 'Overview',
        path: '/dashboard/overview',
      },
      {
        icon: PageIcon,
        name: 'Programs',
        path: '/dashboard/programs',
      },
      {
        icon: ListIcon,
        name: 'Workouts',
        path: '/dashboard/workouts',
      },
      {
        icon: TableIcon,
        name: 'Body Weights',
        path: '/dashboard/body-weights',
      },
    ],
  },
]

const isActive = (path) => route.path === path
</script>
