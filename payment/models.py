from django.db import models

# Create your models here.

class Validation(models.Model):
    data = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.data



# {
#     'TransactionType': 'Pay Bill', 
#     'TransID': 'NHP61HABHK',    
#     'TransTime': '20190825023843', 
#     'TransAmount': '5.00', 
#     'BusinessShortCode': '601397', 
#     'BillRefNumber': '17258', 
#     'InvoiceNumber': '', 
#     'OrgAccountBalance': '84832.00', 
#     'ThirdPartyTransID': '', 
#     'MSISDN': '254708374149', 
#     'FirstName': 'John', 
#     'MiddleName': 'J.', 
#     'LastName': 'Doe'
# }        