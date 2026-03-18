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
          class="cursor-pointer flex items-center justify-center w-9 h-9 text-gray-500 border-gray-200 rounded-lg z-99999 hover:bg-gray-100 lg:h-9 lg:w-9"
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
          <svg
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
          </svg>        
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
