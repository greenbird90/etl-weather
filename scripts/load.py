def save_to_csv(df, filename="output/weather_data.csv"):
    import os
    os.makedirs("output", exist_ok=True)
    df.to_csv(filename, index=False)
