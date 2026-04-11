<script setup>
import AppLayout from '../../layout/AppLayout.vue'
</script>

<template>
  <AppLayout>
    <div class="bg-inherit p-4 md:p-6 lg:p-8">
      <div class="mb-4 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <div class="rounded-lg border border-gray-200 bg-white p-4">
          <div class="mb-4 flex items-center justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-600">Total Workouts</h3>
              <p class="text-2xl font-bold text-gray-900">127</p>
            </div>
          </div>
          <p class="text-sm text-gray-600">+12% from last month</p>
        </div>
        <div class="rounded-lg border border-gray-200 bg-white p-4">
          <div class="mb-4 flex items-center justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-600">Calories Burned</h3>
              <p class="text-2xl font-bold text-gray-900">45,230</p>
            </div>
          </div>
          <p class="text-sm text-gray-600">+8% from last month</p>
        </div>
        <div class="rounded-lg border border-gray-200 bg-white p-4">
          <div class="mb-4 flex items-center justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-600">Active Days This Month</h3>
              <p class="text-2xl font-bold text-gray-900">24</p>
            </div>
          </div>
        </div>
        <div class="rounded-lg border border-gray-200 bg-white p-4">
          <div class="mb-4 flex items-center justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-600">Avg Duration</h3>
              <p class="text-2xl font-bold text-gray-900">52m</p>
            </div>
          </div>
          <p class="text-sm text-gray-600">Per workout</p>
        </div>
      </div>

      <div class="mb-4 grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div class="rounded-lg border border-gray-200 bg-white p-6">
          <h3 class="mb-4 text-lg font-semibold text-gray-900">Recent Activity</h3>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-gray-100">
                  <span class="text-sm font-medium">💪</span>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">Upper Body Strength</p>
                  <p class="text-xs text-gray-500">45 minutes • 320 cal</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">2 hours ago</span>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-gray-100">
                  <span class="text-sm font-medium">🏃</span>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">Cardio Session</p>
                  <p class="text-xs text-gray-500">30 minutes • 280 cal</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">Yesterday</span>
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="flex h-10 w-10 items-center justify-center rounded-lg bg-gray-100">
                  <span class="text-sm font-medium">🧘</span>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">Yoga Flow</p>
                  <p class="text-xs text-gray-500">60 minutes • 180 cal</p>
                </div>
              </div>
              <span class="text-xs text-gray-500">2 days ago</span>
            </div>
          </div>
        </div>
        <div class="rounded-lg border border-gray-200 bg-white p-6">
          <h3 class="mb-4 text-lg font-semibold text-gray-900">Weekly Goal</h3>
          <div class="space-y-4">
            <div>
              <div class="mb-2 flex items-center justify-between">
                <span class="text-sm font-medium text-gray-700">Workouts</span>
                <span class="text-sm font-medium text-gray-900">4/5</span>
              </div>
              <div class="h-2 w-full rounded-full bg-gray-200">
                <div class="h-2 rounded-full bg-black" style="width: 80%"></div>
              </div>
            </div>
            <div>
              <div class="mb-2 flex items-center justify-between">
                <span class="text-sm font-medium text-gray-700">Active Minutes</span>
                <span class="text-sm font-medium text-gray-900">180/200</span>
              </div>
              <div class="h-2 w-full rounded-full bg-gray-200">
                <div class="h-2 rounded-full bg-black" style="width: 90%"></div>
              </div>
            </div>
            <div>
              <div class="mb-2 flex items-center justify-between">
                <span class="text-sm font-medium text-gray-700">Calories</span>
                <span class="text-sm font-medium text-gray-900">1250/1500</span>
              </div>
              <div class="h-2 w-full rounded-full bg-gray-200">
                <div class="h-2 rounded-full bg-black" style="width: 83%"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>
