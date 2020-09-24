# -*- coding: utf-8 -*-
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'titles', views.TitleViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = router.urls
