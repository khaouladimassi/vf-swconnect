// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedOffers: []
  },
  mutations: {
    setSelectedOffers(state, offers) {
      state.selectedOffers = offers;
    }
  },
  actions: {
    updateSelectedOffers({ commit }, offers) {
      commit('setSelectedOffers', offers);
    }
  },
  getters: {
    getSelectedOffers: state => state.selectedOffers
  }
});
