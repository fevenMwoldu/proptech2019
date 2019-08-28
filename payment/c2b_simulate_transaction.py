import requests

access_token = "zXI8pDH2kvDiClIyxf2LURl7EYyi"

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

headers = {"Authorization": "Bearer %s" % access_token}

request = { "ShortCode":"601397",
"CommandID":"CustomerPayBillOnline",
"Amount":"10",
"Msisdn":"254708374149",
"BillRefNumber":"17260" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
