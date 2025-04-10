import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.extract import fetch_weather_data
from scripts.transform import transform_weather_data
from scripts.load import save_to_csv

def main():
    print("🚀 ETL process started")

    raw = fetch_weather_data(-6.2, 106.8)
    print("✅ Weather data fetched")

    df = transform_weather_data(raw)
    print("✅ Weather data transformed")

    save_to_csv(df)
    print("✅ Data saved to CSV")

if __name__ == "__main__":
    main()
