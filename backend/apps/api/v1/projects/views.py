# -*- coding: utf-8 -*-
from rest_framework import viewsets

from apps.projects import models

from . import serializers


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()

    def get_serializer_class(self):
        return serializers.ProjectSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
