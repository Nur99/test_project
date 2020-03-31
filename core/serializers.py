from core.models import (App, Key)
from rest_framework import serializers


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('key', )


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'key')
