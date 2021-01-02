import request from "../utils/request"

export function test() {
    return request({
        url: "/text",
        method: "get",
        params: {
            a: 1,
        },
    })
}
