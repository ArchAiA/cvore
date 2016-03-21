# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_remove_join_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=datetime.datetime(2015, 7, 2, 4, 30, 4, 107868, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
