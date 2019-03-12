from django.shortcuts import render
from uuid import UUID
import uuid
import json
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sessions.models import Session
# Create your views here.


def home(request):
    return render(request, 'synchro/home.html', context={
        'seconds' : 0,
        'session': 'asdas'
    })