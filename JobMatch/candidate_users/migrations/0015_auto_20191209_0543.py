# Generated by Django 2.2.7 on 2019-12-09 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_users', '0014_auto_20191207_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 912163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 912199, tzinfo=utc)),
        ),
    ]