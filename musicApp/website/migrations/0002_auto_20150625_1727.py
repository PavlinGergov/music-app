# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='location',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='singles',
            field=models.SmallIntegerField(default=0),
        ),
    ]
