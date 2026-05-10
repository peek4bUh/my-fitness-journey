<script setup>
import ExerciseCard from '@/components/ExerciseCard.vue'
import { useFilterSidebar } from '@/composables/useFilterSidebar.js'
import BaseLayout from '@/layouts/BaseLayout.vue'
import FilterDrawerLayout from '@/layouts/FilterDrawerLayout.vue'
import Button from 'primevue/button'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import InputText from 'primevue/inputtext'
import { onMounted, ref } from 'vue'

import { useExerciseFilters } from '@/composables/useExerciseFilters'
import { ExerciseService } from '@/services/exerciseService'
import { MuscleService } from '@/services/muscleService'

const muscleService = new MuscleService()
const exerciseService = new ExerciseService()

const { toggleFilterSidebar } = useFilterSidebar()
const exercises = ref([])
const loading = ref(true)
const error = ref(null)
const difficultyGroupOptions = ref([])
const muscleGroupOptions = ref([])
const {
  searchExercise,
  selectedType,
  selectedDifficultyGroups,
  selectedMuscleGroups,
  filteredExercises,
  clearFilters,
  typeOptions,
} = useExerciseFilters(exercises)

onMounted(async () => {
  try {
    exercises.value = await exerciseService.getExercises()
    difficultyGroupOptions.value = await exerciseService.getExerciseLevels()
    muscleGroupOptions.value = await muscleService.getMuscleGroups()
  } catch (err) {
    console.error('Error loading data:', err)
    error.value = 'Failed to load data.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <BaseLayout>
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
            <RouterLink
              v-for="exercise in filteredExercises"
              :key="exercise.id"
              :to="{ name: 'exercise-detail', params: { id: exercise.id } }"
            >
              <ExerciseCard
                :title="exercise.name"
                :overview="exercise.description"
                :mechanic="exercise.mechanic"
                :level="exercise.level"
                :targetMuscle="exercise.targetMuscle"
              />
            </RouterLink>
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
        <FilterDrawerLayout
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
  </BaseLayout>
</template>
