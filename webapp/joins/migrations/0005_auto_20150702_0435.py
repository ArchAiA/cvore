# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_join_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
