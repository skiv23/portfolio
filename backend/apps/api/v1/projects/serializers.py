# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework import serializers

from apps.projects import models

from . import mixins, fields


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectTag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    images = fields.ImageListingField(many=True, read_only=True)
    tags = ProjectTagSerializer(many=True)

    class Meta:
        model = models.Project
        fields = '__all__'


class ProjectListSerializer(mixins.ImageSerializerMixin, serializers.ModelSerializer):
    primary_image_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'primary_image_url',)

    def get_primary_image_url(self, obj):
        return self.build_absolute_image_url(obj.primary_image.original.url)
