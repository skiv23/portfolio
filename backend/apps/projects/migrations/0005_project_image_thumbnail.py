# Generated by Django 3.1.1 on 2021-03-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_delete_projecttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnails', verbose_name='Thumbnail'),
        ),
    ]
