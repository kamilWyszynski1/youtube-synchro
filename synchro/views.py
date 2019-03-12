from django.shortcuts import render
from uuid import UUID
import uuid
import json
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sessions.models import Session
# Create your views here.


def home(request):
    request.session['user_id'] = 1
    return render(request, 'synchro/home.html', context={
        'seconds' : 0,
        'session': request.session.get('user_id')
    })

def room(request):
    return render(request, 'synchro/room.html',{
        'room_name_json': 'my_room'
    })