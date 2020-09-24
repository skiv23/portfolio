# -*- coding: utf-8 -*-
import json

from django.db import models


class BaseContactModel(models.Model):
    text = models.CharField(max_length=64)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.text} ({self.get_type_display()})'


class Title(BaseContactModel):
    NAME = 1
    ROLE = 2
    TECH_STACK = 3
    TYPES = (
        (NAME, 'Name'),
        (ROLE, 'Role'),
        (TECH_STACK, 'Tech Stack'),
    )
    type = models.PositiveSmallIntegerField(unique=True, choices=TYPES)


class Contact(BaseContactModel):
    LOCATION = 1
    LINKEDIN = 2
    MAIL = 3
    TELEGRAM = 4
    TYPES = (
        (LOCATION, 'Location'),
        (LINKEDIN, 'LinkedIn'),
        (MAIL, 'Mail'),
        (TELEGRAM, 'Telegram'),
    )
    type = models.PositiveSmallIntegerField(unique=True, choices=TYPES)
    url = models.CharField(max_length=64, blank=True)

    show_in_sidebar = models.BooleanField(default=False)
    show_in_contact = models.BooleanField(default=False)

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


