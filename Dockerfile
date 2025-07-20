FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY db_connector/requirements.txt db_connector/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir -r db_connector/requirements.txt

# Устанавливаем ffmpeg и зависимости
RUN apt-get update && apt-get install -y ffmpeg

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    && rm -rf /var/lib/apt/lists/*
    
COPY . .

# Используем переменную PORT, Railway подставит нужное значение
ENV PORT=8080

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
