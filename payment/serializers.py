from rest_framework import serializers
from .models import C2BPayment

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayment
        fields = '__all__'
    # TransactionType = serializers.CharField(max_length=20, blank = False)
    # TransID = serializers.CharField(max_length=20, blank = False)
    # TransTime = serializers.DateTimeField(default=datetime.now())
    # TransAmount = serializers.IntegerField()
    # BusinessShortCode = serializers.IntegerField()
    # BillRefNumber = serializers.IntegerField()
    # InvoiceNumber = serializers.IntegerField()
    # OrgAccountBalance = serializers.IntegerField()
    # ThirdPartyTransID = serializers.CharField(max_length=20, blank=True, default=null)
    # MSISDN = serializers.IntegerField()
    # FirstName = serializers.CharField(max_length=20, blank = False)
    # MiddleName = serializers.CharField(max_length=20, blank = False)
    # LastName = serializers.CharField(max_length=20, blank = False)


    def create(self, validated_data):
        return C2BPayment.objects.create(**validated_data)



       