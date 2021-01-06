<template>
    <div class="three-paver">
        <common-card title="三分命中率">
            <template v-slot:line>
                <vue-echarts :options="getLineOptions()" />
            </template>
            <template v-slot:bar>
                <vue-echarts :options="getBarOptions()" />
            </template>
            <template v-slot:pie>
                <vue-echarts :options="getPieOptions()" />
            </template>
        </common-card>
    </div>
</template>

<script>
import CommonCard from "@/components/commonCard/CommonCard"

export default {
    name: "ThreePAver",
    components: {
        CommonCard,
    },
    inject: ["getTableData"],
    mounted() {
        console.log(this.tableData)
    },
    computed: {
        tableData() {
            // console.log(this.getTableData())
            return this.getTableData()
        },
        season() {
            let res = []
            for (let data of this.tableData) {
                res.push(data.season)
            }
            return res
        },
        pts() {
            let res = []
            for (let data of this.tableData) {
                let threepver = Number(data["3paver"].slice(0, -1))
                res.push(threepver)
            }
            return res
        },
        pieData() {
            let res = []
            for (let data of this.tableData) {
                let threepver = Number(data["3paver"].slice(0, -1))
                res.push({ value: threepver, name: data.season })
            }
            return res
        },
    },
    methods: {
        getLineOptions() {
            return {
                xAxis: {
                    type: "category",
                    data: this.season,
                },
                yAxis: {
                    type: "value",
                },
                series: [
                    {
                        data: this.pts,
                        type: "line",
                    },
                ],
                grid: {
                    top: 10,
                    bottom: 20,
                    left: 35,
                    right: 20,
                },
            }
        },
        getBarOptions() {
            return {
                xAxis: {
                    type: "category",
                    data: this.season,
                },
                yAxis: {
                    type: "value",
                },
                series: [
                    {
                        data: this.pts,
                        type: "bar",
                        showBackground: true,
                        backgroundStyle: {
                            color: "rgba(220, 220, 220, 0.8)",
                        },
                    },
                ],
                grid: {
                    top: 10,
                    bottom: 20,
                    left: 35,
                    right: 20,
                },
            }
        },
        getPieOptions() {
            return {
                tooltip: {
                    trigger: "item",
                    formatter: "{a} <br/>{b}: {c} ({d}%)",
                },
                legend: {
                    orient: "vertical",
                    left: 10,
                    data: this.season,
                },
                series: [
                    {
                        name: "赛季得分",
                        type: "pie",
                        center: ["60%", "50%"],
                        radius: ["60%", "80%"],
                        avoidLabelOverlap: false,
                        label: {
                            show: false,
                            position: "center",
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: "30",
                                fontWeight: "bold",
                            },
                        },
                        labelLine: {
                            show: false,
                        },
                        data: this.pieData,
                    },
                ],
                grid: {
                    top: 10,
                    bottom: 20,
                    left: 55,
                    right: 20,
                },
            }
        },
    },
}
</script>

<style lang="stylus" scoped></style>

<style lang="stylus">
.echarts
    width 50rem
    height 27rem
</style>
