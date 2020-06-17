from rest_framework import serializers
from .models import apidata

class apidataSerializer(serializers.Serializer):
    date = serializers.CharField()
    temperature = serializers.IntegerField()
    humidity = serializers.IntegerField()