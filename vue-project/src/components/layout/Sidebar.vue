<template>
  <aside
    class="fixed flex flex-col top-0 px-3.5 lg:px-5 left-0 bg-white text-gray-900 w-screen h-screen transition-all duration-300 ease-in-out z-100 lg:border-r lg:border-gray-200"
    :class="[
      {
        'lg:w-[320px]': isExpanded,
        'lg:w-[90px]': !isExpanded,
        'translate-x-0 w-screen': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
        'lg:translate-x-0': true,
      },
    ]"
  >
    <div
      class="py-4 flex justify-between mb-px"
      :class="[!isExpanded ? 'lg:justify-center' : 'justify-start']"
    >
      <router-link to="/dashboard/overview">
        <div v-if="isExpanded || isMobileOpen" class="flex items-center gap-2.5 w-fit lg:gap-3">
          <SiteLogo/>
          <p class="text-lg font-semibold">MyFitnessJourney</p>
        </div>
        <SiteLogo v-else/>
      </router-link>
      <button
          @click="handleToggle"
          class="cursor-pointer flex items-center justify-center w-9 h-9 text-gray-500 border-gray-200 rounded-lg z-110 hover:bg-gray-100 lg:h-9 lg:w-9 lg:hidden"
        >
          <CrossIcon/>
        </button>
    </div>
    <div
      class="flex flex-col overflow-y-auto duration-300 ease-linear no-scrollbar"
    >
      <nav class="mb-6">
        <div class="flex flex-col gap-4">
          <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
            <h2
              :class="[
                'mb-4 text-xs uppercase flex leading-[20px] text-gray-400',
                !isExpanded
                  ? 'lg:justify-center'
                  : 'justify-start',
              ]"
            >
              <template v-if="isExpanded || isMobileOpen">
                {{ menuGroup.title }}
              </template>
              <HorizontalDots v-else />
            </h2>
            <ul class="flex flex-col gap-0.5">
              <li v-for="(item, index) in menuGroup.items" :key="item.name">
                <router-link
                  :to="item.subItems ? item.subItems[0]?.path : item.path"
                  :class="[
                    'flex items-center px-3 py-2.5 gap-3 text-gray-900 rounded-lg hover:bg-gray-100 w-full',
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
    <div class="hidden fixed left-0 bottom-0 w-full border-t border-gray-200 px-3 py-2 lg:block">
        <div
            class="border-top border-gray-200 w-full px-3 pt-2 pb-1.5 rounded-lg cursor-pointer hover:bg-gray-100"
        >
            <UserMenu />
      </div>
    </div>
  </aside>
</template>

<script setup>
import { useRoute } from 'vue-router'

import {
  GridIcon,
  HorizontalDots,
  PageIcon,
  TableIcon,
  ListIcon,
  CrossIcon,
} from '../../icons'
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
