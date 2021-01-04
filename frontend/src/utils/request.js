import axios from "axios"

const service = axios.create({
    baseURL: "http://www.baidu.com",
    timeout: 1000,
})

service.interceptors.response.use(
    (response) => {
        console.log(response)
        if (response.status === 200 && response.data) {
            return response.data
        } else {
            return Promise.reject(new Error("请求失败"))
        }
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default service
