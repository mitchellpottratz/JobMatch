# Generated by Django 2.2.7 on 2019-12-09 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0012_auto_20191208_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 956681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 5, 43, 23, 956747, tzinfo=utc)),
        ),
    ]
