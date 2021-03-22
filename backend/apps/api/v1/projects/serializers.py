# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.api.v1.about.serializers import SkillSerializer
from apps.projects import models

from . import mixins, fields


class ProjectSerializer(mixins.ImageSerializerMixin, serializers.ModelSerializer):
    images = fields.ImageListingField(many=True, read_only=True)
    skills = SkillSerializer(many=True)
    primary_image_url = serializers.SerializerMethodField()
    thumbnail_image_url = serializers.SerializerMethodField()

    def get_thumbnail_image_url(self, obj):
        if obj.image_thumbnail:
            return self.build_absolute_image_url(obj.image_thumbnail.url)
        return ''

    def get_primary_image_url(self, obj):
        if obj.primary_image:
            return self.build_absolute_image_url(obj.primary_image.original.url)
        return ''

    class Meta:
        model = models.Project
        fields = '__all__'
