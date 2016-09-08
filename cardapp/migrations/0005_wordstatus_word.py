# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0004_cardstatus_wordstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordstatus',
            name='word',
            field=models.OneToOneField(null=True, to='cardapp.Word'),
        ),
    ]
