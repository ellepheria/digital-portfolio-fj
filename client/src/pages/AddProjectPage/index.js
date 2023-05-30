import AddProjectPage from "@/pages/AddProjectPage/components/AddProjectPage.vue";

export default AddProjectPage;

export const AddProjectRoutes = [
    {
        path: '/add_project',
        name: 'AddProject',
        component: import('@/pages/AddProjectPage/components/AddProjectPage.vue'),
        meta: {
            title: 'Добавление проекта',
        },
    },
];