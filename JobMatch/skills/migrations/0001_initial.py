# Generated by Django 2.2.7 on 2019-12-04 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 12, 4, 18, 7, 44, 443831, tzinfo=utc))),
            ],
        ),
    ]