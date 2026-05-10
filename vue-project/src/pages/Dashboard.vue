<script setup>
import StatCard from '@/components/StatCard.vue'
import WorkoutItem from '@/components/WorkoutItem.vue'

const recentWorkouts = [
  { name: 'Upper Body', duration: '45 min', calories: 320, time: 'Today' },
  { name: 'HIIT Cardio', duration: '30 min', calories: 280, time: 'Yesterday' },
  { name: 'Leg Day', duration: '50 min', calories: 400, time: '2 days ago' },
  { name: 'Core Training', duration: '25 min', calories: 180, time: '3 days ago' },
]
</script>

<template>
  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6 lg:grid-cols-4">
    <StatCard title="Total Workouts" value="127" subtitle="+12% from last week" />
    <StatCard title="Calories Burned" value="45,230" subtitle="+8% from last month" />
    <StatCard title="Active Days This Month" value="24" />
    <StatCard title="Avg Duration" value="52m" subtitle="Per workout" />

    <div class="lg:col-span-2">
      <div class="rounded-md border border-gray-200 bg-white p-4 md:p-6">
        <h2 class="text-sm font-medium text-gray-600">Recent Workouts</h2>
        <div v-for="workout in recentWorkouts" :key="workout.name">
          <WorkoutItem :name="workout.name" :duration="workout.duration" :time="workout.time" />
        </div>
      </div>
    </div>
  </div>
</template>
