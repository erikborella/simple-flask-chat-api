import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    isAuth: false,
    jwt: localStorage.getItem('token'),
    endpoinst: {
      apiUrl: "127.0.0.1:5000",
      obtainToken: "127.0.0.1:5000/api/auth"
    }
  },
  mutations: {
    setAuthUser(state, {user, isAuth}) {
      Vue.set(state, 'user', user);
      Vue.set(state, 'isAuth', isAuth);
    },
    updateToken(state, newToken) {
      localStorage.setItem('token', newToken);
    },
    removeToken(state) {
      localStorage.removeItem('token');
      state.jwt = null;
    }
  },
  actions: {
  },
  modules: {
  }
})
