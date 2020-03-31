from django.utils.decorators import method_decorator
from rest_framework import mixins
from rest_framework import viewsets

from core.models import (App,
                         Key,
                         )
from core.serializers import (AppSerializer,
                              KeySerializer,
                              )
from utils.decorators import response_wrapper


@method_decorator(response_wrapper(), name='dispatch')
class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer


@method_decorator(response_wrapper(), name='dispatch')
class KeyViewSet(viewsets.GenericViewSet,
                 mixins.CreateModelMixin):
    serializer_class = KeySerializer
    queryset = Key.objects.all()
