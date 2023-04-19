import $http from "@/api";
import {
    setToken,
    deleteToken,
    getToken,
} from "@/helpers";
import {baseURI} from "@/api";

export default {
    namespaced: true,
    state: {
        token: getToken($http),
    },
    getters: {
        isAuthenticated(state) {
            const isTokenExists = !!state.token;
            return isTokenExists;
        },
    },
    mutations: {
        ['AUTH']: (state, token) => {
            state.token = token;
        },
        ['LOGOUT']: (state) => {
            state.token = '';
        },
    },
    actions: {
        async login({ commit }, { login, password, rememberMe }) {
            try {
                const { data } = await $http.post(baseURI + 'login', {
                    login,
                    password,
                });
                const token = data['access_token'];
                rememberMe ? setToken('local', token, $http) : setToken('session', token, $http);
                commit('AUTH', token);
                return { data };
            } catch (e) {
                console.log(e);
            }
        },
        async register({ commit }, { email, username, password }) {
            try {
                const { data } = await $http.post(baseURI + 'register', {
                    email,
                    username,
                    password,
                });
                const token = data['access_token'];
                setToken('local', token, $http);
                commit('AUTH', token);
                return { data };
            } catch (e) {
                console.log(e);
            }
        },
        logout({ commit }) {
            deleteToken($http);
            commit('LOGOUT');
            return;
        },
    },
}