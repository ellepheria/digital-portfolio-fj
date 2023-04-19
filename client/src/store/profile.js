import $http from "@/api";
import {baseURI} from "@/api";

export default {
    namespaced: true,
    state: {
        currentData: {
            name: '',
            surname: '',
            username: '',
            age: '',
            type_of_activity: '',
            phone: '',
            about: '',
            education: '',
            technologies: '',
            social_networks: '',
        },
    },
    getters: {
        getCurrentData(state) {
            const data = state.currentData;
            return data;
        },
    },
    mutations: {
        ['UPDATE']: (state, newData) => {
            for (let key in newData) {
                state.currentData[key] = newData[key];
            }
        }
    },
    actions: {
        async editData ({ commit }, newData) {
            try {
                const { data } = await $http.post(baseURI + 'profile_edit', newData);
                if (data) {
                    commit('UPDATE', newData);
                }
            } catch (e) {
                console.log(e);
            }
        },
        async getCurrentProfileData({ commit }, username) {
            try {
                const { data } = await $http.get(baseURI + `get_user/${username}`);
                if (data) {
                    commit('UPDATE', data);
                    return data;
                }
            } catch (e) {
                console.log(e);
            }
            return;
        }
    }
}