import csv

def save_to_csv(data, filename):
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0: 
                writer.writerow(['Title', 'Link', 'Author', 'Comments'])
            for item in data:
                writer.writerow([item['title'], item['link'], item['author'], item['comments']])
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")