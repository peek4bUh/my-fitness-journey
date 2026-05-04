import { useAuth } from '@/composables/useAuth.js'
import { createRouter, createWebHistory } from 'vue-router'

const LoginPage = () => import('@/pages/Login.vue')
const SignupPage = () => import('@/pages/Signup.vue')
const ForgotPasswordPage = () => import('@/pages/ForgotPassword.vue')
const DashboardPage = () => import('@/pages/Dashboard.vue')
const ExercisePage = () => import('@/pages/Exercise.vue')
const ProgramPage = () => import('@/pages/Program.vue')
const ProgramDetailPage = () => import('@/pages/ProgramDetail.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    {
      path: '/login',
      name: 'login',
      component: () => LoginPage(),
      meta: { guestOnly: true },
    },
    {
      path: '/register',
      name: 'signup',
      component: () => SignupPage(),
      meta: { guestOnly: true },
    },
    {
      path: '/forgot-password',
      name: 'forgotPassword',
      component: () => ForgotPasswordPage(),
      meta: { guestOnly: true },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => DashboardPage(),
      meta: { requiresAuth: true, title: 'Dashboard' },
    },
    {
      path: '/exercises',
      name: 'exercises',
      component: () => ExercisePage(),
      meta: { requiresAuth: true, title: 'Exercises' },
    },
    {
      path: '/programs',
      name: 'programs',
      component: () => ProgramPage(),
      meta: { requiresAuth: true, title: 'Programs' },
      children: [
        {
          path: ':id',
          name: 'program-detail',
          component: () => ProgramDetailPage(),
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
