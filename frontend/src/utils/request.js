import axios from "axios"

const service = axios.create({
    baseURL: "http://10.116.110.182:8000",
    timeout: 10000,
})

service.interceptors.response.use(
    (response) => {
        if (response.status === 200 && response.data) {
            console.log(response.data)
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
