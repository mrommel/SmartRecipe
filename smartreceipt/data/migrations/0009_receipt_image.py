# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20150426_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/receipts', blank=True),
            preserve_default=True,
        ),
    ]
