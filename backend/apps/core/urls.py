# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path

from . import views

urlpatterns = []
if not settings.DEBUG:
    urlpatterns.append(path('', views.IndexView.as_view(), name='index'))
