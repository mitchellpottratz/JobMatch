# Generated by Django 2.2.7 on 2019-12-09 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0013_auto_20191207_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 923933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 923993, tzinfo=utc)),
        ),
    ]
