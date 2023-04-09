import { createRouter, createWebHistory } from 'vue-router'
import RegistrationPage from "@/pages/RegistrationPage";

const routes = [
  {path: '/registration', component: RegistrationPage},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
