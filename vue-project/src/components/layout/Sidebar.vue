<template>
  <aside
    :class="[
      'fixed mt-16 flex flex-col lg:mt-0 top-0 px-5 left-0 bg-white text-gray-900 h-screen transition-all duration-300 ease-in-out z-99999 border-r border-gray-200',
      {
        'lg:w-[290px]': isExpanded || isMobileOpen || isHovered,
        'lg:w-[90px]': !isExpanded && !isHovered,
        'translate-x-0 w-[290px]': isMobileOpen,
        '-translate-x-full': !isMobileOpen,
        'lg:translate-x-0': true,
      },
    ]"
    @mouseenter="!isExpanded && (isHovered = true)"
    @mouseleave="isHovered = false"
  >
    <div
      :class="[
        'py-8 flex',
        !isExpanded && !isHovered ? 'lg:justify-center' : 'justify-start',
      ]"
    >
      <router-link to="/">
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          src="/images/logo/logo.svg"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-if="isExpanded || isHovered || isMobileOpen"
          class="hidden"
          src="/images/logo/logo-dark.svg"
          alt="Logo"
          width="150"
          height="40"
        />
        <img
          v-else
          src="/images/logo/logo-icon.svg"
          alt="Logo"
          width="32"
          height="32"
        />
      </router-link>
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
                !isExpanded && !isHovered
                  ? 'lg:justify-center'
                  : 'justify-start',
              ]"
            >
              <template v-if="isExpanded || isHovered || isMobileOpen">
                {{ menuGroup.title }}
              </template>
              <HorizontalDots v-else />
            </h2>
            <ul class="flex flex-col">
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
                  <span v-if="isExpanded || isHovered || isMobileOpen">{{ item.name }}</span>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <div class="fixed left-0 bottom-0 w-full border-t border-gray-200 p-2">
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
  CalenderIcon,
  UserCircleIcon,
  HorizontalDots,
  PageIcon,
  TableIcon,
  ListIcon,
} from '../../icons'
import { useSidebar } from '@/composables/useSidebar'
import UserMenu from './header/UserMenu.vue'

const route = useRoute()
const { isExpanded, isMobileOpen, isHovered } = useSidebar()
const menuGroups = [
  {
    title: 'Menu',
    items: [
      {
        icon: GridIcon,
        name: 'Overview',
        subItems: [{ name: 'Ecommerce', path: '/', pro: false }],
      },
      {
        icon: CalenderIcon,
        name: 'Calendar',
        path: '/calendar',
      },
      {
        icon: UserCircleIcon,
        name: 'User Profile',
        path: '/profile',
      },

      {
        name: 'Forms',
        icon: ListIcon,
        subItems: [
          { name: 'Form Elements', path: '/form-elements', pro: false },
        ],
      },
      {
        name: 'Tables',
        icon: TableIcon,
        subItems: [{ name: 'Basic Tables', path: '/basic-tables', pro: false }],
      },
      {
        name: 'Pages',
        icon: PageIcon,
        subItems: [
          { name: 'Black Page', path: '/blank', pro: false },
          { name: '404 Page', path: '/error-404', pro: false },
        ],
      },
    ],
  },
]

const isActive = (path) => route.path === path
</script>
