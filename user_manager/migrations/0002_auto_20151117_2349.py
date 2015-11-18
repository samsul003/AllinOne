# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alluser',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
