# Generated by Django 2.2.7 on 2019-11-29 22:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191129_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 22, 8, 21, 60238, tzinfo=utc)),
        ),
    ]
