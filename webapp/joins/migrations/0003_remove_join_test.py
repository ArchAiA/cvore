# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_join_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='test',
        ),
    ]
