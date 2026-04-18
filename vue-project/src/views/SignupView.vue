<script setup>
import { reactive, ref } from 'vue'

import AuthLayout from '@/layout/AuthLayout.vue'
import { useAuth } from '../composables/useAuth.js'
import router from '../router/index.js'
import { Form } from '@primevue/forms'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import FloatLabel from 'primevue/floatlabel'
import Button from 'primevue/button'

import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'

const { login } = useAuth()

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const initialValues = reactive({
  username: '',
})

const resolver = ({ values }) => {
  const errors = {}

  if (!values.username) {
    errors.username = [{ message: 'Username is required.' }]
  }

  return {
    values, // (Optional) Used to pass current form values to submit event.
    errors,
  }
}

async function handleLogin() {
  const result = await login(username.value, password.value)

  if (result.success) {
    router.push('/dashboard/overview')
  } else {
    errorMessage.value = result.error
  }
}
</script>

<template>
  <AuthLayout title="Create Account" subtitle="Start your journey today">
    <Form
      v-slot="$form"
      :initialValues
      :resolver
      @submit="handleLogin"
      class="flex w-full max-w-md flex-col gap-8"
    >
      <div class="flex grow flex-col gap-4">
        <FloatLabel variant="on">
          <IconField>
            <InputIcon class="pi pi-user" />
            <InputText id="username" v-model="username" autocomplete="off" class="w-full" />
          </IconField>
          <label for="username" class="font-normal! text-gray-500!">Username</label>
        </FloatLabel>

        <FloatLabel variant="on">
          <IconField>
            <InputIcon class="pi pi-at" />
            <InputText id="email" v-model="email" autocomplete="off" class="w-full" />
          </IconField>
          <label for="email" class="font-normal! text-gray-500!">Email</label>
        </FloatLabel>

        <FloatLabel variant="on">
          <IconField>
            <InputIcon class="pi pi-lock" />
            <Password
              id="password"
              v-model="password"
              inputId="password"
              variant="filled"
              :feedback="false"
              toggleMask
              class="w-full"
              inputClass="w-full bg-white!"
            />
          </IconField>
          <label for="password" class="font-normal! text-gray-500!">Password</label>
        </FloatLabel>

        <FloatLabel variant="on">
          <IconField>
            <InputIcon class="pi pi-lock" />
            <Password
              id="password"
              v-model="password"
              inputId="password"
              variant="filled"
              :feedback="false"
              toggleMask
              class="w-full"
              inputClass="w-full bg-white!"
            />
          </IconField>
          <label for="password" class="font-normal! text-gray-500!">Repeat Password</label>
        </FloatLabel>
      </div>
      <Button type="submit" label="Create" />
    </Form>

    <p class="text-center text-gray-600">
      Already registered?
      <RouterLink :to="{ name: 'login' }" class="font-medium text-black hover:underline"
        >Login</RouterLink
      >
    </p>
  </AuthLayout>
</template>
