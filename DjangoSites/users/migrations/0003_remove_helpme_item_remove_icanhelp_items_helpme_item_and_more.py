# Generated by Django 4.2.5 on 2023-11-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_science'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpme',
            name='item',
        ),
        migrations.RemoveField(
            model_name='icanhelp',
            name='items',
        ),
        migrations.AddField(
            model_name='helpme',
            name='item',
            field=models.ManyToManyField(to='users.science'),
        ),
        migrations.AddField(
            model_name='icanhelp',
            name='items',
            field=models.ManyToManyField(to='users.science'),
        ),
    ]
