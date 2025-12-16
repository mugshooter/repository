import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

response = requests.get('http://wttr.in/Moscow', headers=headers)
soup = BeautifulSoup(response.text, 'htmp.parser')

print(soup.pre.text)