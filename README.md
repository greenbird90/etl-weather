# ETL Weather Pipeline 🌧️

[![ETL Pipeline Status](https://github.com/greenbird90/etl-weather/actions/workflows/etl.yml/badge.svg)](https://github.com/greenbird90/etl-weather/actions)

Proyek ini adalah **ETL pipeline sederhana** yang mengambil data cuaca harian dari API publik [Open-Meteo](https://open-meteo.com/), lalu menyimpannya ke dalam file CSV. Pipeline ini dibuat dengan **Python** dan otomatis dijalankan setiap hari dengan **GitHub Actions**.

---

## 📊 Data yang Diambil

- **Sumber API**: [Open-Meteo](https://open-meteo.com/en/docs)
- **Lokasi**: Jakarta, Indonesia (koordinat: -6.2, 106.8)
- **Periode**: 7 hari ke belakang
- **Kolom:**
  - `date`
  - `temperature_2m_max`
  - `temperature_2m_min`

---

## 💡 Arsitektur Pipeline

```
+-----------+       +-------------+       +-------------+       +-------------+
|  extract  |  -->  |  transform  |  -->  |    load     |  -->  |  CSV Output  |
+-----------+       +-------------+       +-------------+       +-------------+
```

### 1. Extract (`scripts/extract.py`)
Mengambil data cuaca 7 hari ke belakang dari Open-Meteo API.

### 2. Transform (`scripts/transform.py`)
- Konversi ke pandas DataFrame
- Rename kolom agar mudah dibaca

### 3. Load (`scripts/load.py`)
- Simpan ke file: `output/weather_data.csv`

---

## 💻 Teknologi

- Python 3.10
- `pandas`, `requests`
- GitHub Actions (untuk otomatisasi)

---

## ⚙️ Cara Menjalankan di Lokal

```bash
# 1. Clone repo ini
$ git clone https://github.com/greenbird90/etl-weather.git
$ cd etl-weather

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Jalankan pipeline
$ python scripts/run_etl.py
```

📁 Output CSV akan disimpan di `output/weather_data.csv`

---

## ⏳ Otomasi dengan GitHub Actions

ETL pipeline ini dijalankan otomatis setiap hari melalui GitHub Actions:

- File workflow: `.github/workflows/etl.yml`
- Bisa juga dijalankan manual dari tab **Actions**

---

## 🗂️ Use Case

- Bisa dikembangkan ke:
  - Load ke database (PostgreSQL)
  - Visualisasi pakai Streamlit atau Power BI
  - Notifikasi otomatis ke Telegram/Discord

---

## 📄 Lisensi

MIT License

---

## 👤 Dibuat oleh

Nama: **[Saripudin Sahardi]**  
🔗 LinkedIn: [linkedin.com/in/saripudin-sahardi-387b74156/](https://linkedin.com/in/saripudin-sahardi-387b74156/)

