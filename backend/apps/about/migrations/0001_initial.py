# Generated by Django 3.1.1 on 2020-09-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'About Entries',
            },
        ),
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Name')),
                ('value', models.CharField(max_length=128, verbose_name='Value')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_entries', to='about.about', verbose_name='About')),
                ('url', models.CharField(blank=True, max_length=64, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'About Info Entries',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WhatIDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=64, verbose_name='Icon')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'What I Do Entries',
                'ordering': ['id'],
            },
        ),
    ]
