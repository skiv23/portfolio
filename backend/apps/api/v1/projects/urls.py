# -*- coding: utf-8 -*-
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'', views.ProjectViewSet)

urlpatterns = router.urls
