# -*- coding: utf-8 -*-
from rest_framework import viewsets

from apps.contact import models

from . import serializers


class ContactViewSetMixin:
    def get_queryset(self):
        qs = super().get_queryset()

        type = self.request.query_params.get('type', None)
        if type:
            qs = qs.filter(type=type)

        return qs


class TitleViewSet(ContactViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer


class ContactViewSet(ContactViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        component = self.request.query_params.get('component', None)
        if component:
            qs = qs.filter(**{f'show_in_{component}': True})

        return qs
