# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


admin.site.register(models.Title)
admin.site.register(models.Contact)
admin.site.register(models.ContactMeEntry)
