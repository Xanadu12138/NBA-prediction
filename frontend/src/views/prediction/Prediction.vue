<template>
    <div class="prediction">
        <common-header></common-header>
        <section class="container">
            <h2 class="info">说明：本预测基于xxxxxxxxx</h2>
            <div class="res">
                <h1 class="title">预测结果</h1>
                <div class="content">
                    <el-table
                        :data="resTableData"
                        :row-style="{ height: '8.5rem' }"
                        :row-class-name="tableRowClassName"
                        style="width: 100%; font-size: 2.5rem;"
                    >
                        <el-table-column prop="time" label="时间" width="200">
                        </el-table-column>
                        <el-table-column prop="first" label="主队" width="200">
                        </el-table-column>
                        <el-table-column prop="second" label="客队" width="200">
                        </el-table-column>
                        <el-table-column prop="data" label="数据" width="200">
                        </el-table-column>
                        <el-table-column
                            prop="prediction"
                            label="胜负预测"
                            width="220"
                        >
                        </el-table-column>
                        <el-table-column
                            prop="MVPprediction"
                            label="MVP预测"
                            width="220"
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
                            src="../../assets/pictures/headDefaultImg.jpeg"
                            alt=""
                        />
                        <div class="name">xxx</div>
                    </div>
                    <vue-echarts
                        class="chart"
                        :options="getOptions()"
                    ></vue-echarts>
                </div>
            </div>
            <div class="custom">
                <h1 class="title">自定义预测</h1>
                <div class="content"></div>
            </div>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"

export default {
    name: "Prediction",
    components: {
        CommonHeader,
    },
    data() {
        return {
            resTableData: [
                {
                    time: "8:00",
                    first: "火箭",
                    second: "公牛",
                    prediction: "40%",
                    MVP: "xxx",
                },
                {
                    time: "8:00",
                    first: "火箭",
                    second: "公牛",
                    prediction: "40%",
                    MVP: "xxx",
                },
                {
                    time: "8:00",
                    first: "火箭",
                    second: "公牛",
                    prediction: "40%",
                    MVP: "xxx",
                },
                {
                    time: "8:00",
                    first: "火箭",
                    second: "公牛",
                    prediction: "40%",
                    MVP: "xxx",
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
                        { name: "场均得分", max: 150 },
                        { name: "场均盖帽", max: 30 },
                        { name: "场均抢断", max: 30 },
                        { name: "场均篮板", max: 30 },
                        { name: "场均助攻", max: 30 },
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
                                    this.tableData[0].PTS,
                                    this.tableData[0].BLK,
                                    this.tableData[0].STL,
                                    this.tableData[0].TRB,
                                    this.tableData[0].AST,
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
    .res
        width 124rem
        // height 28rem
        .title
            font-size 4rem
            color #2c3e50
        .content
            // height 18rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
    .mvp
        width 50vw
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
            .chart
                width 35rem 27rem
    .custom
        width 105rem
        .title
            font-size 4rem
            color #2c3e50
        .content
            height 18rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
</style>
