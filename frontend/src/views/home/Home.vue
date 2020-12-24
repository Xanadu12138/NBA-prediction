<template>
    <div class="home">
        <common-header></common-header>
        <div class="container">
            <section class="game-board">
                <h1 class="title">赛程板</h1>
                <div class="data">
                    <div class="game game1">
                        <div class="time">
                            <span>12-12</span> <span>8:00</span>
                        </div>
                        <div class="team1">
                            <span>火箭</span>
                            <span>99</span>
                        </div>
                        <div class="team2">
                            <span>公牛</span>
                            <span>99</span>
                        </div>
                        <div class="button">数据</div>
                    </div>
                    <div class="game game2">
                        <div class="time">
                            <span>12-12</span> <span>8:00</span>
                        </div>
                        <div class="team1">
                            <span>火箭</span>
                            <span>99</span>
                        </div>
                        <div class="team2">
                            <span>公牛</span>
                            <span>99</span>
                        </div>
                        <div class="button">数据</div>
                    </div>
                    <div class="game game3">
                        <div class="time">
                            <span>12-12</span> <span>8:00</span>
                        </div>
                        <div class="team1">
                            <span>火箭</span>
                            <span>99</span>
                        </div>
                        <div class="team2">
                            <span>公牛</span>
                            <span>99</span>
                        </div>
                        <div class="button">数据</div>
                    </div>
                    <div class="more">全部</div>
                </div>
            </section>
            <section class="data-board">
                <h1 class="title">数据版</h1>
                <div class="data">
                    <div class="detail detail1">
                        <div class="title">得分</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="two">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="three">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail2">
                        <div class="title">得分</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="two">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="three">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail3">
                        <div class="title">得分</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="two">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="three">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail4">
                        <div class="title">得分</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="two">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="three">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail5">
                        <div class="title">得分</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="two">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                            <div class="three">
                                <span>1</span>
                                <span>xxx</span>
                                <span>xx</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"

export default {
    name: "Home",
    components: {
        CommonHeader,
    },
}
</script>

<style lang="stylus" scoped>
.container
    margin 3rem 3rem
    .game-board
        margin 1rem
        position relative
        height 40rem
        .data
            font-size 3rem
            width 100%
            height 32.4rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            display flex
            justify-content space-between
            align-items center
            padding 0 3rem
            .game
                width 34rem
                height 26.4rem
                background-color #D8D8D8
                display flex
                flex-direction column
                justify-content space-around
                align-items center
                .button
                    font-size 2.2rem
            .more
                font-size 2rem
    .data-board
        margin 1rem
        position relative
        height 46rem
        .data
            font-size 3rem
            width 100%
            height 38.7rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            display flex
            justify-content space-around
            align-items center
            padding 0 3rem
            .detail
                width 21.3rem
                height 31rem
                display flex
                flex-direction column
                justify-content space-between
                align-items center
                .info
                    display flex
                    flex-direction column
                    justify-content space-around
                    align-items center
                    width inherit
                    height 25.3rem
                    background-color #D8D8D8
</style>
