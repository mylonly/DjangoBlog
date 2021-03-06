# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.SlugField(max_length=20)),
                ('super_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.SlugField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TagRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Category'),
        ),
        migrations.AddField(
            model_name='tagrelation',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
        ),
        migrations.AddField(
            model_name='tagrelation',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='article.TagRelation', to='article.Tag'),
        ),
    ]
