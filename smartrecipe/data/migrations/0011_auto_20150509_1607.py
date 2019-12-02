# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20150503_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('parentReceiptTopic', models.ForeignKey(blank=True, to='data.ReceiptTopic', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='receiptintegrientrelation',
            name='amount_type',
            field=models.CharField(max_length=1, choices=[(b'K', b'Kilogramm'), (b'G', b'Gramm'), (b'L', b'Liter'), (b'M', b'Milliliter'), (b'T', b'TL'), (b'S', b'St\xc3\xbcck'), (b'B', b'Becher')]),
            preserve_default=True,
        ),
    ]
