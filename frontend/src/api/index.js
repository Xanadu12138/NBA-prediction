import request from "../utils/request"

export function playerInfo(id) {
    return request({
        url: "/api/GetPlayersInfo",
        method: "get",
        params: {
            PlayerID: id,
        },
    })
}

export function teamInfo(id) {
    return request({
        url: "/api/GetTeamsInfo",
        method: "get",
        params: {
            TeamID: id,
        },
    })
}

export function rank() {
    return request({
        url: "/api/GetTopPlayers",
        method: "get",
    })
}

export function prediction(awayTeam, homeTeam) {
    return request({
        url: "/api/Predict",
        method: "get",
        params: {
            AwayTeam: awayTeam,
            HomeTeam: homeTeam,
        },
    })
}
