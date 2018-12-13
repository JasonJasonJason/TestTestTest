import requests

request = requests.get('https://bazaarvoice.com')
request.raise_for_status()

print(request.text)