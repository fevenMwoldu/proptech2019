from rest_framework import serializers
from .models import C2BPayment

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayment
        fields = '__all__'

    def create(self, validated_data):
        return C2BPayment.objects.create(**validated_data)



       