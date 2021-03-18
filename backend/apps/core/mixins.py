# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class SingleModelMixin:
    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise forms.ValidationError(
                _('There can be only 1 %(name)s instance'), params={'name': model.__name__}, code='invalid_quantity'
            )
