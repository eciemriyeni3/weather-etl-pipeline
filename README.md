# 🌦️ Weather ETL Pipeline

An automated ETL pipeline that collects hourly weather data from OpenWeatherMap API, transforms it, and loads it into Google BigQuery.

## 📌 Features
- Extracts real-time weather data (city, temperature, humidity, etc.)
- Transform raw JSON into structured format
- Load data to BigQuery (batch job, not streaming)
- Scheduled every hour using GitHub Actions
- Dockerized for portability

## 🧰 Tech Stack
- Python
- BigQuery
- Docker
- GitHub Actions
- OpenWeatherMap API

## 📁 Project Structure
![Weather Data Pipeline drawio (1)](https://github.com/user-attachments/assets/9aa5f987-029f-47f5-9d55-925223b546f0)

## 🚀 How to Run
1. Clone repository
2. Create a `.env` file based on .env.example (Set up `.env` with your API key & table info)
3. Activate virtual environment, by running: `python -m venv venv && source venv/bin/activate`
4. Install dependencies, by running `pip install -r requirements.txt`
5. Run: `python etl_pipeline.py` or use Docker `docker build -t weather-etl .` & `docker run --rm --env-file .env weather-etl`

## 🔐 Security Note
Secrets are managed via GitHub Actions Secrets and `.gitignore` is used to avoid committing credentials.

## 👩‍💻 Author
Eci Emriyeni · [LinkedIn](https://linkedin.com/in/eciemriyeni3)
