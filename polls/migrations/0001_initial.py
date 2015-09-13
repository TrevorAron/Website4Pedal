# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminVal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_on', models.BooleanField(default=True)),
                ('vote_on', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effect_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('votes_on', models.IntegerField(default=0)),
                ('votes_off', models.IntegerField(default=0)),
                ('param_val', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterVal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_value', models.IntegerField(default=0)),
            ],
        ),
    ]
