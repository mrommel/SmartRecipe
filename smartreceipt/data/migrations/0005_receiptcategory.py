# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20150421_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('parentReceiptCategory', models.ForeignKey(blank=True, to='data.ReceiptCategory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
