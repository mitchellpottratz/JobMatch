# Generated by Django 2.2.7 on 2019-12-12 03:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20191209_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 3, 29, 7, 60376, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 3, 29, 7, 60448, tzinfo=utc)),
        ),
    ]
