# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


class ProjectImageInline(admin.StackedInline):
    model = models.ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


admin.site.register(models.ProjectImage)
admin.site.register(models.ProjectTag)
admin.site.register(models.Project, ProjectAdmin)
