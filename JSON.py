import json
import requests

response = requests.get("http://api.postcodes.io/postcodes/se83pa")     # requests data from url

# print(response.status_code)
# print(response.headers)
my_reponse = response.json()
# print(response
print(response.json())
print(f"my nuts: {my_reponse['result']['codes']['nuts']}")



# aws - kuberenets - cka
# accekerate