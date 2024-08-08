# Este programa hace una peticion http

import requests

response = requests.get('https://galileoguzman.com/')

print(response.text)
