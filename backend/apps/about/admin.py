# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


class AboutInfoStackedInline(admin.StackedInline):
    model = models.AboutInfo


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        AboutInfoStackedInline
    ]


class TimelineEntryStackedInline(admin.StackedInline):
    model = models.TimelineEntry


@admin.register(models.Timeline)
class TimelineAdmin(admin.ModelAdmin):
    inlines = [
        TimelineEntryStackedInline
    ]


admin.site.register(models.AboutInfo)
admin.site.register(models.WhatIDo)
admin.site.register(models.Skill)
