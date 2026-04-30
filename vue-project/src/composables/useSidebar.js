import { onMounted, onUnmounted, ref } from 'vue'

// Shared state across all composable instances
let sidebarState = null

function initializeSidebarState() {
  if (sidebarState) return sidebarState

  const isMobileOpen = ref(false)
  const isMobile = ref(false)
  const activeItem = ref(null)

  const handleResize = () => {
    const mobile = window.innerWidth < 1024
    isMobile.value = mobile
  }

  const toggleSidebar = () => {
    isMobileOpen.value = !isMobileOpen.value
  }

  const setActiveItem = (item) => {
    activeItem.value = item
  }

  sidebarState = {
    isMobileOpen,
    isMobile,
    activeItem,
    toggleSidebar,
    setActiveItem,
    handleResize,
  }

  return sidebarState
}

export function useSidebar() {
  const state = initializeSidebarState()

  onMounted(() => {
    state.handleResize()
    window.addEventListener('resize', state.handleResize)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', state.handleResize)
  })

  return {
    isMobileOpen: state.isMobileOpen,
    isMobile: state.isMobile,
    activeItem: state.activeItem,
    toggleSidebar: state.toggleSidebar,
    setActiveItem: state.setActiveItem,
  }
}
