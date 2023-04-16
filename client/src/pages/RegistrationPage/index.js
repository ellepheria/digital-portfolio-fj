import RegistrationPage from "@/pages/RegistrationPage/components/RegistrationPage.vue";

export default RegistrationPage

export const registrationRoutes = [
    {
        path: '/registration',
        name: 'RegistrationPage',
        component: () => import("@/pages/RegistrationPage"),
        meta: {
            title: 'Registration'
        }
    },
]