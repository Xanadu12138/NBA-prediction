<template>
    <div class="common-card">
        <div class="title-card">{{ title }}</div>
        <el-tabs type="border-card">
            <el-tab-pane label="折线图">
                <div class="chart">
                    <slot name="line"></slot>
                </div>
            </el-tab-pane>
            <el-tab-pane label="柱状图">
                <div class="chart">
                    <slot name="bar"></slot>
                </div>
            </el-tab-pane>
            <el-tab-pane label="饼状图">
                <div class="chart">
                    <slot name="pie"></slot>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "CommonCard",
    props: {
        title: String,
    },
}
</script>

<style lang="stylus" scoped>
.common-card
    height 35rem
</style>
