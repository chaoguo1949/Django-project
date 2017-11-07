# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('real_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_short', models.CharField(max_length=100)),
                ('goods_desc', tinymce.models.HTMLField()),
                ('goods_status', models.BooleanField(default=True)),
                ('goods_unit', models.CharField(max_length=20)),
                ('goods_visits', models.IntegerField(default=0)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_cag', models.ForeignKey(to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
