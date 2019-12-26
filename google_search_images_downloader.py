import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search'  # ?q=nature&tbm=isch
query = 'nature'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 '
                  'Safari/537.36 ',
    'x-client-data': 'CIq2yQEIpLbJAQipncoBCMuuygEIvLDKAQj3tMoBCJm1ygEI7LXKARirpMoB',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}

response = requests.get(url, params={'q': query, 'tbm': 'isch'}, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

a = soup.find_all('a', class_='rg_l')

print(a[0])

#
# image_link = 'https://video.cgtn.com/news/7959544e3059544d34496a4e7a41544d324d7a4e31457a6333566d54/video/d85dde8b721748088feacdfd2cc3551c/d85dde8b721748088feacdfd2cc3551c.jpg'
#
# image = requests.get(image_link, headers=headers)
#
# with open('output.jpg', 'wb') as file:
#     for chunk in image.iter_content(chunk_size=1024):
#         if chunk:
#             file.write(chunk)
