# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('action_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='login.User')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokee', to='login.User')),
            ],
        ),
    ]