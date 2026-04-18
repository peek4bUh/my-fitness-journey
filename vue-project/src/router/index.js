import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '@/composables/useAuth.js'
import LoginView from '@/views/auth/LoginView.vue'
import SignupView from '@/views/auth/SignupView.vue'
import PasswordRecovery from '@/views/auth/PasswordRecovery.vue'
import OverviewView from '@/views/dashboard/OverviewView.vue'
import ProgramsView from '@/views/dashboard/ProgramsView.vue'
import ProgramDetailView from '@/views/dashboard/ProgramDetailView.vue'
import ExercisesView from '@/views/dashboard/ExercisesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/login' },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: { guestOnly: true },
    },
    {
      path: '/register',
      name: 'signup',
      component: SignupView,
      meta: { guestOnly: true },
    },
    {
      path: '/forgot-password',
      name: 'forgotPassword',
      component: PasswordRecovery,
      meta: { guestOnly: true },
    },
    {
      path: '/dashboard',
      meta: { requiresAuth: true },
      children: [
        {
          path: 'overview',
          name: 'overview',
          component: OverviewView,
        },
        {
          path: 'exercises',
          name: 'exercises',
          component: ExercisesView,
        },
        {
          path: 'programs',
          name: 'programs',
          component: ProgramsView,
          children: [
            {
              path: ':id',
              name: 'program-detail',
              component: ProgramDetailView,
              props: true,
            },
          ],
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
    return next('/dashboard/overview')
  }

  // 3. Logic for Protected pages
  if (to.meta.requiresAuth && !isLoggedIn) {
    return { name: 'Login' }
  }

  next()
})

export default router
