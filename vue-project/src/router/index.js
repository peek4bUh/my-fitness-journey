import { useAuth } from '@/composables/useAuth.js'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/auth/LoginView.vue'),
      meta: { guestOnly: true },
    },
    {
      path: '/register',
      name: 'signup',
      component: () => import('@/views/auth/SignupView.vue'),
      meta: { guestOnly: true },
    },
    {
      path: '/forgot-password',
      name: 'forgotPassword',
      component: () => import('@/views/auth/PasswordRecoveryView.vue'),
      meta: { guestOnly: true },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('@/views/DashboardView.vue'),
      meta: { requiresAuth: true, title: 'Dashboard' },
    },
    {
      path: '/exercises',
      name: 'exercises',
      component: () => import('@/views/ExercisesView.vue'),
      meta: { requiresAuth: true, title: 'Exercises' },
    },
    {
      path: '/programs',
      name: 'programs',
      component: () => import('@/views/ProgramsView.vue'),
      meta: { requiresAuth: true, title: 'Programs' },
      children: [
        {
          path: ':id',
          name: 'program-detail',
          component: () => import('@/views/ProgramDetailView.vue'),
          props: true,
          meta: { requiresAuth: true, title: 'Program Detail' },
        },
      ],
    },
  ],
})

router.beforeEach(async (to, from, next) => {
  const auth = useAuth()

  // 1. Only hit the backend if we haven't checked for a session yet
  if (!auth.isInitialCheckDone.value) {
    await auth.checkAuth()
  }

  const isLoggedIn = auth.isAuthenticated.value

  // 2. Logic for Guest-only pages (Login/Register)
  if (to.meta.guestOnly && isLoggedIn) {
    return next('/dashboard')
  }

  // 3. Logic for Protected pages
  if (to.meta.requiresAuth && !isLoggedIn) {
    return { name: 'Login' }
  }

  next()
})

export default router
