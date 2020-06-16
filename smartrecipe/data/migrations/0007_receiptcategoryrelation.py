# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_receipt_teaser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptCategoryRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receipt', models.ForeignKey(to='data.Receipt', on_delete=models.CASCADE)),
                ('receiptCategory', models.ForeignKey(to='data.ReceiptCategory', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
