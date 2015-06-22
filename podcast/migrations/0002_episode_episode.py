# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode',
            field=models.CharField(help_text=b'Episode number (optional)', max_length=255, null=True, blank=True),
        ),
    ]
