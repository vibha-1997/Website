# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_selection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='user_cat',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]