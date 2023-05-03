import {createStore} from 'vuex'
import auth from "@/pages/AuthorizationPage/store";
import profile from "@/pages/ProfileEditPage/store";
import project from "@/pages/ProjectEditPage/store";

export default createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        auth,
        profile,
        project,
    },
})
