# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.about.models import Skill


class Project(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    url = models.URLField(verbose_name=_('URL'), blank=True)
    description = models.TextField(verbose_name=_('Description'))
    skills = models.ManyToManyField(Skill, verbose_name=_('Skills'))

    def __str__(self):
        return f'{self.name}'

    @property
    def primary_image(self):
        try:
            return self.images.first()
        except AttributeError:
            return None


class ProjectImage(models.Model):
    original = models.ImageField(verbose_name=_('Original'), upload_to='projects_images')
    project = models.ForeignKey(Project, verbose_name=_('Project'), on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.project)
