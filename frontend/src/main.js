import Vue from 'vue'
import App from './App.vue'
import { LayoutPlugin, NavbarPlugin, CardPlugin, FormSelectPlugin, OverlayPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import i18n from '@/plugins/i18n'

Vue.use(LayoutPlugin)
Vue.use(NavbarPlugin)
Vue.use(CardPlugin)
Vue.use(FormSelectPlugin)
Vue.use(OverlayPlugin)

Vue.config.productionTip = false

new Vue({
  i18n,
  render: h => h(App)
}).$mount('#app')
