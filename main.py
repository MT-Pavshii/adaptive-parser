import json
from parser import get_data_from_site
from utils.save_csv import save_to_csv
from utils.save_json import save_to_json

def load_config(): 
    with open('Adaptive parser/config/website.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    config = load_config()
    
    all_data = []
    
    for site_name, site_config in config.items():
        print(f"Парсинг сайта: {site_name}")
        data = get_data_from_site(
            base_url=site_config['base_url'],
            pages=site_config['pages'],
            tags=site_config['tags']
        )
        all_data.extend(data)
    
    save_to_csv(all_data, 'Adaptive parser/data/output.csv')
    save_to_json(all_data, 'Adaptive parser/data/output.json')
    print("Парсинг завершен. Данные сохранены.")

if __name__ == '__main__':
    main()