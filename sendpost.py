import requests

url = 'http://localhost:3000'
files = {'file': open('hello.png')}
response = requests.post(url, files=files)