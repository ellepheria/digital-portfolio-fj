import $http from "@/api";
import {baseURI} from "@/api";
import {getUsername, setToken, setUsername} from "@/helpers";

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
            type_of_activity: '',
            cover_path: '',
            profile_picture_path: '',
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
        },
        ['CLEAR']: (state) => {
            for (let key in state.currentData) {
                state.currentData[key] = '';
            }
        },
        ['UPDATE_IMAGES']: (state, images) => {
            state.currentData.cover_path = images.cover;
            state.currentData.profile_picture_path = images.profile_picture;
        }
    },
    actions: {
        async editData({commit}, newData) {
            try {
                await $http.post(baseURI + 'profile_edit', newData)
                    .then((res) => {
                        commit('UPDATE', newData);
                        setToken('local', res.data.access_token, $http);
                        setUsername(res.data.username);
                    });
            } catch (e) {
                console.log(e);
            }
        },
        async getCurrentProfileData({commit}, username) {
            try {
                const {data} = await $http.get(baseURI + `get_profile/${getUsername()}`);
                data.cover_path = data.cover_path ?
                    baseURI + data.cover_path : '';
                data.profile_picture_path = data.profile_picture_path ?
                    baseURI + data.profile_picture_path : '';
                if (data) {
                    commit('UPDATE', data);
                    return data;
                }
            } catch (e) {
                console.log(e);
            }
            return;
        },
        uploadImages({commit}, images) {
            commit('UPDATE_IMAGES', images);
        },
        setLocalData({commit}, data) {
            commit('UPDATE', data);
        },
        clearProfileState({commit}) {
            commit('CLEAR');
        },
    }
}