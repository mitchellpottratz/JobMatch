# Generated by Django 2.2.7 on 2019-11-29 21:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0002_auto_20191129_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 21, 48, 49, 754590, tzinfo=utc)),
        ),
    ]