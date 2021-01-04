<template>
    <div class="data-detail">
        <el-row :gutter="30">
            <el-col :span="12">
                <score></score>
            </el-col>
            <el-col :span="12">
                <Time></Time>
            </el-col>
        </el-row>
        <el-row :gutter="30">
            <el-col :span="12">
                <fgpercent></fgpercent>
            </el-col>
            <el-col :span="12">
                <three-p-aver></three-p-aver>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import Score from "./score/Score"
import Time from "./time/Time"
import Fgpercent from "./fgpercent/Fgpercent"
import ThreePAver from "./threepaver/ThreePAver"

export default {
    name: "DataDetail",
    components: {
        Score,
        Time,
        Fgpercent,
        ThreePAver,
    },
}
</script>

<style lang="stylus" scoped>
.data-detail
    padding 0 3rem 3rem 3rem
</style>
<style lang="stylus">
.title-card
    font-size 1.4rem
    margin 2rem 0 1rem 0
.el-col
    padding-bottom 1rem
    margin-bottom 1.5rem
</style>
