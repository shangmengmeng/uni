import Vue from 'vue'
import App from './App'
import AppUrl from './api/baseApi.js'

Vue.config.productionTip = false

App.mpType = 'app'


const app = new Vue({
    ...App,
})
app.$mount()
