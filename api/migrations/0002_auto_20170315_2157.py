# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='served_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
    ]
