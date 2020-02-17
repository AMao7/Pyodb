import requests

web_page = requests.get('http://bbc.co.uk/')

print(web_page)
print(web_page.cookies)