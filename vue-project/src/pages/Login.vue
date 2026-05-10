<script setup>
import { reactive } from 'vue'

import { useAuth } from '@/composables/useAuth.js'
import router from '@/router/index.js'
import { Form, FormField } from '@primevue/forms'
import Button from 'primevue/button'
import Checkbox from 'primevue/checkbox'
import FloatLabel from 'primevue/floatlabel'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'

import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import Message from 'primevue/message'

const { login } = useAuth()
const initialValues = reactive({
  username: '',
  password: '',
  rememberMe: false,
})

const resolver = ({ values }) => {
  const errors = { username: [], password: [] }

  if (!values.username) {
    errors.username.push({ type: 'required', message: 'Username is required.' })
  }

  if (!values.password) {
    errors.password.push({ type: 'required', message: 'Password is required.' })
  }

  return { values, errors }
}

async function onFormSubmit({ valid, values }) {
  if (!valid) {
    return
  }

  const result = await login(values.username, values.password)
  if (result.success) {
    router.push({ name: 'dashboard' })
  } else {
    console.error('Login error: ' + result.error)
  }
}
</script>

<template>
  <div class="text-center">
    <h2 class="mb-2 text-3xl font-bold text-black lg:text-4xl">Welcome Back</h2>
    <p class="max-w-md text-gray-600 lg:text-lg">Sign in to continue your journey</p>
  </div>

  <Form
    v-slot="$form"
    :initialValues="initialValues"
    :resolver="resolver"
    @submit="onFormSubmit"
    class="flex w-full max-w-md flex-col gap-8"
  >
    <div class="flex grow flex-col gap-4">
      <!-- Username Field -->
      <FormField class="space-y-1">
        <FloatLabel variant="on">
          <IconField>
            <InputIcon
              class="pi pi-user"
              :class="{ 'before:text-red-600': $form.username?.invalid }"
            />
            <InputText name="username" class="w-full" />
          </IconField>
          <label for="username" class="font-normal!">Username</label>
        </FloatLabel>
        <Message v-if="$form.username?.invalid" severity="error" size="small" variant="simple">
          {{ $form.username.error?.message }}
        </Message>
      </FormField>

      <!-- Password Field -->
      <FormField class="space-y-1">
        <FloatLabel variant="on">
          <IconField>
            <InputIcon
              class="pi pi-lock"
              :class="{ 'before:text-red-600': $form.password?.invalid }"
            />
            <Password
              name="password"
              variant="filled"
              :feedback="false"
              toggleMask
              class="w-full"
              inputClass="w-full bg-white!"
            />
          </IconField>
          <label for="password" class="font-normal!">Password</label>
        </FloatLabel>
        <Message v-if="$form.password?.invalid" severity="error" size="small" variant="simple">
          {{ $form.password.error?.message }}
        </Message>
      </FormField>

      <div class="flex items-center justify-between text-sm">
        <div class="flex cursor-pointer items-center gap-2">
          <Checkbox
            binary
            name="rememberMe"
            class="h-4 w-4 rounded border-gray-300 text-black focus:ring-black"
          />
          <label for="rememberMe" class="text-gray-700">Remember me</label>
        </div>
        <RouterLink
          :to="{ name: 'forgotPassword' }"
          class="text-gray-600 transition-colors hover:text-black"
        >
          Forgot password?
        </RouterLink>
      </div>
    </div>
    <Button type="submit" label="Login" />
  </Form>

  <p class="text-center text-gray-600">
    No account yet?
    <RouterLink :to="{ name: 'signup' }" class="font-medium text-black hover:underline">
      Sign Up
    </RouterLink>
  </p>
</template>
