import requests
from bs4 import BeautifulSoup

def get_data_from_site(base_url, pages, tags):
    data = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print("Ищем элементы по селектору:", tags['item'])

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        if 'item' not in tags:
            print("❌ В конфиге не задан 'item' тег!")
            continue

        items = soup.select(tags['item'])
        print(f"Найдено {len(items)} элементов на странице {page}")

        for item in items:
            title = 'Без имени'
            link = 'Без ссылки'

            title_tags = item.select(tags['title'])
            for tag in title_tags:
                if tag.text.strip():
                    title = tag.get_text(strip=True)
                    link = tag.get('href') if tag.has_attr('href') else 'Без ссылки'
                    break

            phone_tag = item.select_one(tags.get('phone', ''))
            phone = phone_tag.get('href').replace('tel:', '') if phone_tag and phone_tag.has_attr('href') else 'Без телефона'

            data.append({
                'title': title,
                'link': link,
                'phone': phone
            })

    return data

