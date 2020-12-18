<template>
    <div class="all-data">
        <common-header></common-header>
        <section class="content">
            <div class="teams">
                <h1 class="title">队伍信息</h1>
                <div class="teams-info">
                    <el-table
                        class="team-table"
                        :data="teamsTableData"
                        stripe
                        style="width: 100%"
                    >
                        <el-table-column prop="east" label="东部" width="180">
                        </el-table-column>
                        <el-table-column prop="west" label="西部" width="180">
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
                        <el-table-column prop="name" label="姓名" width="180">
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
                            prop="blockShot"
                            label="场均盖帽"
                            width="180"
                        >
                        </el-table-column>
                    </el-table>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"

export default {
    name: "AllData",
    components: {
        CommonHeader,
    },
    data() {
        return {
            teamsTableData: [
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
                {
                    east: "雄鹿",
                    west: "公牛",
                },
            ],
            personsTableData: [
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
                {
                    name: "阿尔德里奇",
                    score: "18.9",
                    board: "7.4",
                    assist: "2.4",
                    steal: "0.7",
                    blockShot: "1.6",
                },
            ],
        }
    },
    methods: {
        handleClickGoToDetail(row, column, event) {
            this.$router.push("/personaldata")
            console.log(row, column, event)
        },
    },
}
</script>

<style lang="stylus" scoped>
.all-data
    .content
        display flex
        justify-content space-around
        margin 0 3rem 3rem
        .teams
            .title
                font-size 2rem
                margin 2rem 1rem
            .teams-info
                width 37rem
                height 76.5rem
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        .persons
            .title
                font-size 2rem
                margin 2rem 1rem
            .persons-info
                width 87.2rem
                height 95rem
                box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
</style>
