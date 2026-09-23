# 🚲 Proyek Analisis Data: Bike Sharing Dataset

Proyek akhir analisis data ini bertujuan untuk mengeksplorasi, menganalisis, dan menarik wawasan bisnis yang mendalam dari **Bike Sharing Dataset** (Capital Bikeshare system, Washington D.C., USA). Analisis dilakukan mengikuti metodologi analisis data yang terstruktur: *Determining Business Questions (SMART)*, *Data Wrangling (Gathering, Assessing, Cleaning)*, *Exploratory Data Analysis (EDA)*, *Data Visualization & Explanatory Analysis*, *Advanced Non-ML Analysis (Binning & RFM Analysis)*, serta perumusan *Conclusion & Actionable Recommendations*.

- **Nama:** Afdha Auliya Atiq
- **Email:** afdha.auliya.atiq@gmail.com
- **ID Dicoding:** afdha_auliya_atiq

---

## 📁 Struktur Direktori Proyek

```text
submission/
├── dashboard/
│   ├── dashboard.py          # Aplikasi Streamlit Dashboard interaktif
│   ├── main_data.csv         # Dataset harian yang telah dibersihkan
│   └── hour_clean.csv        # Dataset per jam yang telah dibersihkan
├── data/
│   ├── day.csv               # Dataset mentah harian
│   └── hour.csv              # Dataset mentah per jam
├── notebook.ipynb            # Jupyter Notebook analisis data lengkap (tereksekusi)
├── Proyek_Analisis_Data.ipynb# Salinan berkas Jupyter Notebook utama
├── README.md                 # Dokumentasi proyek analisis data
├── requirements.txt          # Daftar pustaka Python yang dibutuhkan
└── url.txt                   # Tautan aplikasi Streamlit Cloud
```

---

## 🎯 Pertanyaan Bisnis utama

1. **Tren Bulanan:** Bagaimana performa dan tren total penyewaan sepeda (berdasarkan tipe pengguna: *casual* vs *registered*) dari tahun 2011 hingga 2012?
2. **Pola Jam Sibuk:** Pada jam berapa terjadi lonjakan puncak (*peak hours*) dan titik terendah (*off-peak hours*) penyewaan sepeda pada hari kerja (*working day*) dibandingkan akhir pekan/hari libur (*non-working day*)?
3. **Faktor Cuaca & Musim:** Bagaimana pengaruh kondisi cuaca (*weathersit*) dan musim (*season*) terhadap volume penyewaan sepeda harian?

---

## ⚙️ Cara Menjalankan Proyek

### 1. Membuka Jupyter Notebook Analisis Data
Pastikan lingkungan Python Anda telah terinstal Jupyter Notebook atau JupyterLab:
```bash
jupyter notebook notebook.ipynb
```
Atau buka berkas `notebook.ipynb` langsung menggunakan Google Colab / VS Code.

### 2. Menjalankan Dashboard Streamlit Secara Lokal

1. **Instalasi Dependencies:**
   Jalankan perintah berikut pada terminal untuk menginstal seluruh dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

2. **Menjalankan Dashboard:**
   Navigasikan ke direktori utama proyek, lalu jalankan perintah Streamlit berikut:
   ```bash
   streamlit run dashboard/dashboard.py
   ```
   Aplikasi dashboard otomatis terbuka pada peramban web di alamat `http://localhost:8501`.

---

## 📊 Hasil Utama & Ringkasan Temuan
- **Pertumbuhan Bisnis:** Penyewaan sepeda tumbuh pesat sebesar **+64,8%** dari 2011 ke 2012. Pengguna terdaftar (*Registered*) mendominasi dengan kontribusi **~81,8%**.
- **Pola Jam Sibuk:** Hari kerja memiliki bimodal peak tajam di jam **08:00** dan **17:00-18:00** (mobilitas komuter). Akhir pekan memiliki unimodal peak melandai di jam **12:00-16:00** (rekreasi).
- **Faktor Cuaca:** Musim Gugur (*Fall*) dan Cuaca Cerah (*Clear / Few Clouds*) adalah pendorong utama penyewaan. Cuaca hujan/salju menurunkan penyewaan hingga **>60%**.
