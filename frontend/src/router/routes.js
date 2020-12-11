// export default routes = [ // 这样是错误的
export default [
    {
        path: "/",
        name: "home",
        component: () => import("../views/home/Home.vue"),
    },
]
