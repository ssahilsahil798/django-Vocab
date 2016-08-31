# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0002_learntwords'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='learntwords',
            unique_together=set([('user', 'word')]),
        ),
    ]
