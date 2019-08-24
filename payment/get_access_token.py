import requests
from requests.auth import HTTPBasicAuth

consumer_key = "SXqCXJWqyIcwYJCujvkzOi0XUg2gvcRm"
consumer_secret = "As1qTDGImwZqtfD4"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r.text)