# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins, decorators, response

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

    @decorators.action(methods=['POST'], detail=False, url_path='me')
    def contact_me(self, request):
        serializer = serializers.ContactMeEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data)

    @decorators.action(methods=['GET'], detail=False, url_path='photo')
    def photo(self, request):
        photo = models.Photo.objects.first()
        url = photo.original.url if photo else ''
        return response.Response(data={'url': url})
