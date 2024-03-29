import ProfilePage from "@/pages/ProfilePage/components/ProfilePage.vue";

export default ProfilePage;

export const ProfileRoutes = [
    {
        path: '/:username',
        name: 'ProfilePage',
        component: () => import("@/pages/ProfilePage/components/ProfilePage.vue"),
        meta: {
            title: 'Профиль',
            layout: 'default'
        }
    }
]