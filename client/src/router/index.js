import { createRouter, createWebHistory } from 'vue-router'
import { registrationRoutes } from "@/pages/RegistrationPage";
import { authorizationRoutes } from "@/pages/AuthorizationPage";
import { ProfileEditRoutes } from "@/pages/ProfileEditPage";
import { ProfileRoutes } from "@/pages/ProfilePage";
import { ProjectRoutes } from "@/pages/ProjectPage";
import { ProjectEditRoutes } from "@/pages/ProjectEditPage";
import { LikedProjectsRoutes } from "@/pages/LikedProjectsPage";
import { PortfolioPageRoutes } from "@/pages/PortfolioPage";

const routes = [
    ...registrationRoutes,
    ...authorizationRoutes,
    ...ProfileRoutes,
    ...ProfileEditRoutes,
    ...ProjectRoutes,
    ...ProjectEditRoutes,
    ...LikedProjectsRoutes,
    ...PortfolioPageRoutes,
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
