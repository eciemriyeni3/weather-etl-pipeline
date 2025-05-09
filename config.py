import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE")