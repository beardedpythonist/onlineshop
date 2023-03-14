# Generated by Django 4.1.7 on 2023-03-14 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parts',
            name='slug',
        ),
        migrations.AddField(
            model_name='parts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
