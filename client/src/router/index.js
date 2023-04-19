import { createRouter, createWebHistory } from 'vue-router'
import { registrationRoutes } from "@/pages/RegistrationPage";
import { authorizationRoutes } from "@/pages/AuthorizationPage";
import { ProfileEditRoutes } from "@/pages/ProfileEditPage";
import { ProfileRoutes } from "@/pages/ProfilePage";

const routes = [
    ...registrationRoutes,
    ...authorizationRoutes,
    ...ProfileRoutes,
    ...ProfileEditRoutes,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    next();
})
export default router
