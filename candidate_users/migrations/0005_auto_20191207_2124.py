# Generated by Django 2.2.7 on 2019-12-07 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_users', '0004_auto_20191206_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 653276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 653302, tzinfo=utc)),
        ),
    ]