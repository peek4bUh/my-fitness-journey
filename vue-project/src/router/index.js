import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '../composables/useAuth'
import routes from './routes.js'

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)
  const { isAuthenticated } = useAuth()

  if (requiresAuth && !isAuthenticated.value) {
    next({ name: 'login' })
  } else if (!requiresAuth && isAuthenticated.value) {
    next({ name: 'dashboard' })
  } else {
    next()
  }
})

export default router
