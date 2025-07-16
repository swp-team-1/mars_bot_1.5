FROM python:3.11-slim

WORKDIR /app

# Копируем оба requirements.txt (если второй в поддиректории db_connector)
COPY requirements.txt .
COPY db_connector/requirements.txt db_connector/requirements.txt

# Устанавливаем зависимости из обоих файлов
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r db_connector/requirements.txt

# Копируем весь проект
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
