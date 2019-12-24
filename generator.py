import requests
from bs4 import BeautifulSoup
from string import ascii_uppercase
import random

url = 'https://avto-nomer.ru/kz/informer'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 '
                  'Safari/537.36 '
}

with requests.Session() as session:
    for i in range(1000):
        data = {
            'ctype': '6',
            'digit2': f'{random.randint(0, 999):03}',
            'b1': random.choice(ascii_uppercase),
            'b2': random.choice(ascii_uppercase),
            # 'b3': random.choice(ascii_uppercase),
            'region2': f'{random.randint(0, 17):02}',
            'fon': '2',
            'posted': '1'
        }

        response = session.post(url, data=data, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        image = soup.find('img', class_='img-responsive vcenter')
        image = session.get(image['src'], headers=headers)

        image_name = f"{data['digit2']}{data['b1']}{data['b2']}{data['region2']}.png"

        with open('generated/Двухрядный/' + image_name, 'wb') as file:
            for chunk in image.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f'{i}  -  {image_name}')
