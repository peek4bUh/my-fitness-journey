<script setup>
import { UserService } from '@/services/userService'
import Avatar from 'primevue/avatar'
import { onMounted, ref } from 'vue'

const userService = new UserService()
const user = ref(null)

onMounted(async () => {
  try {
    user.value = await userService.getUserInfo()
  } catch (err) {
    console.error('Failed to load user info:', err)
  }
})
</script>

<template>
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
</template>
