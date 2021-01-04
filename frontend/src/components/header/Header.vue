<template>
    <div class="common-header">
        <div class="container">
            <div class="logo" @click="goToPath('/')">
                <img class="ball" src="../../assets/pictures/篮球.png" alt="" />
                <span>NBA PREDICTION</span>
            </div>
            <nav class="nav">
                <div class="game" @click="goToPath('/game')">赛程</div>
                <div class="data" @click="goToPath('/data')">数据</div>
                <div class="prediction" @click="goToPath('/prediction')">
                    预测
                </div>
            </nav>
        </div>
    </div>
</template>

<script>
import { goToPath } from "@/utils/function.js"

export default {
    name: "CommonHeader",
    data() {
        return {
            goToPath,
        }
    },
}
</script>

<style lang="stylus" scoped>
.common-header
    background-color #74b9ff
    font-size 3rem
    .container
        width 90vw
        height 7rem
        margin 0 auto
        display flex
        justify-content space-between
        align-items center
        cursor pointer

        .logo
            .ball
                height 3.5rem
                line-height 3.5rem
                vertical-align top
                margin-right 2rem
        .nav
            // flex 1 1 10rem
            flex-basis 36rem
            display flex
            justify-content space-between
</style>
