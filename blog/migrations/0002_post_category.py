# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-30 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogCategory'),
            preserve_default=False,
        ),
    ]