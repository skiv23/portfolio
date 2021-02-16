# -*- coding: utf-8 -*-
import json

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseContactModel(models.Model):
    text = models.CharField(max_length=64, verbose_name=_('Text'))

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.text} ({self.get_type_display()})'


class Title(BaseContactModel):
    NAME = 1
    ROLE = 2
    TECH_STACK = 3
    TYPES = (
        (NAME, _('Name')),
        (ROLE, _('Role')),
        (TECH_STACK, _('Tech Stack')),
    )
    type = models.PositiveSmallIntegerField(unique=True, choices=TYPES, verbose_name=_('Type'))


class Contact(BaseContactModel):
    LOCATION = 1
    LINKEDIN = 2
    MAIL = 3
    TELEGRAM = 4
    TYPES = (
        (LOCATION, _('Location')),
        (LINKEDIN, _('LinkedIn')),
        (MAIL, _('Mail')),
        (TELEGRAM, _('Telegram')),
    )
    type = models.PositiveSmallIntegerField(unique=True, choices=TYPES, verbose_name=_('Type'))
    url = models.CharField(max_length=64, blank=True, verbose_name=_('URL'))

    show_in_sidebar = models.BooleanField(default=False, verbose_name=_('Show in Sidebar'))
    show_in_contact = models.BooleanField(default=False, verbose_name=_('Show in Contact'))

    @property
    def icon(self):
        return json.dumps({
            self.LOCATION: ['fas', 'map-marker-alt'],
            self.LINKEDIN: ['fab', 'linkedin-in'],
            self.MAIL: ['fas', 'envelope'],
            self.TELEGRAM: ['fas', 'paper-plane'],
        }.get(self.type, ['fas', 'question']))

    class Meta:
        ordering = ['type']


class ContactMeEntry(models.Model):
    full_name = models.CharField(max_length=128, verbose_name=_('Full name'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=128, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name_plural = _('Contact me entries')
        ordering = ['id']

    def __str__(self):
        return f'{self.subject} from {self.full_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            pass  # TODO: send message to Telegram
        super().save(*args, **kwargs)
