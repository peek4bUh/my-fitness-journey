import { onMounted, onUnmounted, ref } from 'vue'

// Shared state across all composable instances
let filterSidebarState = null

function initializeFilterSidebarState() {
  if (filterSidebarState) return filterSidebarState

  const isOpen = ref(false)
  const isMobile = ref(false)
  const isDesktop = ref(false)

  const handleResize = () => {
    isMobile.value = window.innerWidth < 1024
    isDesktop.value = window.innerWidth >= 1280
  }

  const toggleFilterSidebar = () => {
    isOpen.value = !isOpen.value
  }

  filterSidebarState = {
    isOpen,
    isMobile,
    isDesktop,
    toggleFilterSidebar,
    handleResize,
  }

  return filterSidebarState
}

export function useFilterSidebar() {
  const state = initializeFilterSidebarState()

  onMounted(() => {
    state.handleResize()
    window.addEventListener('resize', state.handleResize)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', state.handleResize)
  })

  return {
    isOpen: state.isOpen,
    isMobile: state.isMobile,
    isDesktop: state.isDesktop,
    toggleFilterSidebar: state.toggleFilterSidebar,
  }
}
