// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import 'swiper/dist/css/swiper.css'
import VueMaterial from 'vue-material'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'vue-material/dist/vue-material.min.css'
import theme from './assets/sass/theme.scss'
import './assets/css/animate.css'
Vue.use(VueMaterial)
Vue.use(VueAwesomeSwiper, /* { default global options } */)

Vue.config.productionTip = false


//the router loading
router.beforeEach(function (to, from, next) {
  store.commit('updateLoadingStatus', true)
  next()
})

router.afterEach(function (to) {
  store.commit('updateLoadingStatus', false)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
