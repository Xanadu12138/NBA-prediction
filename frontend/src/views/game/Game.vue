<template>
    <div class="game">
        <common-header></common-header>
        <div class="content">
            <h1>NBA 未来赛程</h1>
            <div class="time-board">
                <div class="time">
                    <div class="date">12-12</div>
                    <div class="info">
                        <el-table
                            :data="tableData"
                            :row-style="{ height: '8.5rem' }"
                            :row-class-name="tableRowClassName"
                            style="width: 100%; font-size: 2.5rem;"
                        >
                            <el-table-column
                                prop="time"
                                label="时间"
                                width="170"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="state"
                                label="状态"
                                width="200"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="first"
                                label="主队"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="score"
                                label="比分"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="second"
                                label="客队"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="data"
                                label="数据"
                                width="180"
                            >
                            </el-table-column>
                            <el-table-column
                                prop="prediction"
                                label="预测"
                                width="100"
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
            tableData: [
                {
                    time: "8:00",
                    state: "已结束",
                    first: "火箭",
                    score: "99:99",
                    second: "公牛",
                    data: "",
                    prediction: "40%",
                },
                {
                    time: "8:00",
                    state: "已结束",
                    first: "火箭",
                    score: "99:99",
                    second: "公牛",
                    data: "",
                    prediction: "40%",
                },
                {
                    time: "10:00",
                    state: "进行中",
                    first: "火箭",
                    score: "99:99",
                    second: "公牛",
                    data: "",
                    prediction: "40%",
                },
                {
                    time: "12:00",
                    state: "未开始",
                    first: "火箭",
                    score: "99:99",
                    second: "公牛",
                    data: "",
                    prediction: "40%",
                },
                {
                    time: "12:00",
                    state: "未开始",
                    first: "火箭",
                    score: "99:99",
                    second: "公牛",
                    data: "",
                    prediction: "40%",
                },
            ],
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
    h1 
        margin-left 10rem
        font-size 4rem
    .time-board
        font-size 2.5rem
        .time
            margin 0 auto
            position relative
            width 125rem
            height 56rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            padding 3rem
            .date 
                margin-left 2rem
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
