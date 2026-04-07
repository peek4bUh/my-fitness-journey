import 'primeicons/primeicons.css'
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import router from './router'
import Aura from '@primeuix/themes/aura'
import axios from 'axios'

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/v1/'

const app = createApp(App)
app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      prefix: 'p',
      darkModeSelector: false,
      cssLayer: false,
    },
  },
})

app.use(router)
app.mount('#app')
