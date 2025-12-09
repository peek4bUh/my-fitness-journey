<script setup>
import Badge from '../components/Badge.vue'
import ReasonItem from '../components/ReasonItem.vue'

import DumbellIcon from '../components/icons/IconDumbell.vue'
</script>

<template>
  <header id="header">
    <div class="w-full fixed top-0 z-50 transition-[background-color] duration-300 ease-in-out">
      <div class="container mx-auto px-6 py-4 flex items-center justify-between">
        <a href="/" class="flex items-center gap-2 lg:gap-3 w-fit">
          <span class="w-7 h-7 lg:w-9 lg:h-9 bg-black rounded-lg flex items-center justify-center">
            <DumbellIcon class="w-4 h-4 lg:w-5 lg:h-5 text-white" />
          </span>
          <p class="lg:text-xl font-semibold">MyFitnessJourney</p>
        </a>

        <!-- Navigation -->
        <nav class="hidden md:flex items-center gap-6">
          <a
            href="#features"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors"
            >features</a
          >
          <a
            href="#reasons"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors"
            >Reasons</a
          >
          <a
            href="#opensource"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors"
            >Open Source</a
          >

          <div class="flex items-center gap-2 font-semibold">
            <RouterLink
              to="/login"
              class="px-6 py-2.5 text-sm border border-gray-800 hover:bg-gray-200 rounded-md text-gray-700 hover:text-black transition-colors"
              >Log In</RouterLink
            >
            <RouterLink
              to="/register"
              class="px-6 py-2.5 text-sm border border-black bg-black text-white rounded-md hover:bg-gray-800 transition-all duration-200"
              >Sign Up</RouterLink
            >
          </div>
        </nav>

        <!-- Hamburger -->
        <button class="md:hidden p-2 text-gray-600 hover:text-black transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Added mobile navigation menu that toggles with smooth transitions -->
      <nav class="md:hidden border-t border-gray-100 bg-white">
        <div class="container mx-auto px-6 py-4 flex flex-col gap-3">
          <a
            href="#features"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors py-2"
            >Features</a
          >
          <a
            href="#reasons"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors py-2"
            >Reasons</a
          >
          <a
            href="#opensource"
            class="text-sm font-medium text-gray-600 hover:text-black transition-colors py-2"
            >Open Source</a
          >

          <div class="flex flex-col gap-3 pt-3 border-t border-gray-100">
            <a
              href="#"
              class="px-5 py-2.5 text-sm font-medium text-center text-gray-700 hover:text-black hover:bg-gray-50 rounded-md transition-colors"
            >
              Log In
            </a>
            <a
              href="#"
              class="px-6 py-2.5 text-sm font-medium text-center bg-black text-white rounded-md hover:bg-gray-800 transition-all duration-200"
            >
              Register
            </a>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <div id="content">
    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center px-4 py-20">
      <div class="max-w-3xl mx-auto text-center">
        <h1 class="text-5xl md:text-7xl font-bold mb-6 leading-tight tracking-tight text-black">
          The Open Source
          <span class="text-gray-500">Fitness Tool</span>
          Tracker
        </h1>

        <p class="text-xl md:text-2xl text-gray-600 mb-10 mx-auto leading-relaxed">
          A completely free and open source fitness tracking app. Document your fitness journey,
          visualize progress, and achieve your goals without any cost or limitations.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
          <RouterLink
            to="/login"
            class="inline-block px-10 py-4 border-2 border-black bg-black text-white text-lg font-medium rounded-md hover:bg-gray-800 transition-all duration-200"
          >
            Join For Free
          </RouterLink>
          <a
            href="https://github.com/peek4bUh/my-fitness-journey"
            class="inline-block px-10 py-4 border-2 border-black text-black text-lg font-medium rounded-md hover:bg-gray-200 transition-all duration-200"
          >
            View on GitHub
          </a>
        </div>

        <div class="flex flex-wrap gap-3 justify-center text-sm text-gray-500">
          <Badge msg="100% Free" />
          <Badge msg="Open Source" />
          <Badge msg="No Limitations" />
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Everything You Need to Dominate Your Workouts
          </h2>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            Powerful features designed for serious fitness enthusiasts who want to track, analyze,
            and improve their performance.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Workout Tracking</h3>
              <p class="text-gray-600 leading-relaxed">
                Log every rep, set, and weight with our intuitive interface. Never lose track of
                your progress again.
              </p>
            </div>
          </div>

          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Progress Analytics</h3>
              <p class="text-gray-600 leading-relaxed">
                Visualize your strength gains with detailed charts and progress tracking over time.
              </p>
            </div>
          </div>

          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Goal Setting</h3>
              <p class="text-gray-600 leading-relaxed">
                Set weekly and monthly fitness goals and track your consistency with smart
                reminders.
              </p>
            </div>
          </div>

          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Workout Timer</h3>
              <p class="text-gray-600 leading-relaxed">
                Built-in rest timers and workout duration tracking to optimize your gym sessions.
              </p>
            </div>
          </div>

          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Body Metrics</h3>
              <p class="text-gray-600 leading-relaxed">
                Track weight, body fat percentage, and muscle mass changes over time.
              </p>
            </div>
          </div>

          <div
            class="rounded-lg border-2 border-gray-100 hover:border-gray-300 transition-all duration-300 hover:shadow-lg group bg-white"
          >
            <div class="p-6">
              <div
                class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center mb-4 group-hover:bg-gray-300 transition-colors"
              ></div>
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Mobile First</h3>
              <p class="text-gray-600 leading-relaxed">
                Designed for mobile use in the gym with offline support and quick logging.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Reasons Section -->
    <section id="reasons" class="py-20">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
              Why Choose MyFitnessJourney?
            </h2>
            <p class="text-lg text-gray-600 mb-8">
              Join thousands of fitness enthusiasts who have transformed their workouts with our
              comprehensive tracking platform.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <ReasonItem msg="Track unlimited workouts and exercises" />
              <ReasonItem msg="Visual progress charts and analytics" />
              <ReasonItem msg="Workout templates and routines" />
              <ReasonItem msg="Rest timer and workout duration tracking" />
              <ReasonItem msg="Body metrics and measurements" />
              <ReasonItem msg="Goal setting and achievement tracking" />
              <ReasonItem msg="Offline mode for gym use" />
              <ReasonItem msg="Export data and progress reports" />
            </div>
          </div>
          <div class="relative">
            <img
              class="w-full md:w-4/5 z-50"
              src="../assets/images/reasons.png"
              alt="Reasons Image"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Highlights Section -->
    <section id="highlights" class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Built by Fitness Enthusiasts, For Fitness Enthusiasts
          </h2>
          <p class="text-xl text-gray-600">
            MyFitnessJourney is completely open source and free to use
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div class="border-2 border-gray-200 text-center rounded-lg bg-white">
            <div class="p-8">
              <div
                class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6"
              ></div>
              <h3 class="text-xl font-bold text-gray-900 mb-4">100% Free</h3>
              <p class="text-gray-600">
                No subscriptions, no hidden fees, no premium features. Everything is free forever.
              </p>
            </div>
          </div>

          <div class="border-2 border-gray-200 text-center rounded-lg bg-white">
            <div class="p-8">
              <div
                class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6"
              ></div>
              <h3 class="text-xl font-bold text-gray-900 mb-4">Open Source</h3>
              <p class="text-gray-600">
                Full source code available on GitHub. Contribute, customize, or learn from the
                codebase.
              </p>
            </div>
          </div>

          <div class="border-2 border-gray-200 text-center rounded-lg bg-white">
            <div class="p-8">
              <div
                class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6"
              ></div>
              <h3 class="text-xl font-bold text-gray-900 mb-4">Privacy First</h3>
              <p class="text-gray-600">
                Your data stays on your device. No tracking, no ads, no data collection.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <footer id="footer" class="py-10 text-gray-200 bg-gray-900">
    <div class="container mx-auto px-8 flex flex-col sm:flex-row sm:justify-between gap-6 sm:gap-0">
      <div class="order-2">
        <div class="flex items-center mb-4">
          <ul class="flex items-center text-sm">
            <li class="relative after:content-['·'] after:mx-2">
              <a
                href="http://www.aandradeb.com"
                target="_blank"
                class="hover:text-sky-500 transition-colors duration-200"
                >Portfolio</a
              >
            </li>
            <li class="relative after:content-['·'] after:mx-2">
              <a
                href="https://www.linkedin.com/in/angel-andrade-berganti%C3%B1os-3791a7176"
                target="_blank"
                class="hover:text-sky-500 transition-colors duration-200"
                >LinkedIn</a
              >
            </li>
            <li class="relative after:content-['·'] after:mx-2">
              <a
                href="https://github.com/peek4bUh/my-fitness-journey"
                target="_blank"
                class="hover:text-sky-500 transition-colors duration-200"
                >GitHub</a
              >
            </li>
            <li class="relative">
              <a
                href="https://github.com/peek4bUh/my-fitness-journey/blob/main/LICENSE"
                target="_blank"
                class="hover:text-sky-500 transition-colors duration-200"
                >License</a
              >
            </li>
          </ul>
        </div>
        <p class="text-gray-400 text-sm">© 2025 · MyFitnessJourney · All rights reserved</p>
      </div>
      <div class="order-1 sm:order-3 sm:text-right">
        <p class="text-sm text-gray-400 mb-3">
          Created by
          <a
            href="https://www.linkedin.com/in/angel-andrade-berganti%C3%B1os-3791a7176/"
            target="_blank"
            rel="noopener noreferrer"
            class="underline font-bold text-gray-200 hover:text-sky-500 transition-colors duration-200"
            >Angel Andrade</a
          >
        </p>
        <p class="text-sm text-gray-400">
          Developed with
          <a
            href="https://flask.palletsprojects.com/en/stable/"
            target="_blank"
            class="underline font-bold text-gray-200 hover:text-sky-500 transition-colors duration-200"
            >Flask</a
          >
          +
          <a
            href="https://tailwindcss.com/"
            target="_blank"
            class="underline font-bold text-gray-200 hover:text-sky-500 transition-colors duration-200"
            >Tailwind CSS</a
          >
        </p>
      </div>
    </div>
  </footer>
</template>
