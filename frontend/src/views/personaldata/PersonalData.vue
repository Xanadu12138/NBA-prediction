<template>
    <div class="personal-data">
        <common-header></common-header>
        <section class="container">
            <div class="basic">
                <div class="avatar"></div>
                <div class="info">
                    <div class="title">球员信息</div>
                    <div class="data-simple"></div>
                </div>
                <div class="ability">
                    <div class="title">球员能力</div>
                </div>
            </div>
            <div class="data-all">
                <div class="title">数据总览</div>
            </div>
            <div class="data-detail">
                <div class="title">详细数据</div>
            </div>
        </section>
    </div>
</template>

<script>
import CommonHeader from "@/components/header/Header"

export default {
    name: "PersonalData",
    components: {
        CommonHeader
    }
}
</script>

<style lang="stylus" scoped>
.container
    position relative
    width 85vw
    margin 0 auto
    .basic
        display flex
        justify-content space-between
        width 120rem
        height 30rem
        margin 5rem 0
        .avatar 
            width 20rem
            height 20rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        .info 
            width 50rem 
            height 30rem
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            .title
                font-size 2.2rem
        .ability 
            width 30rem 
            height 30rem 
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
            .title
                font-size 2.2rem
    .data-all
        width 120rem
        height 36rem
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        margin 5rem 0
        .title
            font-size 2.2rem
    .data-detail
        width 120rem
        height 52rem
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.5)
        margin 5rem 0
        .title
            font-size 2.2rem

    




</style>
