import { ref, onMounted, onUnmounted, provide, inject } from 'vue'

const SidebarSymbol = Symbol()

export function useSidebarProvider() {
  const isMobileOpen = ref(false)
  const isMobile = ref(false)
  const activeItem = ref(null)

  const handleResize = () => {
    const mobile = window.innerWidth < 1024
    isMobile.value = !mobile
  }

  onMounted(() => {
    handleResize()
    window.addEventListener('resize', handleResize)
  })

  onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
  })

  const toggleSidebar = () => {
    isMobileOpen.value = !isMobileOpen.value
  }

  const setActiveItem = (item) => {
    activeItem.value = item
  }

  const context = {
    isMobileOpen,
    activeItem,
    toggleSidebar,
    setActiveItem,
  }

  provide(SidebarSymbol, context)

  return context
}

export function useSidebar() {
  const context = inject(SidebarSymbol)
  if (!context) {
    throw new Error(
      'useSidebar must be used within a component that has SidebarProvider as an ancestor',
    )
  }
  return context
}
