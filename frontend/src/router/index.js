import Vue from "vue"
import VueRouter from "vue-router"
import routesArr from "./routes"

Vue.use(VueRouter)

const routes = routesArr

const router = new VueRouter({
    routes,
})

export default router
