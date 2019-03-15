from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages


# Create your views here.


def player(request, id):
    return render(request, 'synchro/player.html')


def room(request):
    return render(request, 'synchro/room.html', {'room_name_json': 'my_room'})


def home(request):
    return render(request, 'synchro/home.html')


def createGroup(request):
    messages.add_message(request, messages.INFO, request.POST['username'])
    return HttpResponseRedirect('player/%s' % request.POST['groupname'])
