// 引入必要组件
import Vue from "vue"
import App from "./App.vue"
import router from "./router/index"
import store from "./store"
// 引入组件
import echarts from "echarts"
import ELEMENT from "element-ui"
import VueEcharts from "vue-echarts"
// css
import "./assets/styles/reset.css"
import "./assets/styles/border.css"

Vue.prototype.$echarts = echarts
Vue.component("vue-echarts", VueEcharts)
Vue.use(ELEMENT)
Vue.config.productionTip = false
Vue.config.devtools = true // cdn引入vue时，devtools需要在这里指定为ture才能使用

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app")
