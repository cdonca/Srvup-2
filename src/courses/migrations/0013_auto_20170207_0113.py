# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20170207_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourses',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='owned', to='courses.Course'),
        ),
    ]
