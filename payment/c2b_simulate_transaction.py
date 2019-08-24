import requests

access_token = "fAKtG7n3qBMreIgiWS2UBtddVbCu"

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

headers = {"Authorization": "Bearer %s" % access_token}

request = { "ShortCode":"601397",
"CommandID":"CustomerPayBillOnline",
"Amount":"5",
"Msisdn":"254708374149",
"BillRefNumber":"17258" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)