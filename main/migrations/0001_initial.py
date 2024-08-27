# Generated by Django 5.1 on 2024-08-23 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('room_number', models.IntegerField(verbose_name='Room number')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('responsible_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.telegramuser', verbose_name='Responsible user')),
            ],
            options={
                'verbose_name': 'Thing',
                'verbose_name_plural': 'Things',
            },
        ),
    ]
