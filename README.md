1. **Структура проекту**
   ```
   iot_management/
   ├── app.py
   ├── config.py
   ├── create_tables.py
   ├── Dockerfile
   ├── docker-compose.yml
   ├── models.py
   ├── requirements.txt
   ├── test_app.py
   └── README.md
   ```

2. **Файли конфігурації**
   - `config.py`: Конфігурація для підключення до бази даних PostgreSQL через Peewee.
   - `Dockerfile`: Інструкції для створення Docker-образу.
   - `docker-compose.yml`: Конфігурація для Docker Compose.
   - `requirements.txt`: Залежності Python для вашого проекту.



### Запуск додатку

1. **Збірка Docker-образів та запуск контейнерів**
   ```bash
   docker-compose up --build
   ```

2. **Перевірка статусу контейнерів**
   ```bash
   docker-compose ps
   ```
   Перегляньте логи:
   ```bash
   docker-compose logs
   ```

### Тестування

**Встановіть `pytest`:**
    ```bash
    pip install pytest
    ```


### Документація API

**API має такі кінцеві точки:**
   - POST /devices: Створення нового пристрою.
   - GET /devices/{id}: Отримання інформації про пристрій за його ID.
   - PUT /devices/{id}: Оновлення інформації про пристрій за його ID.
   - DELETE /devices/{id}: Видалення пристрою за його ID.
