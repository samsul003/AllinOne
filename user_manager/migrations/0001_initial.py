# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.CharField(unique=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
