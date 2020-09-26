# -*- coding: utf-8 -*-
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _


class About(models.Model):
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        if len(self.description) >= 20:
            return f'{self.description[:20]}...'
        return self.description

    class Meta:
        verbose_name_plural = _('About Entries')

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise forms.ValidationError(
                _('There can be only 1 %(name)s instance'), params={'name': model.__name__}, code='invalid_quantity'
            )


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
