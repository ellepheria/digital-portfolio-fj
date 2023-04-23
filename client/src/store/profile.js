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
            phone_number: '',
            about: '',
            education: '',
            technologies: '',
            social_networks: '',
            type_career: '',
        },
    },
    getters: {
        getCurrentData(state) {
            const data = state.currentData;
            return data;
        },
        getUsername(state) {
            return state.currentData.username;
        }
    },
    mutations: {
        ['UPDATE']: (state, newData) => {
            for (let key in newData) {
                state.currentData[key] = newData[key];
            }
        },
        ['CLEAR']: (state) => {
            for (let key in state.currentData) {
                state.currentData[key] = '';
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
        },
        setLocalData({ commit }, data) {
          commit('UPDATE', data);
        },
        clearProfileState({ commit }) {
            commit('CLEAR');
        },
    }
}