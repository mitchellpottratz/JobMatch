# Generated by Django 2.2.7 on 2019-11-29 22:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0010_auto_20191129_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 22, 24, 44, 356993, tzinfo=utc)),
        ),
    ]