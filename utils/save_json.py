import json

def save_to_json(data, filename):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")