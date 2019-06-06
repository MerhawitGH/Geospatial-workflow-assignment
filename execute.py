# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) + "\\buffer_distance.xml").read()

wpsServerUrl = "http://130.89.221.193:85/geoserver/ows?"  # Use your SNUMBER

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)