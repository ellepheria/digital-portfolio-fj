import { createStore } from 'vuex'
import auth from "@/pages/AuthorizationPage/store";
import profile from "@/pages/ProfileEditPage/store"

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    profile
  }
})
