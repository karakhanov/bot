# Generated by Django 3.1.7 on 2021-03-29 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210329_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
