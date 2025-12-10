import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import OverviewView from '@/views/dashboard/OverviewView.vue'
import PorgramsView from '@/views/dashboard/PorgramsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
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
      path: '/dashboard/overview',
      name: 'overview',
      component: OverviewView,
    },
    {
      path: '/dashboard/programs',
      name: 'programs',
      component: PorgramsView,
    },
  ],
})

export default router
