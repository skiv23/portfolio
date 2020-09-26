# -*- coding: utf-8 -*-
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'about-entries', views.AboutViewSet)
router.register(r'about-info-entries', views.AboutInfoViewSet)
router.register(r'what-i-do-entries', views.WhatIDoViewSet)

urlpatterns = router.urls
