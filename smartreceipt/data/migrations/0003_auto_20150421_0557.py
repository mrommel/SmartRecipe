# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150416_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='calories',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='cooktime',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='relaxtime',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='worktime',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='receiptintegrientrelation',
            name='amount_ytep',
            field=models.CharField(max_length=1, choices=[(b'K', b'Kilogramm'), (b'G', b'Gramm'), (b'L', b'Liter'), (b'M', b'Milliliter'), (b'T', b'TL')]),
            preserve_default=True,
        ),
    ]
