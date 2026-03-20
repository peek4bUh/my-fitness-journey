<script setup>
import SiteLogo from '../components/SiteLogo.vue'
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
      <SiteLogo />

      <div class="flex flex-1 items-center justify-center">
        <div class="w-full max-w-md">
          <div class="mt-0 mb-8 text-center">
            <h2 class="mb-2 text-3xl font-bold text-black lg:text-4xl">Create Account</h2>
            <p class="text-gray-600 lg:text-lg">Start your fitness journey today</p>
          </div>

          <form method="post" class="flex flex-col gap-6">
            <div>
              <label
                for="username"
                class="mb-1 block text-sm font-semibold text-gray-600 lg:text-base"
              >
                Username
              </label>
              <input
                type="text"
                name="username"
                required
                class="w-full border-b border-gray-400 bg-transparent py-1 text-sm transition-colors focus:border-black focus:outline-none lg:text-base"
              />
            </div>

            <div>
              <label
                for="email"
                class="mb-1 block text-sm font-semibold text-gray-600 lg:text-base"
              >
                Email
              </label>
              <input
                type="text"
                name="email"
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
                name="password"
                required
                class="w-full border-b border-gray-400 bg-transparent py-1 text-sm transition-colors focus:border-black focus:outline-none lg:text-base"
              />
            </div>

            <div>
              <label
                for="confirm-password"
                class="mb-1 block text-sm font-semibold text-gray-600 lg:text-base"
              >
                Confirm Password
              </label>
              <input
                type="password"
                name="confirm-password"
                required
                class="w-full border-b border-gray-400 bg-transparent py-1 text-sm transition-colors focus:border-black focus:outline-none lg:text-base"
              />
            </div>

            <button
              type="submit"
              class="w-full rounded-lg bg-black py-3 font-semibold text-white transition duration-200 hover:bg-gray-800"
            >
              Create Account
            </button>
          </form>

          <div class="mt-8 text-center">
            <p class="text-gray-600">
              Already registered?
              <a href="/login" class="font-semibold text-black hover:underline">Login</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
