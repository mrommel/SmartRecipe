# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_receipttopicrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrient',
            name='important',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
