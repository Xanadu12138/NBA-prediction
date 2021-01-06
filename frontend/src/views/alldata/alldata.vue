<template>
    <div class="all-data">
        <common-header></common-header>
        <section class="body">
            <section class="content">
                <div class="teams">
                    <h1 class="title">球队信息</h1>
                    <div class="teams-info">
                        <el-table
                            class="team-table"
                            :data="teamsTableData"
                            stripe
                            style="width: 100%"
                            :cell-class-name="tableCellClassName"
                            @cell-click="handleClickTeam"
                        >
                            <el-table-column
                                prop="east"
                                label="球队"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column prop="west" label="" width="180">
                            </el-table-column>
                        </el-table>
                    </div>
                </div>
                <div class="persons">
                    <h1 class="title">球员信息</h1>
                    <div class="persons-info">
                        <el-table
                            :data="personsTableData"
                            stripe
                            style="width: 100%"
                            :row-style="{ height: '6rem' }"
                            @row-click="handleClickGoToDetail"
                        >
                            <el-table-column
                                prop="name"
                                label="姓名"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="score"
                                label="场均得分"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="board"
                                label="场均篮板"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="assist"
                                label="场均助攻"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="steal"
                                label="场均抢断"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="blockshots"
                                label="场均盖帽"
                                width="180"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </div>
            </section>
            <section class="team-map">
                <div class="title">球队数据地图</div>
                <div class="map">
                    <el-card class="map-card">
                        <vue-echarts :options="options" />
                    </el-card>
                </div>
            </section>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"
import "echarts/extension/bmap/bmap"
import { teamInfo } from "@/api"

const eastData = [
    { name: "波士顿凯尔特人", rank: 4 }, // 16 - `${number}`
    { name: "布鲁克林篮网", rank: 10 },
    { name: "纽约尼克斯", rank: 5 },
    { name: "费城76人", rank: 1 },
    { name: "多伦多猛龙", rank: 14 },
    { name: "芝加哥公牛", rank: 11 },
    { name: "克利夫兰骑士", rank: 6 },
    { name: "底特律活塞", rank: 15 },
    { name: "印第安那步行者", rank: 3 },
    { name: "密尔沃基雄鹿", rank: 7 },
    { name: "亚特兰大老鹰", rank: 8 },
    { name: "夏洛特黄蜂", rank: 13 },
    { name: "迈阿密热火", rank: 9 },
    { name: "奥兰多魔术", rank: 2 },
    { name: "华盛顿奇才", rank: 12 },
]
const westData = [
    { name: "丹佛掘金", rank: 11 },
    { name: "明尼苏达森林狼", rank: 13 },
    { name: "俄克拉何马城雷霆", rank: 15 },
    { name: "波特兰开拓者", rank: 7 },
    { name: "犹他爵士", rank: 4 },
    { name: "金州勇士", rank: 6 },
    { name: "洛杉矶快船", rank: 1 },
    { name: "洛杉矶湖人", rank: 3 },
    { name: "菲尼克斯太阳", rank: 2 },
    { name: "萨克拉门托国王", rank: 9 },
    { name: "达拉斯独行侠", rank: 8 },
    { name: "休斯敦火箭", rank: 10 },
    { name: "孟菲斯灰熊", rank: 14 },
    { name: "新奥尔良鹈鹕", rank: 5 },
    { name: "圣安东尼奥马刺", rank: 12 },
]
const eastCoordMap = {
    波士顿凯尔特人: [-71.06222, 42.36639],
    布鲁克林篮网: [-73.9746889, 40.68265],
    纽约尼克斯: [-73.99361, 40.75056],
    费城76人: [-75.171968, 39.901193],
    多伦多猛龙: [-79.379088, 43.643543],
    芝加哥公牛: [-83.0549111, 42.3411722],
    克利夫兰骑士: [-81.688097, 41.496745],
    底特律活塞: [-83.05522438661731, 42.34123739231859],
    印第安那步行者: [-86.155493, 39.7642],
    密尔沃基雄鹿: [-87.911025, 43.038389],
    亚特兰大老鹰: [-84.39639, 33.75722],
    夏洛特黄蜂: [-80.83940183101089, 35.2252307588481],
    迈阿密热火: [-80.1870441042567, 25.7815752793962],
    奥兰多魔术: [-81.38381058699731, 28.5393816102714],
    华盛顿奇才: [-77.02089746159612, 38.89806912934071],
}
const westCoordMap = {
    丹佛掘金: [-105.00765644622516, 39.748837955759456],
    明尼苏达森林狼: [-93.27606251536693, 44.979486046445004],
    俄克拉何马城雷霆: [-97.51514598867696, 35.46364314203038],
    波特兰开拓者: [-122.66684230185716, 45.531677814738906],
    犹他爵士: [-111.90111958852118, 40.768300581444535],
    金州勇士: [-122.20296973093944, 37.750309779664626],
    洛杉矶快船: [-118.2437080043135, 34.0533141075975],
    洛杉矶湖人: [-118.2865222863597, 34.02851797727663],
    菲尼克斯太阳: [-112.071189573386, 33.44573698068085],
    萨克拉门托国王: [-121.49968165975133, 38.58021286663735],
    达拉斯独行侠: [-96.81016945991203, 32.79047662782887],
    休斯敦火箭: [-95.36212195998714, 29.7507696965931],
    孟菲斯灰熊: [-90.05059713101329, 35.138124232855446],
    新奥尔良鹈鹕: [-90.08206753114615, 29.949035081828313],
    圣安东尼奥马刺: [-98.43749203115844, 29.427133392795536],
}
const convertData = function(data, coordMap) {
    const res = []
    data.forEach((item) => {
        const { name, rank } = item
        const coord = coordMap[name]
        res.push({ name, value: [...coord, rank] })
    })
    // console.log(res)
    return res
}

export default {
    name: "AllData",
    components: {
        CommonHeader,
    },
    data() {
        return {
            teamsTableData: [
                {
                    east: "骑士",
                    west: "魔术",
                },
                {
                    east: "步行者",
                    west: "老鹰",
                },
                {
                    east: "76人",
                    west: "篮网",
                },
                {
                    east: "热火",
                    west: "尼克斯",
                },
                {
                    east: "凯尔特人",
                    west: "雄鹿",
                },
                {
                    east: "黄蜂",
                    west: "活塞",
                },
                {
                    east: "猛龙",
                    west: "奇才",
                },
                {
                    east: "开拓者",
                    west: "雷霆",
                },
                {
                    east: "鹈鹕",
                    west: "快船",
                },

                {
                    east: "湖人",
                    west: "太阳",
                },
                {
                    east: "国王",
                    west: "森林狼",
                },
                {
                    east: "马刺",
                    west: "爵士",
                },
                {
                    east: "公牛",
                    west: "独行侠",
                },
                {
                    east: "勇士",
                    west: "火箭",
                },
                {
                    east: "灰熊",
                    west: "掘金",
                },
            ],
            personsTableData: null,
            options: {},
            teamID: 1,
        }
    },
    // watch: {
    //     teamID() {
    //         teamInfo(this.teamID).then((data) => {
    //             console.log(data)
    //             this.personsTableData = data.personsTableData
    //             console.log(this.personsTableData)
    //         })
    //     },
    // },
    mounted() {
        teamInfo(this.teamID).then((data) => {
            console.log(data)
            this.personsTableData = data.personsTableData
            console.log(this.personsTableData)
        })

        this.options = {
            bmap: {
                key: "D6wdYEzm1ZXfXV88WgSMuxNEXHaXacTz",
                center: [-97.096886, 36.647638],
                zoom: 5,
                roam: false,
                mapStyle: {
                    styleJson: [
                        {
                            featureType: "water",
                            elementType: "all",
                            stylers: {
                                color: "#d1d1d1",
                            },
                        },
                        {
                            featureType: "land",
                            elementType: "all",
                            stylers: {
                                color: "#f3f3f3",
                            },
                        },
                        {
                            featureType: "railway",
                            elementType: "all",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "highway",
                            elementType: "all",
                            stylers: {
                                color: "#fdfdfd",
                            },
                        },
                        {
                            featureType: "highway",
                            elementType: "labels",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "arterial",
                            elementType: "geometry",
                            stylers: {
                                color: "#fefefe",
                            },
                        },
                        {
                            featureType: "arterial",
                            elementType: "geometry.fill",
                            stylers: {
                                color: "#fefefe",
                            },
                        },
                        {
                            featureType: "poi",
                            elementType: "all",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "green",
                            elementType: "all",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "subway",
                            elementType: "all",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "manmade",
                            elementType: "all",
                            stylers: {
                                color: "#d1d1d1",
                            },
                        },
                        {
                            featureType: "local",
                            elementType: "all",
                            stylers: {
                                color: "#d1d1d1",
                            },
                        },
                        {
                            featureType: "arterial",
                            elementType: "labels",
                            stylers: {
                                visibility: "off",
                            },
                        },
                        {
                            featureType: "boundary",
                            elementType: "all",
                            stylers: {
                                color: "#fefefe",
                            },
                        },
                        {
                            featureType: "building",
                            elementType: "all",
                            stylers: {
                                color: "#d1d1d1",
                            },
                        },
                        {
                            featureType: "label",
                            elementType: "labels.text.fill",
                            stylers: {
                                color: "#999999",
                            },
                        },
                    ],
                },
            },
            tooltip: {},
            series: [
                {
                    name: "东部",
                    type: "scatter",
                    coordinateSystem: "bmap",
                    data: convertData(eastData, eastCoordMap),
                    encode: { value: 2 },
                    itemStyle: {
                        color: "#2ecc71",
                    },
                    symbolSize: 15,
                    label: {
                        show: false,
                        position: "right",
                        formatter: function(val) {
                            console.log(val)
                            return `${val.data.name} - ${val.data.value[2]}`
                        },
                    },
                },
                {
                    name: "东部Top3",
                    type: "effectScatter",
                    coordinateSystem: "bmap",
                    data: convertData(
                        eastData
                            .sort(function(a, b) {
                                return a.rank - b.rank
                            })
                            .slice(0, 3),
                        eastCoordMap
                    ),
                    symbolSize: 20,
                    encode: {
                        value: 2,
                    },
                    label: {
                        formatter: function(val) {
                            return `${val.data.name} - ${val.data.value[2]}`
                        },
                        position: "right",
                        show: false,
                    },
                    emphasis: {
                        label: {
                            show: true,
                        },
                    },
                    hoverAnimation: true,
                    rippleEffect: {
                        brushType: "stroke",
                        color: "#2ecc71",
                        scale: 3.5,
                    },
                    itemStyle: {
                        color: "#2ecc71",
                        shadowBlur: 10,
                        shadowColor: "#2ecc71",
                    },
                },
                {
                    name: "西部",
                    type: "scatter",
                    coordinateSystem: "bmap",
                    data: convertData(westData, westCoordMap),
                    encode: { value: 2 },
                    itemStyle: {
                        color: "#3498db",
                    },
                    symbolSize: 15,
                    label: {
                        show: false,
                        position: "right",
                        formatter: function(val) {
                            //   console.log(val)
                            return `${val.data.name} - ${val.data.value[2]}`
                        },
                    },
                },
                {
                    name: "西部Top3",
                    type: "effectScatter",
                    coordinateSystem: "bmap",
                    data: convertData(
                        westData
                            .sort(function(a, b) {
                                return a.rank - b.rank
                            })
                            .slice(0, 3),
                        westCoordMap
                    ),
                    symbolSize: 20,
                    encode: {
                        value: 2,
                    },
                    label: {
                        formatter: function(val) {
                            return `${val.data.name} - ${val.data.value[2]}`
                        },
                        position: "right",
                        show: false,
                    },
                    emphasis: {
                        label: {
                            show: true,
                        },
                    },
                    hoverAnimation: true,
                    rippleEffect: {
                        brushType: "stroke",
                        color: "#3498db",
                        scale: 3.5,
                    },
                    itemStyle: {
                        color: "#3498db",
                        shadowBlur: 1,
                        shadowColor: "#3498db",
                    },
                },
            ],
        }
    },
    methods: {
        handleClickGoToDetail(row) {
            this.$router.push("/personaldata/" + row.playerID)
            // console.log(row, column, event)
            // console.log(row.playerID)
        },
        tableCellClassName({ row, column, rowIndex, columnIndex }) {
            //注意这里是解构
            //利用单元格的 className 的回调方法，给行列索引赋值
            row.index = rowIndex
            column.index = columnIndex
        },
        handleClickTeam(row, column) {
            let teamID =
                column.index === 0 ? row.index * 2 + 1 : row.index * 2 + 2
            this.teamID = teamID
            // console.log(this.teamID)
            // console.log(cell)
            // console.log(event)
            teamInfo(teamID).then((data) => {
                console.log(data)
                this.personsTableData = data.personsTableData
                console.log(this.personsTableData)
            })
        },
    },
}
</script>

<style lang="stylus" scoped>
.all-data
    .body
        width 85vw
        margin 0 auto
        .content
            display flex
            justify-content space-between
            .teams
                .title
                    font-size 2rem
                    margin 2rem 1rem
                    color #2c3e50
                .teams-info
                    width 25.3vw
                    height 76.5rem
                    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            .persons
                .title
                    font-size 2rem
                    margin 2rem 1rem
                    color #2c3e50
                .persons-info
                    width 53.6vw
                    height 95rem
                    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        .team-map
            margin 3rem 0
            .title
                font-size 2rem
                margin 2rem 1rem
                color #2c3e50
            .map
                display flex
                justify-content space-between
                .map-card
                    width 70%
</style>

<style lang="stylus">
.el-card
    width 100%
    height 50rem
    .el-card__body
        width 100%
        height 100%
        .echarts
            width 100%
            height 100%
.anchorBL
    display none
.el-table__row
    cursor pointer
</style>
