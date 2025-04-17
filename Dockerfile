FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY credentials/weather-etl-key.json /app/credentials/weather-etl-key.json

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials/weather-etl-key.json"

CMD ["python", "etl_pipeline.py"]