# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-02 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='cpu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='deviceclass',
            field=models.CharField(default='11', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='mem',
            field=models.CharField(default='dd', max_length=30),
            preserve_default=False,
        ),
    ]
