# Адаптивный парсер для сбора данных с веб-сайтов

Этот проект представляет собой адаптивный парсер для сбора информации с различных веб-сайтов. На данный момент парсер проверен на примере медицинского сайта, который предоставляет информацию о врачах, но он легко может быть адаптирован для работы с другими сайтами.

## Описание

Парсер предназначен для извлечения контактной информации с сайтов. Он получает данные по параметрам, указанным в конфигурационном файле, и возвращает результаты в удобном для дальнейшей обработки виде (например, в формате JSON).

Основная цель парсера — собрать список врачей с их именами, телефонами и ссылками на страницы. Парсер является адаптивным, что позволяет легко изменять конфигурацию для работы с различными сайтами.

## Структура проекта

Проект имеет следующую структуру:

- **config.json** — содержит настройки парсера, такие как URL сайта, количество страниц для парсинга и CSS-селекторы для поиска элементов.
- **main.py** — основной исполнимый файл, который выполняет парсинг и сохраняет результаты.
- **README.md** — документация проекта.
- **requirements.txt** — файл с зависимостями, которые необходимо установить для корректной работы проекта.
- **utils.py** — файл с утилитами для обработки и улучшения работы парсера (если нужно).

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
2. Установите зависимость
pip install -r requirements.txt
Убедитесь, что используете Python 3.7+

## Использование

1. Откройте файл `config.json` и укажите необходимые параметры парсинга. Пример приведён ниже.
2. Запустите основной файл:
python main.py
3. Результат сохраняется сразу в двух форматах json и csv внутри папки utils.

## Конфигурация

Файл config.json позволяет адаптиролвать любой сайт без динамического обновления. изменяя только селекторы и URL. 
Имеется возможность добавления нескольких источников для парсинга

Пример:
{
    "quotes": {
        "base_url": "https://www.mosmedportal.ru/doctors/?PAGEN_1=",
        "pages": 5,
        "tags": {
            "item": "div.doctor-card--middle",
            "title": "a.doctor-card--name",
            "phone": "a.phone-link"
        }
    }
} 

На данный момент парсер настроен на сайт врачей для проверки его работы. 

## Описание параметров 

1. base_url: URL-адрес без номера страницы.

2. pages: Количество страниц для парсинга.

3. tags:

4. item: CSS-селектор для контейнера каждого элемента.

5. title: Селектор для заголовка или имени.

6. phone: Селектор для номера телефона.

Так же можно добавлять свои селектора в tags таким образом расширить ифнормацию.

## Пример вывода 

После завершения работы парсера, результат будет записан в файл output.json в следующем формате:

[
    {
        "title": "Доктор Иванов Иван Иванович",
        "link": "/doctor/ivanov-ivan-ivanovich/",
        "phone": "+74951234567"
    },
    {
        "title": "Доктор Петров Петр Петрович",
        "link": "/doctor/petrov-petr-petrovich/",
        "phone": "+74959876543"
    }
]

## Зависимости

Для корректной работы парсера необходимо установить следующие библиотеки:

- `requests` — выполнение HTTP-запросов
- `beautifulsoup4` — парсинг HTML-страниц
- `lxml` — парсер для BeautifulSoup (повышает скорость обработки)

Установка всех зависимостей:

bash
pip install -r requirements.txt

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](./LICENSE).

