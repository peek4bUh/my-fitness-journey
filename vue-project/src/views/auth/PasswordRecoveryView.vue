<script setup>
import { reactive } from 'vue'

import AuthLayout from '@/layout/AuthLayout.vue'
import { Form, FormField } from '@primevue/forms'
import InputText from 'primevue/inputtext'
import FloatLabel from 'primevue/floatlabel'
import Button from 'primevue/button'

import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import Message from 'primevue/message'

const initialValues = reactive({
  email: '',
})

const resolver = ({ values }) => {
  const errors = { email: [] }

  if (!values.email) {
    errors.email.push({ type: 'required', message: 'Invalid email.' })
  }

  return { values, errors }
}

async function onFormSubmit({ valid, values }) {
  if (!valid) {
    return
  }

  // Do logic
}
</script>

<template>
  <AuthLayout
    title="Forgotten your password?"
    subtitle="There is nothing to worry about, we'll send you a message to help you reset your password."
  >
    <Form
      v-slot="$form"
      :initialValues="initialValues"
      :resolver="resolver"
      @submit="onFormSubmit"
      class="flex w-full max-w-md flex-col gap-6"
    >
      <!-- Email Field -->
      <FormField class="space-y-1">
        <FloatLabel variant="on">
          <IconField>
            <InputIcon class="pi pi-at" :class="{ 'before:text-red-600': $form.email?.invalid }" />
            <InputText name="email" class="w-full" />
          </IconField>
          <label for="email" class="font-normal!">Email</label>
        </FloatLabel>
        <Message v-if="$form.email?.invalid" severity="error" size="small" variant="simple">
          {{ $form.email.error?.message }}
        </Message>
      </FormField>

      <Button type="submit" label="Login" />
    </Form>
  </AuthLayout>
</template>
