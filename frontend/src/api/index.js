import request from "../utils/request"

export function teamInfo() {
    return request({
        url: "/text",
        method: "get",
        params: {
            a: 1,
        },
    })
}

export function playerInfo() {
    return request({
        url: "/text",
        method: "get",
        params: {
            a: 1,
        },
    })
}
