import ProjectEditPage from "@/pages/ProjectEditPage/components/ProjectEditPage.vue";

export default ProjectEditPage;

export const ProjectEditRoutes = [
    {
        path: '/projects/:projectId/edit',
        name: 'ProjectEditPage',
        component: () => import('@/pages/ProjectEditPage/components/ProjectEditPage.vue'),
        meta: {
            title: 'Project Edit',
        }
    }
];