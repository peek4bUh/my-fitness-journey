<script setup>
import ExerciseCard from '@/components/ExerciseCard.vue'
import AppLayout from '@/layout/AppLayout.vue'
import Button from 'primevue/button'
import MultiSelect from 'primevue/multiselect'
import SelectButton from 'primevue/selectbutton'
import { computed, onMounted, ref } from 'vue'

import difficultyGroupData from '@/mocks/difficulties.json'
import exercisesData from '@/mocks/exercises.json'
import muscleGroupData from '@/mocks/muscleGroup.json'

const loading = ref(true)
const error = ref(null)

// --- Filter states ---
const selectedType = ref('all')
const selectedDifficultyGroups = ref([])
const selectedMuscleGroups = ref([])

// --- Options ---
const typeOptions = [
  { label: 'All', value: 'all' },
  { label: 'Compound', value: 'compound' },
  { label: 'Isolation', value: 'isolation' },
]

const difficultyGroupOptions = difficultyGroupData.data
const muscleGroupOptions = muscleGroupData.data
const exercises = ref(exercisesData.exercises)

function matchesTypeFilter(exercise) {
  if (selectedType.value === 'all') return true
  const exerciseType = (exercise.type || '').toLowerCase()
  return exerciseType === selectedType.value.toLowerCase()
}

function matchesDifficultyFilter(exercise) {
  if (selectedDifficultyGroups.value.length === 0) return true

  const selectedDifficultyValues = selectedDifficultyGroups.value.map((item) =>
    typeof item === 'object' ? item.value || item.label : item,
  )
  const exerciseDifficulty = (exercise.difficulty || '').toLowerCase()

  return selectedDifficultyValues.some((selected) => exerciseDifficulty === selected.toLowerCase())
}

function matchesMuscleFilter(exercise) {
  if (selectedMuscleGroups.value.length === 0) return true

  const selectedMuscleValues = selectedMuscleGroups.value.map((item) =>
    typeof item === 'object' ? item.value || item.label : item,
  )
  const exerciseMuscle = (exercise.targetMuscle || '').toLowerCase()

  return selectedMuscleValues.some((selected) => exerciseMuscle === selected.toLowerCase())
}

const filteredExercises = computed(() => {
  return exercises.value.filter(
    (exercise) =>
      matchesTypeFilter(exercise) &&
      matchesDifficultyFilter(exercise) &&
      matchesMuscleFilter(exercise),
  )
})

const clearFilters = () => {
  selectedType.value = 'all'
  selectedDifficultyGroups.value = []
  selectedMuscleGroups.value = []
}

onMounted(async () => {
  try {
    // Debug: Log the data structure (optional)
    console.log('First exercise:', exercises.value[0])
    console.log('Difficulty group options:', difficultyGroupOptions)
    console.log('Muscle group options:', muscleGroupOptions)
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load exercises'
    console.error(error.value)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <AppLayout>
    <!-- Loading State -->
    <div v-if="loading" class="space-y-6">
      <div class="mb-6">
        <div class="mb-2 h-7 w-32 animate-pulse rounded bg-gray-200"></div>
        <div class="h-4 w-64 animate-pulse rounded bg-gray-200"></div>
      </div>
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="i in 6" :key="i" class="rounded-xl border border-gray-200 bg-white p-5">
          <div class="mb-3 flex items-start gap-3">
            <div class="h-12 w-12 animate-pulse rounded-lg bg-gray-200"></div>
            <div class="flex-1">
              <div class="mb-2 h-5 w-24 animate-pulse rounded bg-gray-200"></div>
              <div class="h-3 w-16 animate-pulse rounded bg-gray-200"></div>
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5">
            <div class="h-5 w-16 animate-pulse rounded-full bg-gray-200"></div>
            <div class="h-5 w-20 animate-pulse rounded-full bg-gray-200"></div>
          </div>
          <div class="mt-2 border-t pt-3">
            <div class="flex items-center justify-between">
              <div class="h-3 w-20 animate-pulse rounded bg-gray-200"></div>
              <div class="h-3 w-12 animate-pulse rounded bg-gray-200"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="rounded-lg border border-red-200 bg-red-50 p-6 text-center">
      <div class="mb-2 text-red-600">
        <svg class="mx-auto h-12 w-12" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
        </svg>
      </div>
      <p class="font-medium">{{ error }}</p>
      <button
        @click="() => window.location.reload()"
        class="mt-4 rounded-lg bg-red-600 px-4 py-2 text-white transition-colors hover:bg-red-700"
      >
        Try Again
      </button>
    </div>

    <!-- Exercises Content -->
    <div v-else>
      <!-- Header -->
      <div class="mb-6 hidden lg:block">
        <h1 class="text-xl font-semibold tracking-tight md:text-2xl">Exercises</h1>
        <p class="md:text-normal mt-0.5 text-sm text-gray-600">Browse the exercise library</p>
      </div>

      <!-- Filters Section -->
      <div class="mb-6 space-y-4">
        <div class="flex flex-wrap gap-4">
          <!-- Exercise Type Filter - SelectButton -->
          <div class="min-w-[280px]">
            <label class="mb-2 block text-sm font-medium text-gray-700">Exercise Type</label>
            <SelectButton
              v-model="selectedType"
              :options="typeOptions"
              optionLabel="label"
              optionValue="value"
              class="w-full"
            />
          </div>

          <!-- Difficulty Group Filter -->
          <div class="min-w-[200px] flex-1">
            <label class="mb-2 block text-sm font-medium text-gray-700">Exercise Difficulty</label>
            <MultiSelect
              v-model="selectedDifficultyGroups"
              :options="difficultyGroupOptions"
              optionLabel="label"
              optionValue="value"
              placeholder="Select difficulty groups"
              class="w-full"
              :maxSelectedLabels="3"
              display="chip"
              filter
              :filterFields="['label']"
            />
          </div>

          <!-- Muscle Group Filter -->
          <div class="min-w-[200px] flex-1">
            <label class="mb-2 block text-sm font-medium text-gray-700">Muscles Worked</label>
            <MultiSelect
              v-model="selectedMuscleGroups"
              :options="muscleGroupOptions"
              optionLabel="label"
              optionValue="value"
              placeholder="Select muscle groups"
              class="w-full"
              :maxSelectedLabels="3"
              display="chip"
              filter
              :filterFields="['label']"
            />
          </div>

          <!-- Clear Filters Button -->
          <div class="flex items-end">
            <Button
              @click="clearFilters"
              :disabled="
                selectedType === 'all' &&
                selectedDifficultyGroups.length == 0 &&
                selectedMuscleGroups.length == 0
              "
            >
              Clear Filters
            </Button>
          </div>
        </div>

        <!-- Results Count -->
        <div class="text-sm text-gray-600">
          Showing {{ filteredExercises.length }} of {{ exercises.length }} exercises
        </div>
      </div>

      <!-- Exercises Grid -->
      <div
        v-if="filteredExercises.length > 0"
        class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3 auto-rows-fr"
      >
        <ExerciseCard
          v-for="exercise in filteredExercises"
          :key="exercise.id"
          :title="exercise.name"
          :overview="exercise.description"
          :type="exercise.type"
          :level="exercise.difficulty"
          :targetMuscle="exercise.targetMuscle"
        />
      </div>

      <!-- No Results State -->
      <div
        v-else
        class="flex flex-col items-center justify-center rounded-xl border border-dashed border-gray-300 bg-gray-50 py-16"
      >
        <div class="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-gray-200">
          <i class="pi pi-search before:text-3xl before:text-gray-500"></i>
        </div>
        <h3 class="mb-2 text-lg font-medium text-gray-900">No exercises found</h3>
        <p class="text-gray-500">Try adjusting your filters</p>
      </div>
    </div>
  </AppLayout>
</template>
