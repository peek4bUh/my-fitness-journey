import { createRouter, createWebHistory } from 'vue-router'
// import { authState } from './composables/useAuth'
import { useAuth } from './composables/useAuth'

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
      meta: { requiresAuth: false },
    },
    {
      path: '/register',
      name: 'signup',
      component: () => SignupPage(),
      meta: { requiresAuth: false },
    },
    {
      path: '/forgot-password',
      name: 'forgotPassword',
      component: () => ForgotPasswordPage(),
      meta: { requiresAuth: false },
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

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)
  const { isAuthenticated } = useAuth()

  if (requiresAuth && !isAuthenticated.value) {
    next('/login')
  } else if (!requiresAuth && isAuthenticated.value) {
    next('/dashboard')
  } else {
    next()
  }
})

export default router
