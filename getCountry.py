from requests import get
import requests

ip = get('https://api.ipify.org').text
response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()


def getCountryCode():
    return response['country_code']
