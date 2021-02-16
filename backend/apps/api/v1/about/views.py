# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import response


from apps.about import models

from . import serializers


class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

    def list(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return response.Response(serializer.data)

    def get_object(self):
        return self.filter_queryset(self.get_queryset()).first()


class AboutInfoViewSet(viewsets.ModelViewSet):
    queryset = models.AboutInfo.objects.all()
    serializer_class = serializers.AboutInfoSerializer


class WhatIDoViewSet(viewsets.ModelViewSet):
    queryset = models.WhatIDo.objects.all()
    serializer_class = serializers.WhatIDoSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = models.Timeline.objects.all()
    serializer_class = serializers.TimelineSerializer
