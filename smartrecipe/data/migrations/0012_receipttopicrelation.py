# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20150509_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptTopicRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receipt', models.ForeignKey(to='data.Receipt')),
                ('receiptTopic', models.ForeignKey(to='data.ReceiptTopic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
