# Generated by Django 4.2.5 on 2023-11-20 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='members',
        ),
        migrations.AddField(
            model_name='chat',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member2', to=settings.AUTH_USER_MODEL),
        ),
    ]
