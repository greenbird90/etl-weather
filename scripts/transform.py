import pandas as pd

def transform_weather_data(raw_json):
    data = raw_json['daily']
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['time'])
    return df[['date', 'temperature_2m_max', 'temperature_2m_min']]
