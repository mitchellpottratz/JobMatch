# Generated by Django 2.2.7 on 2019-12-02 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_company_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_account',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='company_users.Company'),
        ),
    ]