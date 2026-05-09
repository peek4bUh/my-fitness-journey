import { computed, ref } from 'vue'

export function useExerciseFilters(initialExercises) {
  const searchExercise = ref('')
  const selectedType = ref('all')
  const selectedDifficultyGroups = ref([])
  const selectedMuscleGroups = ref([])

  const typeOptions = [
    { label: 'All', value: 'all' },
    { label: 'Compound', value: 'compound' },
    { label: 'Isolation', value: 'isolation' },
  ]

  const filteredExercises = computed(() => {
    if (!initialExercises.value) return []

    return initialExercises.value.filter((exercise) => {
      // 1. Filtro de búsqueda
      const searchTerm = searchExercise.value.toLowerCase()
      const matchesSearch =
        !searchExercise.value ||
        (exercise.name || '').toLowerCase().includes(searchTerm) ||
        (exercise.description || '').toLowerCase().includes(searchTerm)

      // 2. Filtro de tipo
      const matchesType =
        selectedType.value === 'all' ||
        (exercise.type || '').toLowerCase() === selectedType.value.toLowerCase()

      // 3. Filtro de dificultad (ajustado a tu lógica original)
      const matchesDifficulty =
        selectedDifficultyGroups.value.length === 0 ||
        selectedDifficultyGroups.value
          .map((item) => (typeof item === 'object' ? item.name : item)?.toLowerCase())
          .includes((exercise.difficulty || '').toLowerCase())

      // 4. Filtro de músculos
      const matchesMuscle =
        selectedMuscleGroups.value.length === 0 ||
        selectedMuscleGroups.value
          .map((item) => (item.value || item.label || item).toLowerCase())
          .includes((exercise.targetMuscle || '').toLowerCase())

      // Solo si cumple todas las condiciones
      return matchesSearch && matchesType && matchesDifficulty && matchesMuscle
    })
  })

  const clearFilters = () => {
    searchExercise.value = ''
    selectedType.value = 'all'
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
