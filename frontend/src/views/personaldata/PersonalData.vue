<template>
    <div class="personal-data">
        <common-header></common-header>
        <section class="container">
            <div class="basic">
                <div class="avatar">
                    <img :src="data.basicData.img" alt="" />
                </div>
                <div class="info">
                    <div class="title">球员信息</div>
                    <div class="data-simple">
                        <div class="name">姓名：{{ data.basicData.name }}</div>
                        <div class="num">号码：{{ data.basicData.num }}</div>
                        <div class="pos">位置：{{ data.basicData.pos }}</div>
                        <div class="tall">身高：{{ data.basicData.tall }}</div>
                        <div class="bri">生日：{{ data.basicData.bri }}</div>
                        <div class="tm">球队：{{ data.basicData.tm }}</div>
                    </div>
                </div>
                <div class="ability">
                    <div class="title">球员能力</div>
                    <vue-echarts
                        class="chart"
                        :options="getOptions()"
                    ></vue-echarts>
                </div>
            </div>
            <div class="data-table">
                <div class="title">数据表格</div>
                <div class="table-all">
                    <el-table
                        :data="data.tableData"
                        :row-style="{ height: '8.5rem' }"
                        :row-class-name="tableRowClassName"
                        style="width: 100%; font-size: 1.6rem;"
                    >
                        <el-table-column prop="season" label="赛季" width="70">
                        </el-table-column>
                        <el-table-column prop="tm" label="球队" width="70">
                        </el-table-column>
                        <el-table-column prop="mp" label="上场时间" width="90">
                        </el-table-column>
                        <el-table-column prop="pts" label="得分" width="70">
                        </el-table-column>
                        <el-table-column
                            prop="fgaver"
                            label="命中率"
                            width="80"
                        >
                        </el-table-column>
                        <el-table-column prop="fga" label="投篮数" width="70">
                        </el-table-column>
                        <el-table-column
                            prop="3paver"
                            label="三分率"
                            width="80"
                        >
                        </el-table-column>
                        <el-table-column prop="3pa" label="三分数" width="70">
                        </el-table-column>
                        <el-table-column
                            prop="ftaver"
                            label="罚球率"
                            width="80"
                        >
                        </el-table-column>
                        <el-table-column prop="fta" label="罚球数" width="75">
                        </el-table-column>
                        <el-table-column prop="trb" label="篮板" width="75">
                        </el-table-column>
                        <el-table-column prop="ast" label="助攻" width="75">
                        </el-table-column>
                        <el-table-column prop="stl" label="抢断" width="75">
                        </el-table-column>
                        <el-table-column prop="blk" label="盖帽" width="75">
                        </el-table-column>
                        <el-table-column prop="tov" label="失误" width="75">
                        </el-table-column>
                        <el-table-column prop="pf" label="个犯" width="75">
                        </el-table-column>
                    </el-table>
                </div>
            </div>
            <div class="data-all">
                <div class="title">数据图表</div>
                <div class="card-all">
                    <data-detail></data-detail>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"
import DataDetail from "./components/DataDetail"
import { playerInfo } from "@/api"

export default {
    name: "PersonalData",
    components: {
        CommonHeader,
        DataDetail,
    },
    data() {
        return {
            data: {
                basicData: {
                    img: "../../assets/pictures/headDefaultImg.jpeg",
                    name: "阿尔德里奇",
                    num: "02",
                    pos: "中锋",
                    tall: "210",
                    bri: "1985-07-19",
                    tm: "马刺",
                },
                tableData: [
                    {
                        Season: "2014-2015",
                        Tm: "ORL",
                        MP: 17,
                        PTS: 5.2,
                        FGAver: 0.447,
                        FGA: 4.4,
                        FG: 2,
                        "3PAver": 0.271,
                        "3PA": 1,
                        "3P": 0.3,
                        FTAver: 0.721,
                        FTA: 1.3,
                        FT: 0.9,
                        TRB: 3.6,
                        AST: 0.7,
                        STL: 0.4,
                        BLK: 0.5,
                        TOV: 0.8,
                        PF: 1.8,
                    },
                    {
                        Season: "2015-2016",
                        Tm: "ORL",
                        MP: 17,
                        PTS: 5.2,
                        FGAver: 0.447,
                        FGA: 4.4,
                        FG: 2,
                        "3PAver": 0.271,
                        "3PA": 1,
                        "3P": 0.3,
                        FTAver: 0.721,
                        FTA: 1.3,
                        FT: 0.9,
                        TRB: 3.6,
                        AST: 0.7,
                        STL: 0.4,
                        BLK: 0.5,
                        TOV: 0.8,
                        PF: 1.8,
                    },
                    {
                        Season: "2016-2017",
                        Tm: "ORL",
                        MP: 17,
                        PTS: 5.2,
                        FGAver: 0.447,
                        FGA: 4.4,
                        FG: 2,
                        "3PAver": 0.271,
                        "3PA": 1,
                        "3P": 0.3,
                        FTAver: 0.721,
                        FTA: 1.3,
                        FT: 0.9,
                        TRB: 3.6,
                        AST: 0.7,
                        STL: 0.4,
                        BLK: 0.5,
                        TOV: 0.8,
                        PF: 1.8,
                    },
                    {
                        Season: "2017-2018",
                        Tm: "ORL",
                        MP: 17,
                        PTS: 5.2,
                        FGAver: 0.447,
                        FGA: 4.4,
                        FG: 2,
                        "3PAver": 0.271,
                        "3PA": 1,
                        "3P": 0.3,
                        FTAver: 0.721,
                        FTA: 1.3,
                        FT: 0.9,
                        TRB: 3.6,
                        AST: 0.7,
                        STL: 0.4,
                        BLK: 0.5,
                        TOV: 0.8,
                        PF: 1.8,
                    },
                    {
                        Season: "2019-2020",
                        Tm: "ORL",
                        MP: 17,
                        PTS: 5.2,
                        FGAver: 0.447,
                        FGA: 4.4,
                        FG: 2,
                        "3PAver": 0.271,
                        "3PA": 1,
                        "3P": 0.3,
                        FTAver: 0.721,
                        FTA: 1.3,
                        FT: 0.9,
                        TRB: 3.6,
                        AST: 0.7,
                        STL: 0.4,
                        BLK: 0.5,
                        TOV: 0.8,
                        PF: 1.8,
                    },
                ],
            },
            playerID: this.$route.params.id,
        }
    },
    provide() {
        return {
            getTableData: this.getTableData,
            // tableData: this.data.tableData,
        }
    },
    created() {
        playerInfo(this.playerID).then((data) => {
            this.data = data
            // console.log(this.data.tableData)
        })
    },
    methods: {
        getOptions() {
            return {
                tooltip: {},
                radar: {
                    name: {
                        textStyle: {
                            color: "#fff",
                            backgroundColor: "#999",
                            borderRadius: 3,
                            padding: [3, 5],
                        },
                    },
                    indicator: [
                        { name: "场均得分", max: 150 },
                        { name: "场均盖帽", max: 30 },
                        { name: "场均抢断", max: 30 },
                        { name: "场均篮板", max: 30 },
                        { name: "场均助攻", max: 30 },
                    ],
                    center: ["50%", "55%"],
                    radius: ["20%", "70%"],
                },
                series: [
                    {
                        name: "数据",
                        type: "radar",
                        data: [
                            {
                                value: [
                                    this.data.tableData[0].pts,
                                    this.data.tableData[0].blk,
                                    this.data.tableData[0].stl,
                                    this.data.tableData[0].trb,
                                    this.data.tableData[0].ast,
                                ],
                                name: "数据情况",
                            },
                        ],
                        areaStyle: {
                            opacity: 0.9,
                            color: new this.$echarts.graphic.RadialGradient(
                                0.5,
                                0.5,
                                1,
                                [
                                    {
                                        color: "#B8D3E4",
                                        offset: 0,
                                    },
                                    {
                                        color: "#72ACD1",
                                        offset: 1,
                                    },
                                ]
                            ),
                        },
                    },
                ],
            }
        },
        getTableData() {
            console.log(this.data.tableData)
            return this.data.tableData
        },
    },
}
</script>

<style lang="stylus" scoped>
.container
    position relative
    width 85vw
    margin 0 auto
    .basic
        display flex
        justify-content space-between
        width 120rem
        height 30rem
        margin 3rem 0
        .avatar
            width 15rem
            height 21rem
            margin 4.5rem 0 0 0
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            img
                width 100%
                overflow hidden
        .info
            width 50rem
            height 30rem
            .title
                font-size 2.2rem
            .data-simple
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
                padding 5rem
                margin-top 2rem
                font-size 2rem
                display grid
                grid-template-columns repeat(2, 26rem)
                grid-template-areas "name num" "pos tall" "bri tm"
                grid-row-gap 5rem
                .name
                    grid-area name
                .num
                    grid-area num
                .pos
                    grid-area pos
                .tall
                    grid-area tall
                .bri
                    grid-area bri
                .tm
                    grid-area tm
        .ability
            width 35rem
            height 30rem
            .title
                font-size 2.2rem
            .chart
                margin-top 2rem
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
                width 35rem
                height 27rem
    .data-table
        width 120rem
        // height 52rem
        margin 5rem 0
        .title
            font-size 2.2rem
            margin-bottom 2rem
        .table-all
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
    .data-all
        width 120rem
        // height 36rem
        margin 5rem 0
        .title
            font-size 2.2rem
            margin-bottom 2rem
        .card-all
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
</style>
