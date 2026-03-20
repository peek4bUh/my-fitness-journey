<script setup>
import { useRoute } from 'vue-router'

import { GridIcon, PageIcon, TableIcon, ListIcon, CrossIcon } from '../../icons'
import { useSidebar } from '@/composables/useSidebar'
import SiteLogo from '../SiteLogo.vue'

const { isMobileOpen } = useSidebar()

const route = useRoute()
const isActive = (path) => route.path === path
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
</script>

<template>
  <aside
    class="fixed top-[65px] left-0 z-200 flex h-screen w-64 flex-col border-r border-gray-200 bg-gray-50 text-gray-900 transition-all duration-300 ease-in-out lg:top-0 lg:w-80 lg:translate-x-0"
    :class="[
      {
        'translate-x-0': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
      },
    ]"
  >
    <div class="hidden border-b border-gray-200 bg-white lg:block lg:py-4.5 lg:pl-5">
      <router-link to="/dashboard/overview" class="flex w-fit items-center gap-2.5 lg:gap-3">
        <SiteLogo />
        <p class="text-lg font-semibold">MyFitnessJourney</p>
      </router-link>
    </div>
    <div class="px-3 py-5 lg:px-5 lg:py-8">
      <div class="no-scrollbar overflow-y-autoduration-300 flex flex-col ease-linear">
        <nav class="mb-6">
          <div class="flex flex-col gap-4">
            <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
              <h2
                class="mb-4 flex text-xs leading-5 font-semibold tracking-widest text-gray-400 uppercase"
              >
                {{ menuGroup.title }}
              </h2>
              <ul class="flex flex-col gap-0.5">
                <li v-for="item in menuGroup.items" :key="item.name">
                  <router-link
                    :to="item.subItems ? item.subItems[0]?.path : item.path"
                    class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-gray-900 hover:bg-gray-100"
                    :class="[
                      isActive(item.subItems ? item.subItems[0]?.path : item.path)
                        ? 'bg-gray-100'
                        : '',
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
  </aside>
</template>
