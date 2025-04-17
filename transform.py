def transform_weather_data(raw_data):
    return {
        'city': raw_data['name'],
        'temperature': raw_data['main']['temp'],
        'humidity': raw_data['main']['humidity'],
        'weather': raw_data['weather'][0]['main'],
        'timestamp': raw_data['dt']
    }