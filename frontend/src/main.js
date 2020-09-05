import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'
import Axios from 'axios'
import VueKinesis from 'vue-kinesis';

Vue.prototype.$http = Axios;

const token = localStorage.getItem('user-token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

Vue.use(VueKinesis)
Vue.config.productionTip = false

Vue.config({
  css: {
    loaderOptions: {
      sass: {
        data: `@import "~/assets/variables.scss']"`
      }
    }
  }
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
