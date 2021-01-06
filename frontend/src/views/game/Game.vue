<template>
    <div class="game">
        <common-header></common-header>
        <div class="content">
            <div class="title">
                <img src="../../assets/pictures/未来.png" alt="" />
                <h1>NBA 近期赛程</h1>
            </div>
            <div class="time-board">
                <div v-for="(item, index) in data" :key="index" class="time">
                    <div class="date">{{ index }}</div>
                    <div class="info">
                        <el-table
                            :data="item"
                            :row-style="{ height: '8.5rem' }"
                            :row-class-name="tableRowClassName"
                            style="width: 100%; font-size: 2.5rem;"
                        >
                            <el-table-column
                                prop="time"
                                label="时间"
                                width="240"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="state"
                                label="状态"
                                width="240"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="first"
                                label="主队"
                                width="240"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="score"
                                label="比分"
                                width="240"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="second"
                                label="客队"
                                width="240"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"

export default {
    name: "Game",
    components: {
        CommonHeader,
    },
    data() {
        return {
            data: {
                "1-5": [
                    {
                        time: "8:00",
                        state: "已结束",
                        first: "魔术",
                        score: "103:83",
                        second: "骑士",
                    },
                    {
                        time: "8:00",
                        state: "已结束",
                        first: "76人",
                        score: "118:101",
                        second: "黄蜂",
                    },
                    {
                        time: "8:30",
                        state: "已结束",
                        first: "老鹰",
                        score: "108:113",
                        second: "尼克斯",
                    },
                    {
                        time: "8:30",
                        state: "已结束",
                        first: "热火",
                        score: "118:90",
                        second: "雷霆",
                    },
                    {
                        time: "8:30",
                        state: "已结束",
                        first: "猛龙",
                        score: "114:126",
                        second: "凯尔特人",
                    },
                    {
                        time: "9:00",
                        state: "已结束",
                        first: "火箭",
                        score: "100:113",
                        second: "独行侠",
                    },
                    {
                        time: "9:00",
                        state: "已结束",
                        first: "雄鹿",
                        score: "125:115",
                        second: "活塞",
                    },
                    {
                        time: "9:00",
                        state: "已结束",
                        first: "鹈鹕",
                        score: "116:118",
                        second: "步行者",
                    },
                    {
                        time: "11:00",
                        state: "已结束",
                        first: "勇士",
                        score: "137:106",
                        second: "国王",
                    },
                ],
                "1-6": [
                    {
                        time: "8:30",
                        state: "已结束",
                        first: "篮网",
                        score: "130:96",
                        second: "爵士",
                    },
                    {
                        time: "9:00",
                        state: "已结束",
                        first: "灰熊",
                        score: "92:94",
                        second: "湖人",
                    },
                    {
                        time: "10:00",
                        state: "已结束",
                        first: "掘金",
                        score: "123:116",
                        second: "森林狼",
                    },
                    {
                        time: "11:00",
                        state: "已结束",
                        first: "快船",
                        score: "116:113",
                        second: "马刺",
                    },
                    {
                        time: "11:30",
                        state: "已结束",
                        first: "开拓者",
                        score: "111:108",
                        second: "公牛",
                    },
                ],
                "1-7": [
                    {
                        time: "8:00",
                        state: "未开始",
                        first: "步行者",
                        score: "-:-",
                        second: "火箭",
                    },
                    {
                        time: "8:00",
                        state: "未开始",
                        first: "魔术",
                        score: "-:-",
                        second: "骑士",
                    },
                    {
                        time: "8:00",
                        state: "未开始",
                        first: "76人",
                        score: "-:-",
                        second: "奇才",
                    },
                    {
                        time: "8:30",
                        state: "未开始",
                        first: "老鹰",
                        score: "-:-",
                        second: "黄蜂",
                    },
                    {
                        time: "8:30",
                        state: "未开始",
                        first: "热火",
                        score: "-:-",
                        second: "凯尔特人",
                    },
                    {
                        time: "8:30",
                        state: "未开始",
                        first: "尼克斯",
                        score: "-:-",
                        second: "爵士",
                    },
                    {
                        time: "9:00",
                        state: "未开始",
                        first: "雄鹿",
                        score: "-:-",
                        second: "活塞",
                    },
                    {
                        time: "9:00",
                        state: "未开始",
                        first: "鹈鹕",
                        score: "-:-",
                        second: "雷霆",
                    },
                    {
                        time: "10:00",
                        state: "未开始",
                        first: "太阳",
                        score: "-:-",
                        second: "猛龙",
                    },
                    {
                        time: "11:00",
                        state: "未开始",
                        first: "勇士",
                        score: "-:-",
                        second: "快船",
                    },
                    {
                        time: "11:00",
                        state: "未开始",
                        first: "国王",
                        score: "-:-",
                        second: "公牛",
                    },
                ],
            },
        }
    },
    methods: {
        tableRowClassName({ row }) {
            // console.log(row);
            if (row.state === "已结束") {
                return "row-before"
            } else if (row.state === "进行中") {
                return "row-now"
            } else if (row.state === "未开始") {
                return "row-future"
            }
            return ""
        },
    },
}
</script>

<style lang="stylus">
.content
    .title
        display flex
        align-items center
        margin-left 6vw
        img
            height 4rem
        h1
            margin-left 2rem
            font-size 4rem
            color #2c3e50
    .time-board
        margin 0 auto 3rem
        width 86.8vw
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        font-size 2.5rem
        .time
            margin 0 auto
            position relative
            width 100%
            // height 55rem
            padding 3rem
            .date
                margin-left 0rem
                font-size 3rem
                font-weight bold
            .info
                margin 0 auto

.el-table
    .row-before
        background: oldlace;
    .row-now
        background: #F56C6C35
    .row-future
        background: #f0f9eb;
</style>
