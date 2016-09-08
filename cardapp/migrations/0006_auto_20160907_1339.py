# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0005_wordstatus_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardstatus',
            name='category',
            field=models.ForeignKey(to='cardapp.CardCategory'),
        ),
        migrations.AlterField(
            model_name='wordstatus',
            name='word',
            field=models.ForeignKey(to='cardapp.Word', null=True),
        ),
    ]
