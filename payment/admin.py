from django.contrib import admin

# Register your models here.
from .models import C2BPayment

class C2BPaymentAdmin(admin.ModelAdmin):
    list_display = ["MSISDN", "TransID", "TransTime", "TransAmount", "BillRefNumber", "FirstName", "MiddleName", "LastName"]

admin.site.register(C2BPayment, C2BPaymentAdmin)

