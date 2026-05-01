<script setup>
import ExerciseCard from '@/components/ExerciseCard.vue'
import { useFilterSidebar } from '@/composables/useFilterSidebar'
import AppLayout from '@/layout/AppLayout.vue'
import FilterSidebar from '@/layout/components/FilterSidebar.vue'
import Button from 'primevue/button'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import InputText from 'primevue/inputtext'
import { computed, onMounted, ref } from 'vue'

import difficultyGroupData from '@/mocks/difficulties.json'
import exercisesData from '@/mocks/exercises.json'
import muscleGroupData from '@/mocks/muscleGroup.json'

const { toggleFilterSidebar } = useFilterSidebar()
const loading = ref(true)
const error = ref(null)
const searchExercise = ref('')

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

function matchesSearchFilter(exercise) {
  if (!searchExercise.value) return true
  const searchTerm = searchExercise.value.toLowerCase()
  return (
    (exercise.name || '').toLowerCase().includes(searchTerm) ||
    (exercise.description || '').toLowerCase().includes(searchTerm)
  )
}

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
      matchesSearchFilter(exercise) &&
      matchesTypeFilter(exercise) &&
      matchesDifficultyFilter(exercise) &&
      matchesMuscleFilter(exercise),
  )
})

const clearFilters = () => {
  selectedType.value = 'all'
  searchExercise.value = ''
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
      <div class="mb-6 space-y-1">
        <h1 class="text-3xl font-extrabold">Exercises</h1>
        <p class="text-gray-500">Explore our complete library of exercises</p>
      </div>

      <!-- BARRA DE BÚSQUEDA EXTERIOR: Se oculta al llegar a XL (1280px) -->
      <div class="mb-8 flex flex-nowrap gap-3 xl:hidden">
        <IconField class="w-full">
          <InputIcon class="pi pi-search" />
          <InputText class="w-full" v-model="searchExercise" placeholder="Search..." />
        </IconField>
        <Button
          @click="toggleFilterSidebar()"
          class="px-5!"
          label="Filters"
          icon="pi pi-sliders-h"
          severity="secondary"
        />
      </div>

      <!-- CONTENEDOR FLEX: En XL cambia a fila para poner el sidebar a la derecha -->
      <div class="flex flex-col gap-8 xl:flex-row">
        <!-- GRID DE EJERCICIOS (Se expande) -->
        <div class="flex-1">
          <div
            v-if="filteredExercises.length > 0"
            class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 auto-rows-fr"
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

          <!-- Estado Vacío -->
          <div
            v-else
            class="flex flex-col items-center justify-center rounded-2xl border-2 border-dashed border-gray-200 bg-gray-50 py-20"
          >
            <i class="pi pi-search text-4xl text-gray-300 mb-4"></i>
            <h3 class="text-xl font-semibold text-gray-900">No results found</h3>
            <p class="text-gray-500">Try changing the filters or the search query.</p>
          </div>
        </div>

        <!-- SIDEBAR: En XL aparece aquí a la derecha -->
        <FilterSidebar
          v-model:searchQuery="searchExercise"
          :selectedType="selectedType"
          :selectedDifficultyGroups="selectedDifficultyGroups"
          :selectedMuscleGroups="selectedMuscleGroups"
          :typeOptions="typeOptions"
          :difficultyGroupOptions="difficultyGroupOptions"
          :muscleGroupOptions="muscleGroupOptions"
          :exerciseCount="filteredExercises.length"
          :totalExerciseCount="exercises.length"
          @update:selectedType="selectedType = $event"
          @update:selectedDifficultyGroups="selectedDifficultyGroups = $event"
          @update:selectedMuscleGroups="selectedMuscleGroups = $event"
          @clear-filters="clearFilters"
        />
      </div>
    </div>
  </AppLayout>
</template>
