import { onMounted, onUnmounted, provide, ref } from 'vue'

const SidebarSymbol = Symbol()

export function useSidebar() {
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
