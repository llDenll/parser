import requests
from bs4 import BeautifulSoup
import json
from time import sleep

for count in range(1, 3):
    sleep(3)

    url = f"https://prom.ua/ua/search?search_term=staff&category=35502&page={count}"
    reponse = requests.get(url)

    soup = BeautifulSoup(reponse.text, "lxml")

    data = soup.find_all(class_='HDvhV js-productad')

    names = []
    for item in data:
        name = item.find(class_='ZnG60').find('span', class_='slpaZ Fg9VN IvV06 h97_n').text
        price = item.find(class_='EbrdH gDvzc').find('div', class_='q9TNF E47cR R8fWE zzQeS qFf0j').find('span',
                                                                                                         class_='slpaZ VPjt6').text.strip() + ' грн '
        img = item.find('a', class_='Lc2U1 M6GLI').find(class_='Gc4mq SZojr').find('img').get('src').strip()

        names.append(
            {
                'name': name,
                'price': price,
                'img': img
            }
        )

    with open('json.json', 'w', encoding='UTF-8') as file:
        json.dump(names, file, indent=4, ensure_ascii=False)
