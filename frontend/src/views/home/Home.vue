<template>
    <div class="home">
        <common-header></common-header>
        <div class="container">
            <section class="game-board">
                <div class="title">
                    <img src="../../assets/pictures/战术板.png" alt="" />
                    <h1 class="title">赛程</h1>
                </div>
                <div class="data">
                    <div class="game game1">
                        <div class="separate time">
                            <div>{{ game[0].date }}</div>
                            <div>{{ game[0].time }}</div>
                        </div>
                        <div class="separate team1">
                            <div>{{ game[0].first }}</div>
                            <div>{{ game[0].firstScore }}</div>
                        </div>
                        <div class="separate team2">
                            <div>{{ game[0].second }}</div>
                            <div>{{ game[0].secondScore }}</div>
                        </div>
                    </div>
                    <div class="game game2">
                        <div class="time separate">
                            <div>{{ game[1].date }}</div>
                            <div>{{ game[1].time }}</div>
                        </div>
                        <div class="team1 separate">
                            <div>{{ game[1].first }}</div>
                            <div>{{ game[1].firstScore }}</div>
                        </div>
                        <div class="team2 separate">
                            <div>{{ game[1].second }}</div>
                            <div>{{ game[1].secondScore }}</div>
                        </div>
                    </div>
                    <div class="game game3">
                        <div class="time separate">
                            <div>{{ game[2].date }}</div>
                            <div>{{ game[2].time }}</div>
                        </div>
                        <div class="team1 separate">
                            <div>{{ game[2].first }}</div>
                            <div>{{ game[2].firstScore }}</div>
                        </div>
                        <div class="team2 separate">
                            <div>{{ game[2].second }}</div>
                            <div>{{ game[2].secondScore }}</div>
                        </div>
                    </div>
                    <div class="more" @click="goToPath('/game')">
                        <img
                            src="../../assets/pictures/方向-向右-粗.png"
                            alt=""
                        />
                    </div>
                </div>
            </section>
            <section class="data-board">
                <div class="title">
                    <img src="../../assets/pictures/数据.png" alt="" />
                    <h1 class="title">数据</h1>
                </div>
                <div class="data">
                    <div class="detail detail1">
                        <div class="detail-title">得分</div>
                        <div class="info">
                            <div class="one separate">
                                <div>1</div>
                                <div>{{ top[0].no1 }}</div>
                                <div>{{ top[0].no1score }}</div>
                            </div>
                            <div class="two separate">
                                <div>2</div>
                                <div>{{ top[0].no2 }}</div>
                                <div>{{ top[0].no2score }}</div>
                            </div>
                            <div class="three separate">
                                <div>3</div>
                                <div>{{ top[0].no3 }}</div>
                                <div>{{ top[0].no3score }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail2">
                        <div class="detail-title">篮板</div>
                        <div class="info">
                            <div class="one separate">
                                <div>1</div>
                                <div>{{ top[1].no1 }}</div>
                                <div>{{ top[1].no1score }}</div>
                            </div>
                            <div class="two separate">
                                <div>2</div>
                                <div>{{ top[1].no2 }}</div>
                                <div>{{ top[1].no2score }}</div>
                            </div>
                            <div class="three separate">
                                <div>3</div>
                                <div>{{ top[1].no3 }}</div>
                                <div>{{ top[1].no3score }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail3">
                        <div class="detail-title">助攻</div>
                        <div class="info">
                            <div class="one separate">
                                <div>1</div>
                                <div>{{ top[2].no1 }}</div>
                                <div>{{ top[2].no1score }}</div>
                            </div>
                            <div class="two separate">
                                <div>2</div>
                                <div>{{ top[2].no2 }}</div>
                                <div>{{ top[2].no2score }}</div>
                            </div>
                            <div class="three separate">
                                <div>3</div>
                                <div>{{ top[2].no3 }}</div>
                                <div>{{ top[2].no3score }}</div>
                            </div>
                        </div>
                    </div>

                    <div class="detail detail4">
                        <div class="detail-title">抢断</div>
                        <div class="info">
                            <div class="one separate">
                                <div>1</div>
                                <div>{{ top[3].no1 }}</div>
                                <div>{{ top[3].no1score }}</div>
                            </div>
                            <div class="two separate">
                                <div>2</div>
                                <div>{{ top[3].no2 }}</div>
                                <div>{{ top[3].no2score }}</div>
                            </div>
                            <div class="three separate">
                                <div>3</div>
                                <div>{{ top[3].no3 }}</div>
                                <div>{{ top[3].no3score }}</div>
                            </div>
                        </div>
                    </div>
                    <div class="detail detail5">
                        <div class="detail-title">盖帽</div>
                        <div class="info">
                            <div class="one separate">
                                <div>1</div>
                                <div>{{ top[4].no1 }}</div>
                                <div>{{ top[4].no1score }}</div>
                            </div>
                            <div class="two separate">
                                <div>2</div>
                                <div>{{ top[4].no2 }}</div>
                                <div>{{ top[4].no2score }}</div>
                            </div>
                            <div class="three separate">
                                <div>3</div>
                                <div>{{ top[4].no3 }}</div>
                                <div>{{ top[4].no3score }}</div>
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
import { goToPath } from "@/utils/function.js"
import { rank } from "@/api"

export default {
    name: "Home",
    data() {
        return {
            goToPath,
            game: [
                {
                    date: "1-6",
                    time: "8:30",
                    first: "篮网",
                    firstScore: "---",
                    second: "爵士",
                    secondScore: "---",
                },
                {
                    date: "1-6",
                    time: "9:00",
                    first: "灰熊",
                    firstScore: "---",
                    second: "湖人",
                    secondScore: "---",
                },
                {
                    date: "1-6",
                    time: "10:00",
                    first: "掘金",
                    firstScore: "---",
                    second: "森林狼",
                    secondScore: "---",
                },
            ],
            top: [],
        }
    },
    components: {
        CommonHeader,
    },
    mounted() {
        rank().then((data) => {
            // console.log(data.data[0])
            this.top = data.data
            // console.log(this.top)
        })
    },
}
</script>

<style lang="stylus" scoped>
.container
    margin 0rem 3rem 3rem 3rem
    .game-board
        margin 1rem
        position relative
        height 40rem
        .title
            font-size 4rem
            color #2c3e50
            display flex
            align-items center
            img
                height 5rem
                width 4.5rem
                margin-right 2rem
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
                background-color #ecf0f1
                display flex
                flex-direction column
                justify-content space-around
                align-items center
                .button
                    font-size 2.2rem
            .more
                font-size 2rem
                cursor pointer
                margin-left -4rem
                img
                    height 7rem
    .data-board
        margin 3rem 1rem 1rem 1rem
        position relative
        height 46rem
        .title
            font-size 4rem
            color #2c3e50
            display flex
            align-items center
            img
                height 4rem
                margin-right 2rem
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
                    background-color #bdc3c7
                    font-size 1.8rem


.separate
    display flex
    justify-content space-around
    width 100%
</style>
