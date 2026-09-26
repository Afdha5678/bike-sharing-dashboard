# 🚲 Proyek Analisis Data: Bike Sharing Dataset ✨

Proyek akhir analisis data ini bertujuan untuk mengeksplorasi, menganalisis, dan menarik wawasan bisnis yang mendalam dari **Bike Sharing Dataset** (Capital Bikeshare system, Washington D.C., USA). Analisis dilakukan mengikuti metodologi analisis data yang terstruktur: *Determining Business Questions (SMART)*, *Data Wrangling (Gathering, Assessing, Cleaning)*, *Exploratory Data Analysis (EDA Univariate, Bivariate, Multivariate, & Aggregation)*, *Data Visualization & Explanatory Analysis*, *Advanced Non-ML Analysis (Binning & RFM Analysis)*, serta perumusan *Conclusion & Actionable Recommendations*.

- **Nama:** Afdha Auliya Atiq
- **Email:** afdha.auliya.atiq@gmail.com
- **ID Dicoding:** afdha_auliya_atiq

---

## Setup Environment - Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run streamlit app
```bash
streamlit run dashboard/dashboard.py
```

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
├── README.md                 # Dokumentasi proyek analisis data & petunjuk environment
├── requirements.txt          # Daftar pustaka Python yang dibutuhkan
└── url.txt                   # Tautan aplikasi Streamlit Cloud
```

---

## 🎯 Pertanyaan Bisnis Utama (Prinsip SMART)

1. **Tren Bulanan (Time-Bound 2011-2012):** Bagaimana performa dan tren total penyewaan sepeda (berdasarkan tipe pengguna: *casual* vs *registered*) selama periode tahun 2011 hingga 2012?
2. **Pola Jam Sibuk (Time-Bound 2011-2012):** Pada jam berapa saja terjadi lonjakan puncak (*peak hours*) dan titik terendah (*off-peak hours*) penyewaan sepeda pada hari kerja (*working day*) dibandingkan akhir pekan/hari libur (*non-working day*) selama periode tahun 2011 hingga 2012?
3. **Faktor Cuaca & Musim (Time-Bound 2011-2012):** Bagaimana pengaruh kondisi cuaca (*weathersit*) dan musim (*season*) terhadap volume penyewaan sepeda harian oleh pengguna *casual* dan *registered* selama periode tahun 2011 hingga 2012?

---

## 🌐 Tautan Live Dashboard Streamlit

Aplikasi Dashboard interaktif telah di-deploy dan dapat diakses publik melalui tautan berikut:
👉 [Bike Sharing Analytics Dashboard (Streamlit Cloud)](https://bike-sharing-dashboard-afdha5678.streamlit.app/)

---

## 📓 Menjalankan Jupyter Notebook Analisis Data

Untuk membuka dan mengeksekusi kembali seluruh alur analisis data (Data Wrangling, EDA Univariate & Bivariate/Multivariate, Visualisasi, RFM Analysis & Manual Binning):

```bash
jupyter notebook notebook.ipynb
```
Atau buka berkas `notebook.ipynb` / `Proyek_Analisis_Data.ipynb` menggunakan Visual Studio Code / Google Colab.

---

## 📊 Hasil Utama, Insight, & Actionable Recommendations

### 1. Pertanyaan 1: Tren Bulanan (2011-2012)
- **Evidence & Trend:** Total penyewaan sepeda tumbuh sebesar **+64,8%** dari 2011 ke 2012. *Registered Users* mendominasi dengan kontribusi **~81,8%** dengan tren naik linear konsisten. *Casual Users* (**~18,2%**) memiliki pola musiman memuncak pada musim panas/gugur.
- **Actionable Recommendation:**
  1. Peluncuran *Casual-to-Registered Pass* diskon khusus saat puncak musim panas untuk konversi pengguna kasual.
  2. Paket *Seasonal Pass* (Summer/Fall Pass) khusus untuk pengguna rekreasi.

### 2. Pertanyaan 2: Pola Jam Sibuk (2011-2012)
- **Evidence & Trend:** Hari Kerja membentuk tren *bimodal peak* pada **08:00** (477 unit/jam) dan **17:00-18:00** (525 unit/jam) untuk komuter. Akhir pekan membentuk *unimodal peak* melandai pada **12:00-16:00** (373 unit/jam) untuk rekreasi.
- **Actionable Recommendation:**
  1. Melakukan *rebalancing* armada sepeda ke stasiun komuter sebelum jam 07:00 dan jam 16:30 pada hari kerja.
  2. Melakukan jadwal pemeliharaan rutin pada jam terendah (*off-peak*) pukul 01:00-05:00 WIB.
  3. Relokasi penempatan armada ke lokasi wisata dan taman pada akhir pekan.

### 3. Pertanyaan 3: Dampak Cuaca & Musim (2011-2012)
- **Evidence & Trend:** Musim Gugur (*Fall*) mencatat rerata harian tertinggi (**5.644 unit/hari**). Cuaca Cerah (*Clear/Few Clouds*) mendorong peminjaman puncak (**4.877 unit/hari**), sedangkan hujan/salju menekan peminjaman drastis hingga **>60%**.
- **Actionable Recommendation:**
  1. Penerapan *Dynamic Pricing* / diskon peminjaman saat *off-season* atau kondisi berawan ringan.
  2. Penambahan perlengkapan proteksi cuaca (fender air/lumpur) pada unit sepeda.
