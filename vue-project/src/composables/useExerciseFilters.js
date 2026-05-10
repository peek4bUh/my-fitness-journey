import { computed, ref } from 'vue'

export function useExerciseFilters(initialExercises) {
  const searchExercise = ref('')
  const selectedType = ref('All')
  const selectedDifficultyGroups = ref([])
  const selectedMuscleGroups = ref([])

  const typeOptions = [
    { label: 'All', value: 'All' },
    { label: 'Compound', value: 'Compound' },
    { label: 'Isolation', value: 'Isolation' },
  ]

  const filteredExercises = computed(() => {
    if (!initialExercises.value) return []

    return initialExercises.value.filter((exercise) => {
      // 1. Search Filter
      const searchTerm = searchExercise.value.toLowerCase()
      const matchesSearch =
        !searchExercise.value ||
        (exercise.name || '').toLowerCase().includes(searchTerm) ||
        (exercise.description || '').toLowerCase().includes(searchTerm)

      // 2. Mechanic Filter
      const matchesType =
        selectedType.value === typeOptions[0].value || exercise.mechanic === selectedType.value

      // 3. Level Filter
      const matchesDifficulty =
        selectedDifficultyGroups.value.length === 0 ||
        selectedDifficultyGroups.value
          .map((item) => item.toLowerCase())
          .includes(exercise.level.toLowerCase())

      // 4. Muscle Group Filter

      const matchesMuscle =
        selectedMuscleGroups.value.length === 0 ||
        selectedMuscleGroups.value
          .map((item) => item.toLowerCase())
          .includes(exercise.muscleGroup.toLowerCase())

      return matchesSearch && matchesType && matchesDifficulty && matchesMuscle
    })
  })

  const clearFilters = () => {
    searchExercise.value = ''
    selectedType.value = 'All'
    selectedDifficultyGroups.value = []
    selectedMuscleGroups.value = []
  }

  return {
    searchExercise,
    selectedType,
    selectedDifficultyGroups,
    selectedMuscleGroups,
    filteredExercises,
    clearFilters,
    typeOptions,
  }
}
