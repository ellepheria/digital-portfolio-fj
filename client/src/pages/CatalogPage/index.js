import CatalogPage from "@/pages/CatalogPage/components/CatalogPage.vue";

export default CatalogPage;

export const CatalogRoutes = [
    {
        path: '/catalog',
        component: import("@/pages/CatalogPage/components/CatalogPage.vue"),
        name: 'Catalog',
        meta: {
            title: 'Каталог',
            layout: 'default',
        },
    },
    {},
]