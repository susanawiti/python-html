# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-09 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='description',
            field=models.CharField(default='DEFAULT VALUE', max_length=45),
        ),
        migrations.AddField(
            model_name='family',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
