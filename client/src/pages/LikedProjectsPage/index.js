import LikedProjectsPage from "@/pages/LikedProjectsPage/components/LikedProjectsPage.vue";

export default LikedProjectsPage;

export const LikedProjectsRoutes = [
    {
        path: '/:username/likedProjects',
        name: 'LikedProjectsPage',
        component: () => import('@/pages/LikedProjectsPage/components/LikedProjectsPage.vue'),
        meta: {
            title: 'Liked Projects',
        },
    },
];