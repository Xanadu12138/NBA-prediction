from django.shortcuts import render
from django.conf import settings
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import *

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
        teamId = request.GET.get('Id')
        # Get team Object by teamID
        team = get_object_or_404(Teamlist, Id = teamId)
        #players = Pl