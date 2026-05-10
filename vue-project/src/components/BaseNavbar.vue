<script setup>
import { useAuth } from '@/composables/useAuth.js'
import { menuGroups } from '@/config/navigation.js'
import router from '@/router/index.js'
import { useRoute } from 'vue-router'

const route = useRoute()
const { logout } = useAuth()

const isActive = (itemName) => {
  if (!itemName) return false
  return route.path === `/app/${itemName}` || route.name?.startsWith(itemName + '-')
}

const handleLogout = async () => {
  await logout()
  router.push({ name: 'login' })
}
</script>

<template>
  <div class="px-4 py-5 lg:px-5 lg:py-6">
    <div class="no-scrollbar overflow-y-auto duration-300 flex flex-col ease-linear">
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
                <!-- Si tiene ruta definida y NO es una acción especial -->
                <RouterLink
                  v-if="item.name && !item.action"
                  :to="{ name: item.name }"
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

                <!-- Logout Button -->
                <button
                  v-else-if="item.action"
                  @click="handleLogout(item)"
                  class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 cursor-pointer text-gray-900 hover:bg-gray-100"
                >
                  <span class="flex items-center">
                    <component :is="item.icon" />
                  </span>
                  <span>{{ item.label }}</span>
                </button>

                <!-- Disable item if no route or action is defined -->
                <div
                  v-else
                  class="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-gray-400 cursor-not-allowed"
                >
                  <span class="flex items-center">
                    <component :is="item.icon" />
                  </span>
                  <span>{{ item.label }}</span>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>
