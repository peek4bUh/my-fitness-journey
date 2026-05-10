<script setup>
import { reactive } from 'vue'

import { Form, FormField } from '@primevue/forms'
import Button from 'primevue/button'
import FloatLabel from 'primevue/floatlabel'
import InputText from 'primevue/inputtext'

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

async function onFormSubmit({ valid }) {
  if (!valid) {
    return
  }

  // Do logic
}
</script>

<template>
  <div class="text-center">
    <h2 class="mb-2 text-3xl font-bold text-black lg:text-4xl">Forgotten your password?</h2>
    <p class="max-w-md text-gray-600 lg:text-lg">
      There is nothing to worry about, we'll send you a message to help you reset your password.
    </p>
  </div>

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
</template>
