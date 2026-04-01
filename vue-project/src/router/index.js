import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import OverviewView from '@/views/dashboard/OverviewView.vue'
import ProgramsView from '@/views/dashboard/ProgramsView.vue'
import ProgramDetailView from '@/views/dashboard/ProgramDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: 'login',
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/dashboard',
      redirect: '/dashboard/overview',
      meta: {
        requiresAuth: true,
      },
      children: [
        {
          path: 'overview',
          name: 'overview',
          component: OverviewView,
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

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.path === '/login' || to.path === '/register') {
    if (token) {
      next('/dashboard/overview')
    } else {
      next()
    }
  }

  if (to.meta.requiresAuth) {
    if (!token) {
      next('/login') // Redirect to login if not authenticated
    } else {
      next() // Proceed to route if user is authenticated
    }
  } else {
    next() // Proceed to route if it's not protected
  }
})

export default router
