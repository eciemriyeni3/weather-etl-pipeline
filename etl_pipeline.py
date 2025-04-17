from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_bigquery
from config import BIGQUERY_TABLE

if __name__ == "__main__":
    raw = extract_weather_data()
    transformed = transform_weather_data(raw)
    load_to_bigquery(transformed, BIGQUERY_TABLE)