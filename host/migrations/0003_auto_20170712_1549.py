# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0002_auto_20170703_0420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostinfo',
            options={'ordering': ('hostname',), 'permissions': (('host_list', '查看主机列表'), ('edis_host', '编辑主机'), ('create_host', '创建主机'), ('detail_host', '查看主机详情'))},
        ),
    ]
