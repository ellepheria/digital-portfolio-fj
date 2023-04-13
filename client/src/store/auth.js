import $http from "@/api";
import {
    setToken,
    deleteToken,
    getToken,
} from "@/helpers";

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
                const { data } = await $http.post('http://127.0.0.1:5000/login', {
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
                const { data } = await $http.post('http://127.0.0.1:5000/register', {
                    email,
                    username,
                    password,
                });

                const token = data['access_token'];
                console.log(token)

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