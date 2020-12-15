// 跳到指定路径
// 注意下面的不能写成 箭头函数 因为要使用this
export const goToPath = function(path) {
    this.$router.push(path)
}
