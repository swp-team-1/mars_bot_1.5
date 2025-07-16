FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY db_connector/requirements.txt db_connector/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir -r db_connector/requirements.txt

COPY . .

# Используем переменную PORT, Railway подставит нужное значение
ENV PORT=8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
