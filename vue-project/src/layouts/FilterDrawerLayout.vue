<script setup>
import { useFilterSidebar } from '@/composables/useFilterSidebar'
import Button from 'primevue/button'
import IconField from 'primevue/iconfield'
import InputIcon from 'primevue/inputicon'
import InputText from 'primevue/inputtext'
import MultiSelect from 'primevue/multiselect'
import SelectButton from 'primevue/selectbutton'
import { computed } from 'vue'

const { isOpen, toggleFilterSidebar, isMobile, isDesktop } = useFilterSidebar()

const props = defineProps({
  searchQuery: { type: String, default: '' },
  selectedType: { type: String, default: 'all' },
  selectedDifficultyGroups: { type: Array, default: () => [] },
  selectedMuscleGroups: { type: Array, default: () => [] },
  typeOptions: { type: Array, default: () => [] },
  difficultyGroupOptions: { type: Array, default: () => [] },
  muscleGroupOptions: { type: Array, default: () => [] },
  exerciseCount: { type: Number, default: 0 },
  totalExerciseCount: { type: Number, default: 0 },
})

const canClearFilters = computed(
  () =>
    props.searchQuery !== '' ||
    props.selectedType !== 'all' ||
    props.selectedDifficultyGroups.length > 0 ||
    props.selectedMuscleGroups.length > 0,
)

const sidebarClasses = computed(() => ({
  // Mobile (<1024px)
  'translate-y-0': isOpen.value && isMobile.value,
  'translate-y-full': !isOpen.value && isMobile.value,

  // LG (1024px - 1280px)
  'lg:translate-x-full': !isOpen.value && !isMobile.value && !isDesktop.value,
  'lg:translate-x-0': (isOpen.value && !isMobile.value) || isDesktop.value,

  // XL (>1280px)
  'xl:translate-x-0 xl:bg-inherit': isDesktop.value,
}))
</script>

<template>
  <aside
    class="fixed bottom-0 right-0 z-50 flex h-screen w-full flex-col bg-white text-gray-900 transition-all duration-300 ease-in-out lg:top-0 lg:left-auto lg:w-80 xl:static xl:h-auto xl:w-72 xl:shrink-0 border-l border-gray-200"
    :class="sidebarClasses"
  >
    <div class="flex items-center justify-between border-b border-gray-200 px-6 py-4 xl:hidden">
      <h2 class="text-lg font-semibold">Filters</h2>
      <Button @click="toggleFilterSidebar" icon="pi pi-times" severity="secondary" text rounded />
    </div>

    <div class="hidden px-6 pt-6 pb-2 xl:block">
      <h2 class="text-xl font-bold">Filters</h2>
    </div>

    <div class="flex-1 space-y-8 overflow-y-auto px-6 py-4">
      <!-- Search Bar -->
      <IconField v-if="isDesktop">
        <InputIcon class="pi pi-search" />
        <InputText
          :modelValue="searchQuery"
          @update:modelValue="$emit('update:searchQuery', $event)"
          placeholder="Exercise..."
          class="w-full"
        />
      </IconField>

      <!-- Exercise Type -->
      <div>
        <label class="mb-3 block text-sm font-medium text-gray-700">Exercise Type</label>
        <SelectButton
          :modelValue="selectedType"
          :options="typeOptions"
          optionLabel="label"
          optionValue="value"
          class="w-full"
          @update:modelValue="$emit('update:selectedType', $event)"
        />
      </div>

      <!-- Difficulty -->
      <div>
        <label class="mb-3 block text-sm font-medium text-gray-700">Difficulty</label>
        <MultiSelect
          :modelValue="selectedDifficultyGroups"
          :options="difficultyGroupOptions"
          optionLabel="name"
          optionValue="name"
          placeholder="Select difficulties"
          class="w-full"
          display="chip"
          @update:modelValue="$emit('update:selectedDifficultyGroups', $event)"
        />
      </div>

      <!-- Target Muscles -->
      <div>
        <label class="mb-3 block text-sm font-medium text-gray-700">Target Muscles</label>
        <MultiSelect
          :modelValue="selectedMuscleGroups"
          :options="muscleGroupOptions"
          optionLabel="name"
          optionValue="id"
          placeholder="Select muscles"
          class="w-full"
          display="chip"
          filter
          @update:modelValue="$emit('update:selectedMuscleGroups', $event)"
        />
      </div>

      <!-- Total Results -->
      <div class="text-xs font-bold text-gray-400 uppercase tracking-widest">
        {{ exerciseCount }} results from {{ totalExerciseCount }}
      </div>
    </div>

    <!-- Reset Button -->
    <div class="p-6 xl:bg-transparent">
      <Button
        :disabled="!canClearFilters"
        class="w-full"
        severity="secondary"
        label="Reset Filters"
        @click="$emit('clear-filters')"
      />
    </div>
  </aside>
</template>
