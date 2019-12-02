# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150421_0557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptintegrientrelation',
            old_name='amount_ytep',
            new_name='amount_type',
        ),
    ]
