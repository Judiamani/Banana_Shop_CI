# Generated by Django 2.2.6 on 2020-01-05 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitedesvins', '0003_auto_20200105_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='dat',
        ),
    ]