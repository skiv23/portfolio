# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.contact import models


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Title
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    icon = serializers.CharField(read_only=True)

    class Meta:
        model = models.Contact
        fields = '__all__'


class ContactMeEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactMeEntry
        fields = '__all__'
