# Generated by Django 2.2.7 on 2019-12-07 23:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0011_auto_20191207_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 53, 5, 323224, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 23, 53, 5, 323256, tzinfo=utc)),
        ),
    ]