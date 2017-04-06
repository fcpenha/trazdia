# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_text', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('origin', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Journal'),
        ),
    ]
