<script setup>
import { ref } from 'vue'
import SiteLogo from '../components/SiteLogo.vue'
import router from '../router/index.js'
import { useAuth } from '../composables/useAuth.js'

const { login } = useAuth()

const username = ref('')
const password = ref('')
const errorMessage = ref('')

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
  <div class="flex h-screen">
    <!-- Left Column -->
    <div class="relative hidden basis-2/4 lg:block">
      <img
        class="absolute z-0 h-full object-cover"
        src="../assets/images/bb-romanian-deadlift.jpg"
        alt="Barbell Romanian Deadlift"
      />
      <div
        class="absolute inset-0 z-10 flex h-full w-full flex-col items-start justify-center bg-black/50 pl-10"
      >
        <h2 class="mb-4 text-4xl font-bold text-white drop-shadow-lg md:text-5xl">
          Push Your Limits.
        </h2>
        <p class="max-w-md text-lg text-gray-200">
          Every small step adds up. Stay consistent, show up, and watch your journey transform.
        </p>
      </div>
    </div>

    <!-- Right Column -->
    <div class="flex grow basis-1/2 flex-col justify-between p-6">
      <router-link to="/" class="flex w-fit items-center gap-2.5 lg:gap-3">
        <SiteLogo />
        <p class="text-lg font-semibold">MyFitnessJourney</p>
      </router-link>

      <div class="flex flex-1 items-center justify-center">
        <div class="w-full max-w-md">
          <div class="mt-0 mb-8 text-center">
            <h2 class="mb-2 text-3xl font-bold text-black lg:text-4xl">Welcome Back</h2>
            <p class="text-gray-600 lg:text-lg">Sign in to continue your fitness journey</p>
          </div>

          <form method="post" v-on:submit.prevent="handleLogin" class="flex flex-col gap-6">
            <div>
              <label
                for="username"
                class="mb-1 block text-sm font-semibold text-gray-600 lg:text-base"
              >
                Username
              </label>
              <input
                type="text"
                id="username"
                v-model="username"
                required
                class="w-full border-b border-gray-400 bg-transparent py-1 text-sm transition-colors focus:border-black focus:outline-none lg:text-base"
              />
            </div>

            <div>
              <label
                for="password"
                class="mb-1 block text-sm font-semibold text-gray-600 lg:text-base"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                v-model="password"
                required
                class="w-full border-b border-gray-400 bg-transparent py-1 text-sm transition-colors focus:border-black focus:outline-none lg:text-base"
              />
            </div>

            <p v-if="errorMessage" class="text-sm text-red-600">{{ errorMessage }}</p>

            <div class="flex items-center justify-between text-sm">
              <label class="flex cursor-pointer items-center gap-2">
                <input
                  type="checkbox"
                  v-model="toggle"
                  true-value="yes"
                  false-value="no"
                  class="h-4 w-4 rounded border-gray-300 text-black focus:ring-black"
                />
                <span class="text-gray-700">Remember me</span>
              </label>

              <RouterLink
                to="/forgot-password"
                class="text-gray-600 transition-colors hover:text-black"
              >
                Forgot password?
              </RouterLink>
            </div>

            <button
              type="submit"
              class="w-full cursor-pointer rounded-lg bg-black py-3 font-semibold text-white transition duration-200 hover:bg-gray-800"
            >
              Login
            </button>
          </form>

          <div class="mt-8 text-center">
            <p class="text-gray-600">
              Don't have an account?
              <RouterLink to="/register" class="font-semibold text-black hover:underline"
                >Create Account</RouterLink
              >
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
