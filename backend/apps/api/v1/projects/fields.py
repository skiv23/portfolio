# -*- coding: utf-8 -*-
from rest_framework import serializers

from . import mixins


class ImageListingField(mixins.ImageSerializerMixin, serializers.RelatedField):
    def to_representation(self, value):
        return self.build_absolute_image_url(value.original.url)
