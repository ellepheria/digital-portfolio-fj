import { createRouter, createWebHistory } from 'vue-router'
import { registrationRoutes } from "@/pages/RegistrationPage";
import { authorizationRoutes } from "@/pages/AuthorizationPage";

const routes = [
    ...registrationRoutes,
    ...authorizationRoutes,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
