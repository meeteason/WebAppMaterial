import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const debug = process.env.NODE_ENV !== 'production'

const State = {
    Header: {
        show: true,
        back: false,
    },
    BottomBar: {
        show: true
    },
    Alert: {
        show: false,
        msg: "",
        btnText: "OK"
    },
    isLoading: false

}

const Getters = {

}

const Mutations = {
    updateLoadingStatus(state, isLoading) {
        state.isLoading = isLoading
    },
    updateHeader(state, header) {
        state.Header.show = header.show
        state.Header.back = header.back
    },
    setAlert(state, alert) {
        state.Alert = alert;
    }

}

const Actions = {

}

export default new Vuex.Store({
    state: State,
    getters: Getters,
    mutations: Mutations,
    actions: Actions,
    strict: debug
})