import AuthLayout from '@/layouts/AuthLayout.vue'
import BaseLayout from '@/layouts/BaseLayout.vue'

import DashboardPage from '@/pages/Dashboard.vue'
import ExercisePage from '@/pages/Exercise.vue'
import ExerciseDetailPage from '@/pages/ExerciseDetail.vue'
import ForgotPasswordPage from '@/pages/ForgotPassword.vue'
import LoginPage from '@/pages/Login.vue'
import SignupPage from '@/pages/Signup.vue'

const routes = [
  { path: '/', redirect: { name: 'login' } },
  {
    path: '/auth',
    component: AuthLayout,
    children: [
      {
        path: 'login',
        name: 'login',
        component: LoginPage,
      },
      {
        path: 'register',
        name: 'signup',
        component: SignupPage,
      },
      {
        path: 'forgot-password',
        name: 'forgotPassword',
        component: ForgotPasswordPage,
      },
    ],
  },
  {
    path: '/app',
    component: BaseLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: 'dashboard',
        name: 'dashboard',
        component: DashboardPage,
        meta: { requiresAuth: true, title: 'Dashboard' },
      },

      {
        path: 'exercises',
        name: 'exercises',
        component: ExercisePage,
        meta: { requiresAuth: true, title: 'Exercises' },
      },
      {
        path: 'exercises/:id',
        name: 'exercise-detail',
        component: ExerciseDetailPage,
        props: true,
        meta: { requiresAuth: true, title: 'Exercise Detail' },
      },
    ],
  },
]

export default routes
