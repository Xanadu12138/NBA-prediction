// export default routes = [ // 这样是错误的
export default [
    {
        path: "/",
        name: "Home",
        component: () => import("../views/home/Home.vue"),
    },
    {
        path: "/game",
        name: "Game",
        component: ()=> import("@/views/game/Game.vue"),
    },
    {
        path: "/data",
        name: "Data",
        component: ()=> import("@/views/alldata/AllData.vue")
    },
    {
        path: "/prediction",
        name: "Prediction",
        component: () => import("@/views/prediction/Prediction.vue")
    },
    {
        path: "/personaldata",
        name: "PersonalData",
        component: () => import("@/views/personaldata/PersonalData.vue")
    }
]
