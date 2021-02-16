# Generated by Django 3.1.1 on 2021-02-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TimelineEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('years', models.CharField(max_length=32, verbose_name='Years')),
                ('place', models.CharField(max_length=128, verbose_name='Place')),
                ('description', models.TextField(verbose_name='Description')),
                ('timeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.timeline', verbose_name='Timeline')),
            ],
            options={
                'verbose_name_plural': 'Timeline Entries',
                'ordering': ['id'],
            },
        ),
    ]
