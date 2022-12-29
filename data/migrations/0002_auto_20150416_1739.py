# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptIntegrientRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('amount_ytep', models.CharField(max_length=1, choices=[(b'K', b'Kilogramm'), (b'G', b'Gramm'), (b'L', b'Liter'), (b'M', b'Milliliter')])),
                ('integrient', models.ForeignKey(to='data.Integrient', on_delete=models.CASCADE)),
                ('receipt', models.ForeignKey(to='data.Receipt', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='receipt',
            name='description',
            field=models.CharField(max_length=20000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
