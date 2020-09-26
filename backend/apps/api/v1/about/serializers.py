# -*- coding: utf-8 -*-
from django.utils import timezone

from rest_framework import serializers

from apps.about import models


class AboutInfoSerializer(serializers.ModelSerializer):
    value_display = serializers.SerializerMethodField()

    def get_value_display(self, obj):
        if obj.title.lower() == 'age' and len(obj.value) == 4:
            try:
                return timezone.localtime().year - int(obj.value)
            except ValueError:
                pass
        elif obj.url:
            return f'<a href={obj.url}>{obj.value}</a>'
        return obj.value

    class Meta:
        model = models.AboutInfo
        exclude = ('about',)


class AboutSerializer(serializers.ModelSerializer):
    info_entries = AboutInfoSerializer(many=True, read_only=True)

    class Meta:
        model = models.About
        fields = '__all__'


class WhatIDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WhatIDo
        fields = '__all__'
