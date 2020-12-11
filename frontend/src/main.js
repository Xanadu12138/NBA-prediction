// 引入必要组件
import Vue from "vue"
import App from "./App.vue"
import router from "./router/index"
import store from "./store"

// css
import "./assets/styles/reset.css"
import "./assets/styles/border.css"

// 引入组件
import echarts from "echarts";
import ELEMENT from 'element-ui';

Vue.prototype.$echarts = echarts;
Vue.use(ELEMENT)
Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app")
