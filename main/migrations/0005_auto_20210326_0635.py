# Generated by Django 3.1.7 on 2021-03-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210326_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='is_firm',
            field=models.SmallIntegerField(),
        ),
    ]
