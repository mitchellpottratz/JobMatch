# Generated by Django 2.2.7 on 2019-12-02 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191202_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company_users.Company'),
        ),
    ]
