from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Group, Game, Match
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'bilaapp/signin.html')

def auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard')
    else:
        return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'bilaapp/signup.html')

def storesignup(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    u = User.objects.create_user(name, email, password)
    u.save()
    return redirect('signin')

@login_required
def dashboard(request):
    group_list = Group.objects.all()
    return render(request, 'bilaapp/dashboard.html', {'group_list': group_list})

# group

@login_required
def creategroup(request):
    # create group form
    return render(request, 'bilaapp/creategroup.html')

@login_required
def storegroup(request):
    group_name = request.POST['name']
    group = Group(name = group_name)
    group.save()
    return redirect('dashboard')

@login_required
def groupdetail(request, group_id):
    group = Group.objects.get(pk=group_id)
    user_list = group.players.all()
    return render(request, 'bilaapp/groupdetail.html',  {'user_list': user_list, 'group_id': group_id})

@login_required
def editgroup(request):
    return HttpResponse("Edit group details. Group's name")

@login_required
def updategroup(request):
    return HttpResponse("Confirm group edition")

@login_required
def destroygroup(request):
    return HttpResponse("Deletes a group")

@login_required
def addplayer(request, group_id):
    group = Group.objects.get(pk=group_id)
    groupname = group.name
    #TODO: FILTRAR OS JOGADORES QUE NÃO PERTENCEM AO GRUPO ATUAL. 
    players = User.objects.all()
    return render(request, 'bilaapp/addplayer.html', {'group_id': group_id, 'group_name': groupname, 'players': players})

@login_required
def storeplayer(request, group_id):
    user = request.POST['user']
    g = Group.objects.get(pk=group_id)
    p = User.objects.get(pk=user)
    g.players.add(p)
    g.save()
    return redirect("groupdetail", g.id)

@login_required
def removeplayer(request, group_id):
    user = request.POST['user_id']
    g = Group.objects.get(pk=group_id)
    p = User.objects.get(pk=user)
    g.players.remove(p)
    return redirect("groupdetail", g.id)

# match

@login_required
def creatematch(request):
    return render(request, 'bilaapp/creatematch.html')

@login_required
def storematch(request):
    game = Game.objects.get(pk=request.POST['game_id'])
    group = Group.objects.get(pk=request.POST['group_id'])
    match = Match(game = game, group = group)
    match.save()
    return redirect('dashboard')

@login_required
def matchdetail(request):
    return HttpResponse("Here you are going to see this match details.")

@login_required
def editmatch(request):
    return HttpResponse("Edit match form")

@login_required
def updatematch(request):
    return HttpResponse("Confirm match edition")

@login_required
def destroymatch(request):
    return HttpResponse("Deletes a match")

# game

@login_required
def gamedetail(request):
    return HttpResponse("Game detail.")

# user

@login_required
def userprofile(request):
    return HttpResponse("User information, scores, most played games, rankings")