<script setup>
import Breadcrumb from 'primevue/breadcrumb'
import { ref } from 'vue'

const home = ref({
  icon: 'pi pi-home',
  route: '/dashboard',
})
</script>

<template>
  <Breadcrumb
    :pt="{
      root: { class: 'p-0! bg-inherit! mb-6' },
      itemLink: { class: 'text-sm!' },
    }"
    :home="home"
  >
    <template #item="{ item, props }">
      <RouterLink v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
        <a :href="href" v-bind="props.action" @click="navigate">
          <span :class="[item.icon, 'text-color']" />
          <span class="text-primary font-semibold">{{ item.label }}</span>
        </a>
      </RouterLink>
      <a v-else :href="item.url" :target="item.target" v-bind="props.action">
        {{ item.label }}
      </a>
    </template>
  </Breadcrumb>
</template>
