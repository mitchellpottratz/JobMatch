# Generated by Django 2.2.7 on 2019-12-07 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0008_auto_20191207_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 48, 10, 772228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 48, 10, 772260, tzinfo=utc)),
        ),
    ]