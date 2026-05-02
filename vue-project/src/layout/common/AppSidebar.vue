<script setup>
import {
  BoxCubeIcon,
  CrossIcon,
  GridIcon,
  ListIcon,
  LogoutIcon,
  PageIcon,
  SettingsIcon,
  UserCircleIcon,
} from '@/components/icons'
import SiteLogo from '@/components/SiteLogo.vue'
import { useAuth } from '@/composables/useAuth.js'
import { useSidebar } from '@/composables/useSidebar'
import router from '@/router/index.js'
import Avatar from 'primevue/avatar'
import { useRoute } from 'vue-router'

const route = useRoute()
const isActive = (itemPath) => route.path === `/${itemPath}`

const { logout, user } = useAuth()
const { isMobileOpen, toggleSidebar } = useSidebar()
const handleLogout = async () => {
  await logout()
  router.push({ name: 'login' })
}
const menuGroups = [
  {
    title: 'Menu',
    items: [
      {
        icon: GridIcon,
        label: 'Dashboard',
        name: 'dashboard',
        onClick: null,
      },
      {
        icon: PageIcon,
        label: 'Programs',
        name: 'programs',
        onClick: null,
      },
      {
        icon: ListIcon,
        label: 'Workouts',
        name: null,
        onClick: null,
      },
      {
        icon: BoxCubeIcon,
        label: 'Exercises',
        name: 'exercises',
        onClick: null,
      },
    ],
  },
  {
    title: 'Account',
    items: [
      {
        icon: UserCircleIcon,
        label: 'Profile',
        name: null,
        onClick: null,
      },
      {
        icon: SettingsIcon,
        label: 'Settings',
        name: null,
        onClick: null,
      },
      {
        icon: LogoutIcon,
        label: 'Logout',
        name: null,
        onClick: handleLogout,
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
        <RouterLink :to="{ name: 'dashboard' }" class="flex items-center">
          <h1 class="text-lg font-semibold">MyFitnessJourney</h1>
        </RouterLink>
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
                <li v-for="item in menuGroup.items" :key="item.label">
                  <RouterLink
                    v-if="!item.onClick"
                    :to="{ name: item.name !== null ? item.name : 'login' }"
                    class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5"
                    :class="[
                      isActive(item.name)
                        ? 'bg-primary text-white'
                        : 'text-gray-900 hover:bg-gray-100',
                    ]"
                  >
                    <span class="flex items-center">
                      <component :is="item.icon" />
                    </span>
                    <span>{{ item.label }}</span>
                  </RouterLink>

                  <button
                    v-else
                    @click="item.onClick"
                    class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 cursor-pointer"
                    :class="['text-gray-900 hover:bg-gray-100']"
                  >
                    <span class="flex items-center">
                      <component :is="item.icon" />
                    </span>
                    <span>{{ item.label }}</span>
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>

    <!-- User Info -->
    <div class="fixed bottom-0 left-0 w-full border-t border-gray-200 px-4 py-2">
      <div class="flex w-full items-center gap-3 rounded-lg px-4 pt-2 pb-1.5">
        <Avatar class="w-9! h-9!" icon="pi pi-user" shape="circle" />

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
