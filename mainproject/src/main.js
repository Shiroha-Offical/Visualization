import Vue from 'vue'
import App from './App.vue'
import * as echarts from 'echarts'
import './style/reset.css'
import './style/style.css'
import ElementUI from 'element-ui'
import'element-ui/lib/theme-chalk/index.css'
import router from "@/router"
import axios from 'axios'


Vue.config.productionTip = false
Vue.prototype.$echarts = echarts
Vue.use(ElementUI)
Vue.prototype.axios = axios

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
