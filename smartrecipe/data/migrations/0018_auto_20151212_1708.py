# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_receiptcategory_is_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receipt',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='integrient',
            name='plural',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receiptintegrientrelation',
            name='amount_type',
            field=models.CharField(choices=[(b'K', b'Kilogramm'), (b'G', b'Gramm'), (b'L', b'Liter'), (b'M', b'Milliliter'), (b'T', b'TL'), (b'E', b'EL'), (b'S', b'St\xc3\xbcck'), (b'B', b'Becher'), (b'P', b'Prise(n)'), (b'C', b'P\xc3\xa4ckchen'), (b'F', b'Flasche(n)'), (b'N', b'Scheibe(n)'), (b'W', b'Etwas'), (b'D', b'Dose'), (b'X', b'Glas')], max_length=1),
        ),
    ]
