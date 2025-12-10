<script setup>
import SiteLogo from '../components/SiteLogo.vue'
</script>

<template>
  <div class="flex h-screen">
    <!-- Left Column -->
    <div class="hidden lg:block relative basis-2/4">
      <img
        class="absolute z-0 h-full object-cover"
        src="../assets/images/bb-romanian-deadlift.jpg"
        alt="Barbell Romanian Deadlift"
      />
      <div
        class="absolute z-10 flex flex-col justify-center items-start h-full w-full pl-10 inset-0 bg-black/50"
      >
        <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 drop-shadow-lg">
          Push Your Limits.
        </h2>
        <p class="text-lg text-gray-200 max-w-md">
          Every small step adds up. Stay consistent, show up, and watch your journey transform.
        </p>
      </div>
    </div>

    <!-- Right Column -->
    <div class="flex flex-col justify-between grow basis-1/2 p-6">
      <SiteLogo />

      <div class="flex items-center justify-center flex-1">
        <div class="w-full max-w-md">
          <div class="text-center mt-0 mb-8">
            <h2 class="text-3xl lg:text-4xl font-bold text-black mb-2">Welcome Back</h2>
            <p class="lg:text-lg text-gray-600">Sign in to continue your fitness journey</p>
          </div>

          <form method="post" sub class="flex flex-col gap-6">
            <div>
              <label
                for="username"
                class="block text-sm lg:text-base font-semibold text-gray-600 mb-1"
              >
                Username
              </label>
              <input
                type="text"
                name="username"
                required
                class="text-sm lg:text-base w-full py-1 border-b bg-transparent border-gray-400 focus:outline-none focus:border-black transition-colors"
              />
            </div>

            <div>
              <label
                for="password"
                class="block text-sm lg:text-base font-semibold text-gray-600 mb-1"
              >
                Password
              </label>
              <input
                type="password"
                name="password"
                required
                class="text-sm lg:text-base w-full py-1 border-b bg-transparent border-gray-400 focus:outline-none focus:border-black transition-colors"
              />
            </div>

            <div class="flex items-center justify-between text-sm">
              <label class="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  name="remember"
                  value="1"
                  class="w-4 h-4 rounded border-gray-300 text-black focus:ring-black"
                />
                <span class="text-gray-700">Remember me</span>
              </label>

              <RouterLink
                to="/forgot-password"
                class="text-gray-600 hover:text-black transition-colors"
              >
                Forgot password?
              </RouterLink>
            </div>

            <button
              type="submit"
              class="w-full py-3 bg-black text-white font-semibold rounded-lg hover:bg-gray-800 transition duration-200 cursor-pointer"
            >
              Login
            </button>
          </form>

          <div class="mt-8 text-center">
            <p class="text-gray-600">
              Don't have an account?
              <RouterLink to="/register" class="text-black font-semibold hover:underline"
                >Create Account</RouterLink
              >
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
