from django.urls import path
from rest_framework import routers

from core import views


router = routers.DefaultRouter()
router.register(r'apps', views.AppViewSet, base_name='apps')
router.register(r'keys', views.KeyViewSet, base_name='keys')

urlpatterns = router.urls
