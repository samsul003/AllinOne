# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('currency', models.CharField(default=b'EURO', max_length=50, choices=[(b'EURO', b'Euro'), (b'DOLLAR', b'Dollar'), (b'POUND', b'Pound')])),
                ('category', models.ForeignKey(to='main_app.Category')),
            ],
        ),
    ]
