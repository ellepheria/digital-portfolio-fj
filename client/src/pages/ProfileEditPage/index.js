import ProfileEditPage from "@/pages/ProfileEditPage/components/ProfileEditPage.vue";

export default ProfileEditPage;

export const ProfileEditRoutes = [
    {
        path: '/:username/edit',
        name: 'ProfileEdit',
        component: () => import("@/pages/ProfileEditPage/components/ProfileEditPage.vue"),
        meta: {
            title: 'Редактирование профиля'
        }
    }
]