# Generated by Django 2.1.7 on 2019-03-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synchro', '0005_auto_20190318_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]