# Generated by Django 2.2.7 on 2019-12-07 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 661253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 661278, tzinfo=utc)),
        ),
    ]
