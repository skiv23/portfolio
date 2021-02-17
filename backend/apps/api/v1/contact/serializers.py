# -*- coding: utf-8 -*-
import requests

from django.conf import settings

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
    recaptcha_token = serializers.CharField(write_only=True)

    def validate_recaptcha_token(self, value):
        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': value
            }
        ).json()
        if response.get('error-codes') and not response['success']:
            raise serializers.ValidationError(response.get('error-codes'))

    def create(self, validated_data):
        validated_data.pop('recaptcha_token', None)
        return super().create(validated_data)

    class Meta:
        model = models.ContactMeEntry
        fields = '__all__'
