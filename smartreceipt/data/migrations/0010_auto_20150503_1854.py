# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_receipt_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 18, 54, 52, 443272, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 18, 54, 56, 340088, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
