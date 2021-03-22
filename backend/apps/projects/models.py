# -*- coding: utf-8 -*-
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.about.models import Skill

from .thumbnail import Thumbnail


class Project(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    url = models.URLField(verbose_name=_('URL'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    skills = models.ManyToManyField(Skill, verbose_name=_('Skills'))
    image_thumbnail = models.ImageField(verbose_name=_('Thumbnail'), blank=True, upload_to='thumbnails')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'

    def create_primary_image_thumbnail(self):
        primary_image = self.primary_image
        if primary_image:
            image_generator = Thumbnail(source=primary_image.original)
            result = image_generator.generate()
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(result.read())
            self.image_thumbnail.save(
                primary_image.original.name.split('/')[-1], File(img_temp)
            )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image_thumbnail:
            self.create_primary_image_thumbnail()

    @property
    def primary_image(self):
        return self.images.first()


class ProjectImage(models.Model):
    original = models.ImageField(verbose_name=_('Original'), upload_to='projects_images')
    project = models.ForeignKey(Project, verbose_name=_('Project'), on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.project)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.project.image_thumbnail:
            self.project.create_primary_image_thumbnail()
