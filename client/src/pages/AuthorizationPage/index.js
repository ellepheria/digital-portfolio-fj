import AuthorizationPage from "@/pages/AuthorizationPage/components/AuthorizationPage.vue";
export default AuthorizationPage

export const authorizationRoutes = [
    {
        path: '/auth',
        name: 'AuthorizationPage',
        component: () => import("@/pages/AuthorizationPage")
    },
]