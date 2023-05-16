import PortfolioPage from "@/pages/PortfolioPage/components/PortfolioPage.vue";

export default PortfolioPage;

const PortfolioPageRoutes = [
    {
        path: '/:username/portfolio',
        name: 'Portfolio',
        component: import('@/pages/PortfolioPage/components/PortfolioPage.vue'),
        meta: {
            title: 'Портфолио',
            layout: 'Portfolio',
        }
    }
]

export {PortfolioPageRoutes};