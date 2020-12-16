<template>
    <div class="home">
        <common-header></common-header>
        <div class="container">
            <section class="game-board">
                <h1 class="title">赛程板</h1>
                <div class="data">
                    <div class="game game1">
                        <div class="time">
                            <span>{{ game[0].date }}</span>
                            <span>{{ game[0].time }}</span>
                        </div>
                        <div class="team1">
                            <span>{{ game[0].first }}</span>
                            <span>{{ game[0].firstScore }}</span>
                        </div>
                        <div class="team2">
                            <span>{{ game[0].second }}</span>
                            <span>{{ game[0].secondScore }}</span>
                        </div>
                        <div class="button">数据</div>
                    </div>
                    <div class="game game2">
                        <div class="time">
                            <span>{{ game[1].date }}</span>
                            <span>{{ game[1].time }}</span>
                        </div>
                        <div class="team1">
                            <span>{{ game[1].first }}</span>
                            <span>{{ game[1].firstScore }}</span>
                        </div>
                        <div class="team2">
                            <span>{{ game[1].second }}</span>
                            <span>{{ game[1].secondScore }}</span>
                        </div>
                        <div class="button">数据</div>
                    </div>
                    <div class="game game3">
                        <div class="time">
                            <span>{{ game[2].date }}</span>
                            <span>{{ game[2].time }}</span>
                        </div>
                        <div class="team1">
                            <span>{{ game[2].first }}</span>
                            <span>{{ game[2].firstScore }}</span>
                        </div>
                        <div class="team2">
                            <span>{{ game[2].second }}</span>
                            <span>{{ game[2].secondScore }}</span>
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
                        <div class="title">{{ data[0].title }}</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>{{ data[0].no1 }}</span>
                                <span>{{ data[0].no1score }}</span>
                            </div>
                            <div class="two">
                                <span>2</span>
                                <span>{{ data[0].no2 }}</span>
                                <span>{{ data[0].no2score }}</span>
                            </div>
                            <div class="three">
                                <span>3</span>
                                <span>{{ data[0].no3 }}</span>
                                <span>{{ data[0].no3score }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail2">
                        <div class="title">{{ data[1].title }}</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>{{ data[1].no1 }}</span>
                                <span>{{ data[1].no1score }}</span>
                            </div>
                            <div class="two">
                                <span>2</span>
                                <span>{{ data[1].no2 }}</span>
                                <span>{{ data[1].no2score }}</span>
                            </div>
                            <div class="three">
                                <span>3</span>
                                <span>{{ data[1].no3 }}</span>
                                <span>{{ data[1].no3score }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail3">
                        <div class="title">{{ data[2].title }}</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>{{ data[2].no1 }}</span>
                                <span>{{ data[2].no1score }}</span>
                            </div>
                            <div class="two">
                                <span>2</span>
                                <span>{{ data[2].no2 }}</span>
                                <span>{{ data[2].no2score }}</span>
                            </div>
                            <div class="three">
                                <span>3</span>
                                <span>{{ data[2].no3 }}</span>
                                <span>{{ data[2].no3score }}</span>
                            </div>
                        </div>
                    </div>

                    <div class="detail detail4">
                        <div class="title">{{ data[3].title }}</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>{{ data[3].no1 }}</span>
                                <span>{{ data[3].no1score }}</span>
                            </div>
                            <div class="two">
                                <span>2</span>
                                <span>{{ data[3].no2 }}</span>
                                <span>{{ data[3].no2score }}</span>
                            </div>
                            <div class="three">
                                <span>3</span>
                                <span>{{ data[3].no3 }}</span>
                                <span>{{ data[3].no3score }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail5">
                        <div class="title">{{ data[4].title }}</div>
                        <div class="info">
                            <div class="one">
                                <span>1</span>
                                <span>{{ data[4].no1 }}</span>
                                <span>{{ data[4].no1score }}</span>
                            </div>
                            <div class="two">
                                <span>2</span>
                                <span>{{ data[4].no2 }}</span>
                                <span>{{ data[4].no2score }}</span>
                            </div>
                            <div class="three">
                                <span>3</span>
                                <span>{{ data[4].no3 }}</span>
                                <span>{{ data[4].no3score }}</span>
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
    data() {
        return {
            game: [
                {
                    date: "12-12",
                    time: "8:00",
                    first: "火箭",
                    firstScore: "99",
                    second: "公牛",
                    secondScore: "99",
                },
                {
                    date: "12-12",
                    time: "8:00",
                    first: "火箭",
                    firstScore: "99",
                    second: "公牛",
                    secondScore: "99",
                },
                {
                    date: "12-12",
                    time: "8:00",
                    first: "火箭",
                    firstScore: "99",
                    second: "公牛",
                    secondScore: "99",
                },
            ],
            data: [
                {
                    title: "得分",
                    no1: "xxx",
                    no1score: "xx",
                    no2: "xxx",
                    no2score: "xx",
                    no3: "xxx",
                    no3score: "xx",
                },
                {
                    title: "篮板",
                    no1: "xxx",
                    no1score: "xx",
                    no2: "xxx",
                    no2score: "xx",
                    no3: "xxx",
                    no3score: "xx",
                },
                {
                    title: "助攻",
                    no1: "xxx",
                    no1score: "xx",
                    no2: "xxx",
                    no2score: "xx",
                    no3: "xxx",
                    no3score: "xx",
                },
                {
                    title: "抢断",
                    no1: "xxx",
                    no1score: "xx",
                    no2: "xxx",
                    no2score: "xx",
                    no3: "xxx",
                    no3score: "xx",
                },
                {
                    title: "盖帽",
                    no1: "xxx",
                    no1score: "xx",
                    no2: "xxx",
                    no2score: "xx",
                    no3: "xxx",
                    no3score: "xx",
                },
            ],
        }
    },
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
