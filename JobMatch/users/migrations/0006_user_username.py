# Generated by Django 2.2.7 on 2019-11-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191129_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=155, unique=True),
        ),
    ]
