# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduators', '0007_auto_20170623_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduator',
            name='PersonalDescription',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
