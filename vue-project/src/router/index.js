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
      components: {
        default: () => LoginView,
      },
    },
    {
      path: '/register',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/dashboard',
      redirect: '/dashboard/overview',
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

export default router
