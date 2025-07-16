FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/sweet_shop

EXPOSE 8000

CMD ["python", "main.py"]
