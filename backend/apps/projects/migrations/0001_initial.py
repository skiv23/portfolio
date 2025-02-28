# Generated by Django 3.1.1 on 2020-10-05 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(upload_to='', verbose_name='Original')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project', related_name='images')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.ProjectTag', verbose_name='Tags'),
        ),
    ]
