# Generated by Django 2.1.7 on 2019-03-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synchro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='room_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='connection',
            name='user_id',
            field=models.CharField(max_length=50),
        ),
    ]
