from django.db import models


# Create your models here.

class Connection(models.Model):
    # class Meta:
    #     unique_together = (('user_id','room_id'),)

    user_id = models.CharField(max_length=50)
    room_id = models.CharField(max_length=50)
