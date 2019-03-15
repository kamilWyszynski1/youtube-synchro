from django.shortcuts import render, redirect
from django.template import RequestContext

# Create your views here.


def player(request, id):
    request.session['user_id'] = 1
    return render(request, 'synchro/player.html')


def room(request):
    return render(request, 'synchro/room.html', {
        'room_name_json': 'my_room'
    })

def home(request):
    return render(request, 'synchro/home.html')

def createGroup(request):
    return redirect('player/%s' % request.POST['groupname'])