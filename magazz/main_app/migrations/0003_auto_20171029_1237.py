# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_product_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='prod_img'),
        ),
    ]