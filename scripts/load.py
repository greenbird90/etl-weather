def save_to_csv(df):
    import os
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/weather_data.csv", index=False)
    print("✅ File CSV berhasil disimpan ke data/weather_data.csv")
