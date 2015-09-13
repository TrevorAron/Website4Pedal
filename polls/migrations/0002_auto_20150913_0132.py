# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminVal',
        ),
        migrations.DeleteModel(
            name='TwitterVal',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='votes_off',
        ),
        migrations.RemoveField(
            model_name='effect',
            name='votes_on',
        ),
    ]
