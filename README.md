# Описание

Автотесты для тестового сервиса Restful-booker (REST API playground for practicing API testing)

Адрес сервиса - https://restful-booker.herokuapp.com/

Ссыла на документацию API - https://restful-booker.herokuapp.com/apidoc/


# Stack
- Python 3.x
- pytest
- requests
- allure-pytest
- pytest-xdist


# Структура

* checkers: вспомогательные проверочные функции/методы
* fixtures: фикстуры
* routes: роуты/эндпоинты сервиса (REST)
* tests: тесты на REST API
* config: данные для настроек, урлы и т.д.
* config_file.json: файл с данными, которые подгружаются в config.py


# Настройка для локального запуска
## Конфиг файл

В нашем случае сервис тестовый и не реализует реальную регистрацию пользователей, поэтому sensetive данные (password и username) напрямую лежат в config_file.json. Если бы сервис был рельный, то данные подгружались бы из config_file_local.json, а не config_file.json.

## Настройка виртуального окружения

**Проверяем версию Питона (должна быть не меньше 3.10):**

```bash
python3 -V
Python 3.12.10
```

**Создаём виртуальное окружение:**

```bash
python3 -m venv venv
```

**Активируем:**
```bash
source venv/bin/activate

Результат:

venv your_user:path/to/project/project$
```

**Устанавливаем зависимости:**
```bash
pip install -r requirements.txt
```

**Запускаем тесты:**
```bash
pytest
```

**Запускаем тесты параллельно:**
```bash
pytest -n 4
```

**Запускаем тесты и получаем отчет тестирования:**
```bash
pytest --alluredir=allure-results --clean-alluredir -n auto
allure serve allure-results
```


## Bugs
| # | Endpoint                 | Description                                                                                       |
|---|--------------------------|---------------------------------------------------------------------------------------------------
| 1 | POST /auth               | Returns 200 instead of 401 for invalid credentials
| 2 | POST /booking            | `additionalneeds` is listed as required in docs, but API accepts request without it and returns 200
| 3 | POST /booking            | `additionalneeds` accepts invalid data types
| 4 | POST /booking            | `totalprice` accepts invalid data types 
| 5 | POST /booking            | `depositpaid` accepts invalid data types
| 6 | POST /booking            | `bookingdates` accepts invalid types 
| 7 | DELETE /booking/{id}     | Returns 201 Created instead of 200 OK
