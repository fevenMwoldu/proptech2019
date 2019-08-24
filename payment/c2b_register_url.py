import requests

validation_url = "https://darajambili.herokuapp.com/c2b/validation"
confirmtion_url = "https://darajambili.herokuapp.com/c2b/confirmation"


access_token = "ovKz09czX0ivWjxlMfyHwwFgeMu4"

api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

headers = {"Authorization": "Bearer %s" % access_token}

request = { "ShortCode": "601397",
    "ResponseType": "Completed",
    "ConfirmationURL": confirmtion_url,
    "ValidationURL": validation_url}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)