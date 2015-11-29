# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_integrient_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptintegrientrelation',
            name='amount_type',
            field=models.CharField(max_length=1, choices=[(b'K', b'Kilogramm'), (b'G', b'Gramm'), (b'L', b'Liter'), (b'M', b'Milliliter'), (b'T', b'TL'), (b'E', b'EL'), (b'S', b'St\xc3\xbcck'), (b'B', b'Becher'), (b'P', b'Prise'), (b'C', b'P\xc3\xa4ckchen'), (b'F', b'Flasche')]),
            preserve_default=True,
        ),
    ]
