import ProfileEditPage from "@/pages/ProfileEditPage/components/ProfileEditPage.vue";

export default ProfileEditPage;

export const ProfileEditRoutes = [
    {
        path: '/:username/edit',
        name: 'ProfileEdit',
        component: () => import("@/pages/ProfileEditPage"),
        meta: {
            title: 'Редактирование профиля'
        }
    }
]