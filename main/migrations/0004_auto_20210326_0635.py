# Generated by Django 3.1.7 on 2021-03-26 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_usertelegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('telegram_user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('is_firm', models.SmallIntegerField(max_length=1)),
                ('country', models.CharField(max_length=20)),
                ('state', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='temp',
        ),
        migrations.RemoveField(
            model_name='usertelegram',
            name='id',
        ),
        migrations.AddField(
            model_name='usertelegram',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='id_telegram',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]