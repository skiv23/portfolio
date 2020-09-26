# -*- coding: utf-8 -*-
from django.urls import path, include

urlpatterns = [
    path('contact/', include('apps.api.v1.contact.urls')),
    path('about/', include('apps.api.v1.about.urls')),
]
