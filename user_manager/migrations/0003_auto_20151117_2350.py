# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_auto_20151117_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
