# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180611_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='selected_productss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_pk', models.IntegerField()),
                ('p_pk', models.IntegerField()),
                ('c_pk', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='selected_products',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='branch',
            new_name='phone_no',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='college',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='year',
        ),
    ]
