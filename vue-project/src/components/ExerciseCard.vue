<script setup>
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import { computed, ref } from 'vue'

const props = defineProps({
  title: { type: String, required: true },
  overview: { type: String, required: true },
  mechanic: { type: String, required: true },
  level: { type: String, required: true },
  targetMuscle: { type: String, required: true },
})

const levelKey = ref(props.level.toLowerCase())

const topBorderClass = computed(() => {
  const map = {
    beginner: 'border-t-green-500',
    intermediate: 'border-t-blue-500',
    advanced: 'border-t-amber-500',
    expert: 'border-t-red-500',
  }
  return map[levelKey.value] || ''
})

const rootClasses = computed(
  () =>
    `bg-white rounded-2xl shadow-md border border-gray-200 overflow-hidden transition hover:shadow-lg border-t-4 ${topBorderClass.value}`,
)
</script>

<template>
  <Card
    :pt="{
      root: rootClasses,
      header: 'px-6 pt-6 pb-2',
      body: 'px-6 pb-6',
      content: 'space-y-4',
      title: 'text-xl font-bold text-gray-800',
      subtitle: 'text-sm text-gray-500',
    }"
  >
    <template #title>{{ title }}</template>

    <template #content>
      <p class="text-gray-600 leading-relaxed mb-2">
        {{ overview }}
      </p>
    </template>

    <template #footer>
      <div class="flex items-center gap-2 pt-1">
        <span class="text-xs text-gray-400">Target</span>
        <Tag
          :pt="{
            root: 'bg-gray-100!',
            label: { class: 'text-xs text-gray-700 font-medium' },
          }"
          severity="secondary"
          :value="targetMuscle"
        />
      </div>
    </template>
  </Card>
</template>
