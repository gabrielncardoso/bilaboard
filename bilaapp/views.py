from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Game, Match

def dashboard(request):
    group_list = Group.objects.all()
    return render(request, 'bilaapp/dashboard.html', {'group_list': group_list})

# group

def creategroup(request):
    # create group form
    return render(request, 'bilaapp/creategroup.html')

def storegroup(request):
    group_name = request.POST['name']
    group = Group(name = group_name)
    group.save()
    return redirect('dashboard')

def groupdetail(request, group_id):
    group = Group.objects.get(pk=group_id)
    user_list = group.players.all()
    return HttpResponse(user_list)

def editgroup(request):
    return HttpResponse("Edit group details. Group's name")

def updategroup(request):
    return HttpResponse("Confirm group edition")

def destroygroup(request):
    return HttpResponse("Deletes a group")

def storeplayer(request):
    return HttpResponse("Add player to a group")

def removeplayer(request):
    return HttpResponse("Remove player from a group")

# match

def creatematch(request):
    return render(request, 'bilaapp/creatematch.html')

def storematch(request):
    game = Game.objects.get(pk=request.POST['game_id'])
    group = Group.objects.get(pk=request.POST['group_id'])
    match = Match(game = game, group = group)
    match.save()
    return redirect('dashboard')

def matchdetail(request):
    return HttpResponse("Here you are going to see this match details.")

def editmatch(request):
    return HttpResponse("Edit match form")

def updatematch(request):
    return HttpResponse("Confirm match edition")

def destroymatch(request):
    return HttpResponse("Deletes a match")

# game

def gamedetail(request):
    return HttpResponse("Game detail.")

# user

def userprofile(request):
    return HttpResponse("User information, scores, most played games, rankings")