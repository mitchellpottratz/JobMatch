# Generated by Django 2.2.7 on 2019-12-01 19:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_users', '0011_auto_20191129_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, upload_to='company/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 1, 19, 56, 54, 753011, tzinfo=utc)),
        ),
    ]