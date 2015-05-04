# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_receiptcategoryrelation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='cooktime',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='relaxtime',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='worktime',
        ),
        migrations.AddField(
            model_name='receipt',
            name='portions',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step0',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step1',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step2',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step3',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step4',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step5',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step6',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step7',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step8',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='step9',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='receipt',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
