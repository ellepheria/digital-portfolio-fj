import $http from "@/api";
import {baseURI} from "@/api";
import {getUsername, setToken, setUsername} from "@/helpers";

export default {
    namespaced: true,
    state: {
        currentData: {
            title: '',
            shortDescription: '',
            description: '',
            added_links: '',
            owner: '',
            cover: '',
            images: {},
        },
    },
    getters: {
        getCurrentData(state) {
            const data = {
                title: state.currentData.title,
                shortDescription: state.currentData.shortDescription,
                description: state.currentData.description,
                added_links: state.currentData.added_links,
                owner: state.currentData.owner,
            };
            return data;
        },
        getCover(state) {
            return state.currentData.cover;
        },
        getImages(state) {
            return state.currentData.images;
        }
    },
    mutations: {
        ['UPLOAD_COVER']: (state, cover) => {
            state.currentData.cover = cover;
        },
        ['UPLOAD_IMAGES']: (state, images) => {
            state.currentData.images = images;
        },
        ['UPDATE_DATA']: (state, newData) => {
            state.currentData.title = newData.title;
            state.currentData.shortDescription = newData.shortDescription;
            state.currentData.description = newData.description;
            state.currentData.added_links = newData.added_links;
            state.currentData.owner = newData.owner;
        }
    },
    actions: {
        async editData({commit}, projectId, newData) {
            await $http.post(baseURI + 'projects/' + projectId + '/edit', newData)
                .then((res) => {
                    commit('UPDATE_DATA', newData);
                })
                .catch((e) => console.log(e));
        },
        async getCurrentData({commit}, projectId) {
            await $http.get(baseURI + projectId)
                .then((res) => {
                    commit('UPDATE_DATA', res.data);
                })
                .catch((e) => console.log(e))
        },
        async getCurrentImages({commit}, projectId) {
            await $http.get(baseURI + `projects/${projectId}/files/download`)
                .then((res) => {
                    commit('UPLOAD_COVER', res.data.cover);
                    commit('UPLOAD_IMAGES', res.data.images);
                })
                .catch((e) => console.log(e));
        },
        async uploadImages({commit}, projectId, data) {
            await $http.post(baseURI + `projects/${projectId}/files/upload`, data)
                .then((res) => {
                    commit('UPLOAD_COVER', data.cover);
                    commit('UPLOAD_IMAGES', data.images);
                })
                .catch((e) => console.log(e));
        }
    }
}