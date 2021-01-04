<template>
    <div class="prediction">
        <common-header></common-header>
        <section class="container">
            <h2 class="info">说明：本预测基于xxxxxxxxx</h2>
            <div class="res">
                <h1 class="title">预测结果</h1>
                <div class="content">
                    <el-table
                        :data="tableData"
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
            tableData: [
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
        }
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
    .res
        width 124rem
        // height 28rem
        .title
            font-size 4rem
        .content
            // height 18rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
    .custom
        width 105rem
        .title
            font-size 4rem
        .content
            height 18rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
</style>
