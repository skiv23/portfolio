# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework import serializers

from apps.projects import models

from . import mixins, fields


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectTag
        fields = '__all__'


class ProjectSerializer(mixins.ImageSerializerMixin, serializers.ModelSerializer):
    images = fields.ImageListingField(many=True, read_only=True)
    tags = ProjectTagSerializer(many=True)
    primary_image_url = serializers.SerializerMethodField()

    def get_primary_image_url(self, obj):
        return self.build_absolute_image_url(obj.primary_image.original.url)

    class Meta:
        model = models.Project
        fields = '__all__'
