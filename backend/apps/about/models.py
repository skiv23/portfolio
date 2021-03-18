# -*- coding: utf-8 -*-
from django import forms
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.mixins import SingleModelMixin


class About(SingleModelMixin, models.Model):
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        if len(self.description) >= 20:
            return f'{self.description[:20]}...'
        return self.description

    class Meta:
        verbose_name_plural = _('About Entries')


class AboutInfo(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='info_entries', verbose_name=_('About'))
    title = models.CharField(max_length=32, verbose_name=_('Name'))
    value = models.CharField(max_length=128, verbose_name=_('Value'))
    url = models.CharField(max_length=64, blank=True, verbose_name=_('URL'))

    def __str__(self):
        return f'{str(self.about)} - {self.title}: {self.value}'

    class Meta:
        verbose_name_plural = _('About Info Entries')
        ordering = ['id']


class WhatIDo(models.Model):
    icon = models.CharField(max_length=64, verbose_name=_('Icon'), blank=True)
    name = models.CharField(max_length=32, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = _('What I Do Entries')
        ordering = ['id']


class Skill(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    percent = models.PositiveSmallIntegerField(
        verbose_name=_('Percent'), blank=True, null=True,
        validators=[validators.MaxValueValidator(100)]
    )
    is_secondary = models.BooleanField(default=False, verbose_name=_('Is Secondary'))

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def clean(self):
        if not self.is_secondary and self.percent is None:
            raise forms.ValidationError(_('Percent should be set for main skills!'))


class Timeline(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('Name'))

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class TimelineEntry(models.Model):
    timeline = models.ForeignKey(Timeline, verbose_name=_('Timeline'), on_delete=models.CASCADE, related_name='entries')
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    years = models.CharField(max_length=32, verbose_name=_('Years'))
    place = models.CharField(max_length=128, verbose_name=_('Place'))
    description = models.TextField(verbose_name=_('Description'))

    class Meta:
        verbose_name_plural = _('Timeline Entries')
        ordering = ['id']

    def __str__(self):
        return f'{self.name} for {self.timeline.name}'
