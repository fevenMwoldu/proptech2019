from rest_framework import serializers
from .models import Validation

class ValidationSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=200)
    

    def create(self, validated_data):
        return Validation.objects.create(**validated_data)