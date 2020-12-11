const cdn = {
    externals: {
        vue: "Vue",
        vuex: "Vuex",
        "vue-router": "VueRouter",
        axios: "axios",
        "element-ui": "ELEMENT",
        echarts: "echarts",
    },
    css: ["https://cdn.bootcdn.net/ajax/libs/element-ui/2.14.1/theme-chalk/index.min.css"],
    js: [
        "https://cdn.bootcdn.net/ajax/libs/vue/2.6.11/vue.min.js",
        "https://cdn.bootcss.com/vuex/3.1.2/vuex.min.js",
        "https://cdn.bootcss.com/vue-router/3.1.3/vue-router.min.js",
        "https://cdn.bootcss.com/axios/0.19.2/axios.min.js",
        "https://cdn.bootcdn.net/ajax/libs/element-ui/2.14.1/index.min.js",
        "https://cdn.bootcdn.net/ajax/libs/echarts/4.9.0-rc.1/echarts.min.js"
    ],
}

module.exports = {
    configureWebpack: (config) => {
        config.externals = cdn.externals
    },
    chainWebpack: (config) => {
        config.plugin("html").tap((args) => {
            args[0].cdn = cdn
            return args
        })
    },
}
