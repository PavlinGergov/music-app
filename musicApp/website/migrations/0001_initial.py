# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateField()),
                ('location', models.CharField(max_length=32)),
                ('albums', models.SmallIntegerField()),
                ('singles', models.SmallIntegerField()),
            ],
        ),
    ]
