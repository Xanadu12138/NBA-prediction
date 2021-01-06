<template>
    <div class="prediction">
        <common-header></common-header>
        <section class="container">
            <h2 class="info">说明：本预测基于NBA真实数据</h2>
            <div class="wrapper">
                <div class="res">
                    <h1 class="title">预测结果</h1>
                    <div class="content">
                        <el-table
                            :data="resTableData"
                            :row-style="{ height: '8.5rem' }"
                            :row-class-name="tableRowClassName"
                            style="width: 100%; font-size: 2.5rem;"
                        >
                            <el-table-column
                                prop="time"
                                label="时间"
                                width="160"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="first"
                                label="主队"
                                width="160"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="second"
                                label="客队"
                                width="160"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="prediction"
                                label="胜负预测"
                                width="180"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </div>
                <div class="mvp">
                    <h1 class="title">MVP预测</h1>
                    <div class="content">
                        <div class="headImg">
                            <img
                                src="https://gdc.hupucdn.com/gdc/nba/players/uploads/gamespace/players/94444dafcb97b6e38ff62d05a09a507d.png"
                                alt=""
                            />
                            <div class="name">詹姆斯-哈登</div>
                        </div>
                        <vue-echarts
                            class="chart"
                            :options="getOptions()"
                        ></vue-echarts>
                    </div>
                </div>
            </div>

            <div class="custom">
                <h1 class="title">自定义预测</h1>
                <!-- <div class="content"></div>
                 -->
                <el-tabs type="border-card">
                    <el-tab-pane label="选择球队">
                        <el-select
                            v-model="value1"
                            clearable
                            placeholder="请选择"
                        >
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            >
                            </el-option>
                        </el-select>
                        <el-select
                            v-model="value2"
                            clearable
                            placeholder="请选择"
                        >
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                            >
                            </el-option>
                        </el-select>
                        <el-button
                            type="primary"
                            round
                            @click="handleClickSubmit"
                            >主要按钮</el-button
                        >
                    </el-tab-pane>
                    <el-tab-pane label="选择球员">预测</el-tab-pane>
                </el-tabs>
            </div>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"
import { prediction } from "@/api"

export default {
    name: "Prediction",
    components: {
        CommonHeader,
    },
    data() {
        return {
            resTableData: [
                {
                    time: "8:30",
                    first: "篮网",
                    second: "爵士",
                    prediction: "100%",
                },
                {
                    time: "9:00",
                    first: "灰熊",
                    second: "湖人",
                    prediction: "40%",
                },
                {
                    time: "10:00",
                    first: "掘金",
                    second: "森林狼",
                    prediction: "40%",
                },
                {
                    time: "11:00",
                    first: "快船",
                    second: "马刺",
                    prediction: "40%",
                },
                {
                    time: "11:30",
                    first: "快船",
                    second: "马刺",
                    prediction: "40%",
                },
            ],
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
                    PTS: 34.3,
                    FGAver: 0.447,
                    FGA: 4.4,
                    FG: 2,
                    "3PAver": 0.271,
                    "3PA": 1,
                    "3P": 0.3,
                    FTAver: 0.721,
                    FTA: 1.3,
                    FT: 0.9,
                    TRB: 6.6,
                    AST: 7.5,
                    STL: 1.8,
                    BLK: 0.9,
                    TOV: 0.8,
                    PF: 1.8,
                },
            ],
            options: [
                {
                    value: "CLE",
                    label: "骑士",
                },
                {
                    value: "ORL",
                    label: "魔术",
                },
                {
                    value: "IND",
                    label: "步行者",
                },
                {
                    value: "ATL",
                    label: "老鹰",
                },
                {
                    value: "PHI",
                    label: "76人",
                },
                {
                    value: "BKN",
                    label: "篮网",
                },
                {
                    value: "MIA",
                    label: "热火",
                },
                {
                    value: "NYK",
                    label: "尼克斯",
                },
                {
                    value: "BOS",
                    label: "凯尔特人",
                },
                {
                    value: "MIL",
                    label: "雄鹿",
                },
                {
                    value: "CHA",
                    label: "黄蜂",
                },
                {
                    value: "DET",
                    label: "活塞",
                },
                {
                    value: "TOR",
                    label: "猛龙",
                },
                {
                    value: "WAS",
                    label: "奇才",
                },
                {
                    value: "POR",
                    label: "开拓者",
                },
                {
                    value: "OKC",
                    label: "雷霆",
                },
                {
                    value: "NOP",
                    label: "鹈鹕",
                },
                {
                    value: "LAC",
                    label: "快船",
                },
                {
                    value: "LAL",
                    label: "湖人",
                },
                {
                    value: "PHX",
                    label: "太阳",
                },
                {
                    value: "SAC",
                    label: "国王",
                },
                {
                    value: "MIN",
                    label: "森林狼",
                },
                {
                    value: "SAS",
                    label: "马刺",
                },
                {
                    value: "UTA",
                    label: "爵士",
                },
                {
                    value: "CHI",
                    label: "公牛",
                },
                {
                    value: "DAL",
                    label: "独行侠",
                },
                {
                    value: "GSW",
                    label: "勇士",
                },
                {
                    value: "HOU",
                    label: "火箭",
                },
                {
                    value: "MEM",
                    label: "灰熊",
                },
                {
                    value: "DEN",
                    label: "掘金",
                },
            ],
            value1: "",
            value2: "",
            customPrediction: "",
        }
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
                        { name: "场均得分", max: 80 },
                        { name: "场均盖帽", max: 25 },
                        { name: "场均抢断", max: 25 },
                        { name: "场均篮板", max: 25 },
                        { name: "场均助攻", max: 25 },
                    ],
                    center: ["50%", "55%"],
                    radius: ["20%", "50%"],
                },
                series: [
                    {
                        name: "数据",
                        type: "radar",
                        data: [
                            {
                                value: [
                                    this.tableData[this.tableData.length - 1]
                                        .PTS,
                                    this.tableData[this.tableData.length - 1]
                                        .BLK,
                                    this.tableData[this.tableData.length - 1]
                                        .STL,
                                    this.tableData[this.tableData.length - 1]
                                        .TRB,
                                    this.tableData[this.tableData.length - 1]
                                        .AST,
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
        handleClickSubmit() {
            prediction(this.value1, this.value2).then((data) => {
                this.customPrediction = data.HomeTeamWinPossibility
                console.log(this.customPrediction)
            })
            // console.log(this.value1)
            // console.log(this.value2)
        },
    },
}
</script>

<style lang="stylus" scoped>
.container
    position relative
    width 90vw
    margin 0 auto
    .info
        margin 3rem 0
        font-size 2rem
        color #2c3e50
    .wrapper
        display flex
        justify-content space-between
        .res
            width 45vw
            .title
                font-size 4rem
                color #2c3e50
            .content
                // height 18rem
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        .mvp
            width 42vw
            .title
                font-size 4rem
                color #2c3e50
            .content
                height 30rem
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
                display flex
                align-items center
                .headImg
                    margin-left 3rem
                    text-align center
                    img
                        height 18rem
                    .name
                        font-size 3rem
                        margin-top 1rem
                .chart
                    width 35rem 27rem
    .custom
        width 105rem
        margin-bottom 3rem
        .title
            font-size 4rem
            color #2c3e50
        .content
            height 18rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
</style>

<style lang="stylus">
.echarts
    width 40rem
    height 30rem

// .el-tabs__content
//     display flex

.el-select
    margin 0 3rem 1rem 0

.el-button
    position relative
    left 40rem
</style>
