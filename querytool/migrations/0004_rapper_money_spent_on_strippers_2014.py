# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-30 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querytool', '0003_album_nightclub_rapper'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapper',
            name='money_spent_on_strippers_2014',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]