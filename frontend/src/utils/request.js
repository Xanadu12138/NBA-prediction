import axios from "axios"

const service = axios.create({
    baseURL: "http://www.baidu.com",
    timeout: 1000,
})

export default service
