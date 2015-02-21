# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollingDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('council_id', models.CharField(max_length=100, null=True, blank=True)),
                ('extra_id', models.CharField(max_length=100, null=True, blank=True)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollingStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postcode', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
