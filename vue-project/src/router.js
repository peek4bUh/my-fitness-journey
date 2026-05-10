import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from './composables/useAuth'

const AuthLayout = () => import('@/layouts/AuthLayout.vue')
const BaseLayout = () => import('@/layouts/BaseLayout.vue')

const LoginPage = () => import('@/pages/Login.vue')
const SignupPage = () => import('@/pages/Signup.vue')
const ForgotPasswordPage = () => import('@/pages/ForgotPassword.vue')
const DashboardPage = () => import('@/pages/Dashboard.vue')
const ExercisePage = () => import('@/pages/Exercise.vue')
const ExerciseDetailPage = () => import('@/pages/ExerciseDetail.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: { name: 'login' } },
    {
      path: '/auth',
      component: () => AuthLayout(),
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => LoginPage(),
        },
        {
          path: 'register',
          name: 'signup',
          component: () => SignupPage(),
        },
        {
          path: 'forgot-password',
          name: 'forgotPassword',
          component: () => ForgotPasswordPage(),
        },
      ],
    },
    {
      path: '/app',
      component: () => BaseLayout(),
      meta: { requiresAuth: true },
      children: [
        {
          path: 'dashboard',
          name: 'dashboard',
          component: () => DashboardPage(),
          meta: { requiresAuth: true, title: 'Dashboard' },
        },

        {
          path: 'exercises',
          name: 'exercises',
          component: () => ExercisePage(),
          meta: { requiresAuth: true, title: 'Exercises' },
        },
        {
          path: 'exercises/:id',
          name: 'exercise-detail',
          component: () => ExerciseDetailPage(),
          props: true,
          meta: { requiresAuth: true, title: 'Exercise Detail' },
        },
      ],
    },
  ],
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
