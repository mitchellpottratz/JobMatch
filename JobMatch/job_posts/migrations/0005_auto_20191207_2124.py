# Generated by Django 2.2.7 on 2019-12-07 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0004_auto_20191206_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 657154, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 21, 24, 49, 657185, tzinfo=utc)),
        ),
    ]
