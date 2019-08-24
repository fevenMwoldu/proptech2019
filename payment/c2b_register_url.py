import requests

validation_url = "https://proptech2018.herokuapp.com/api/c2b/validation/" 
#"https://darajambili.herokuapp.com/c2b/validation"
confirmtion_url = "https://proptech2018.herokuapp.com/api/c2b/confirmation/" 
#"https://darajambili.herokuapp.com/c2b/confirmation"


access_token = "fAKtG7n3qBMreIgiWS2UBtddVbCu"

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

headers = {"Authorization": "Bearer %s" % access_token}

request = { "ShortCode": "601397",
    "ResponseType": "Completed",
    "ConfirmationURL": confirmtion_url,
    "ValidationURL": validation_url}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)