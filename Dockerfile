FROM python:3.12-slim

RUN apt-get update && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/www

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080

CMD ["gunicorn main:app"]