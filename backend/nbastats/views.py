from django.shortcuts import render
from django.conf import settings
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

def GetAllTeams(request):
    if request.method == 'GET':
        teams = Teamlist.objects.all()
        resList = []
        for team in teams:
            teamDict = {}
            teamDict[team.tm] = team.Id 

            resList.append(teamDict)

        data = resList
        response = {'data':data}
        return JsonResponse(response)


def GetTeamsInfo(request):
    if request.method == 'GET':
        teamId = request.GET.get('TeamID')
        # Get team Object by teamID
        team = get_object_or_404(Teamlist, Id = teamId)
        players = Playersinfo.objects.filter(tm = team)
        dataList = []
        for player in players:
            playerDict = {}
            # Get stats by player 
            playerStats = Player.objects.filter(playerId = player, season = '2020')
            # Get last season stats
            if len(playerStats) > 0:
                playerStat = playerStats[0]
                playerDict['name'] = playerStat.name
                playerDict['playerID'] = playerStat.playerId.Id
                playerDict['score'] = playerStat.pts
                playerDict['board'] = playerStat.trb
                playerDict['assist'] = playerStat.ast 
                playerDict['steal'] = playerStat.stl
                playerDict['blockshots'] = playerStat.blk
                dataList.append(playerDict)

    response = {'personsTableData': dataList}
    return JsonResponse(response)


def GetPlayersInfo(request):
    if request.method == 'GET':
        playerId = request.GET.get('PlayerID')
        # Get Player object by playerID
        player = get_object_or_404(Playersinfo,Id = playerId)
        # Get players' stats by player
        stats = Player.objects.filter(playerId = player)
        # player data dict
        dataDict = {}
        dataDict['name'] = player.name
        dataDict['num'] = player.num
        dataDict['pos'] = player.pos
        dataDict['tall'] = player.tall 
        dataDict['wei'] = player.wei 
        dataDict['bri'] = player.bri
        # tm = player.tm
        dataDict['con'] = player.con 
        dataDict['img'] = player.img 

        # player stats season list
        statslist = []
        for stat in stats:
            statDict = {}
            statDict['season'] = stat.season
            statDict['pts'] = stat.pts
            statDict['tm'] = stat.tm
            statDict['g'] = stat.g
            statDict['gs'] = stat.gs
            statDict['mp'] = stat.mp
            statDict['fga'] = stat.fga
            statDict['fgaver'] = stat.fgaver
            statDict['3pa'] = stat.threepa
            statDict['3paver'] = stat.threepaver
            statDict['fta'] = stat.fta
            statDict['ftaver'] = stat.ftaver
            statDict['trb'] = stat.trb
            statDict['ast'] = stat.ast
            statDict['stl'] = stat.stl
            statDict['blk'] = stat.blk
            statDict['tov'] = stat.tov
            statDict['pf'] = stat.pf
            statslist.append(statDict)
            
        response = {'basicData':dataDict,'tableData': statslist}
        
        return JsonResponse(response)

def GetTopPlayers(request):
    if request.method == 'GET':
        season = '2019'
        # Get stats by season

        # List of 5 top3 stats
        statsNames = ['pts', 'trb', 'ast', 'stl', 'blk']
        statList = []
        toppts = Player.objects.filter(season = season).order_by('-pts')
        toptrb = Player.objects.filter(season = season).order_by('-trb')
        topast = Player.objects.filter(season = season).order_by('-ast')
        topstl = Player.objects.filter(season = season).order_by('-stl')
        topblk = Player.objects.filter(season = season).order_by('-blk')

        statList.append(toppts[:3])
        statList.append(toptrb[:3])
        statList.append(topast[:3])
        statList.append(topstl[:3])
        statList.append(topblk[:3])

        respList = []
        for statName, stats in zip(statsNames, statList):
            statDict = {}
            statDict['title'] = statName
            for rank, stat in enumerate(stats):
                statDict['no' + str(rank + 1)] = stat.name
                exec("statDict['no' + str(rank + 1) + 'score'] = stat.{}".format(statName))

            respList.append(statDict)

        response = {'data':respList}
        
        return JsonResponse(response)



            