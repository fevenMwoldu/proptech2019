from rest_framework import serializers
from .models import C2BPayment

class C2BPaymentSerializer(serializers.Serializer):
    class Meta:
        model = C2BPayment
        fields = ['TransactionType','TransID','TransTime','TransAmount','BusinessShortCode','BillRefNumber','InvoiceNumber','OrgAccountBalance','ThirdPartyTransID','MSISDN','FirstName','MiddleName','LastName']
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



       