# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_delete', models.BooleanField(default=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pass', models.CharField(max_length=100)),
                ('user_mail', models.CharField(max_length=50)),
                ('user_addr', models.CharField(max_length=50)),
                ('user_tele', models.CharField(max_length=11)),
                ('user_code', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
