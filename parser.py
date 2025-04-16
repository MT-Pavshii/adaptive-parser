import requests
from bs4 import BeautifulSoup

def get_data_from_site(base_url, pages, tags):
    data = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print("Ищем элементы по селектору:", tags.get('item'))

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
            result = {}

            title_tag = item.select_one(tags.get('title', ''))
            if title_tag:
                result['title'] = title_tag.get_text(strip=True)
                result['link'] = title_tag.get('href', 'Без ссылки') if title_tag.has_attr('href') else 'Без ссылки'
            else:
                result['title'] = 'Без имени'
                result['link'] = 'Без ссылки'

            for key, selector in tags.items():
                if key in ['item', 'title']:
                    continue  

                tag = item.select_one(selector) # Блок для добовления специальных условий
                if tag:
                    if key == 'phone' and tag.has_attr('href'):
                        result[key] = tag.get('href').replace('tel:', '')
                    else:
                        result[key] = tag.get_text(strip=True)
                else:
                    result[key] = f"Без {key}"

            data.append(result)

    return data


