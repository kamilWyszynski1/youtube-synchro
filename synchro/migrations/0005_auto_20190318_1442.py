# Generated by Django 2.1.7 on 2019-03-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synchro', '0004_auto_20190318_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
