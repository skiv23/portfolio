# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


class AboutInfoStackedInline(admin.StackedInline):
    model = models.AboutInfo


class AboutAdmin(admin.ModelAdmin):
    inlines = [
        AboutInfoStackedInline
    ]


admin.site.register(models.About, AboutAdmin)
admin.site.register(models.AboutInfo)
admin.site.register(models.WhatIDo)
