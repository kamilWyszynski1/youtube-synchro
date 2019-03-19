from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.sessions.models import Session

# Create your models here.

class Group(models.Model):
    group_id = models.CharField(max_length=50, unique=True)


class User(models.Model):
    user_id = models.CharField(max_length=50)
    group = models.ForeignKey(Group, related_name='users', on_delete=models.CASCADE)

