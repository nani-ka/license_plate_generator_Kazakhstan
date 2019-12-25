import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search'  # ?q=nature&tbm=isch
query = 'nature'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 '
                  'Safari/537.36 '
}

response = requests.get(url, params={'q': query, 'tbm': 'isch'}, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

a = soup.find_all('a', class_='rg_l')
print(len(a))
