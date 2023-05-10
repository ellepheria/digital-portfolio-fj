import ProjectPage from "@/pages/ProjectPage/components/ProjectPage.vue";

export default ProjectPage;

export const ProjectRoutes = [
    {
        path: '/projects/:projectId',
        name: 'ProjectPage',
        component: () => import('@/pages/ProjectPage/components/ProjectPage.vue'),
        meta: {
            title: 'Project',
            layout: 'Project'
        }
    }
];