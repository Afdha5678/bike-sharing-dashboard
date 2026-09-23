import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Bike Sharing Analytics Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stylings
sns.set_theme(style='whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# Fungsi memuat data dengan cache
@st.cache_data
def load_data():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(curr_dir, 'main_data.csv')
    hour_path = os.path.join(curr_dir, 'hour_clean.csv')
    
    if not os.path.exists(main_path):
        main_path = os.path.join(curr_dir, '..', 'dashboard', 'main_data.csv')
        hour_path = os.path.join(curr_dir, '..', 'dashboard', 'hour_clean.csv')
        
    day_df = pd.read_csv(main_path)
    hour_df = pd.read_csv(hour_path)
    
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    return day_df, hour_df

try:
    day_df, hour_df = load_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=80)
st.sidebar.title("🚲 Navigation & Filter")
st.sidebar.markdown("**Analyst:** Afdha Auliya Atiq")
st.sidebar.markdown("**Dicoding Data Analysis Project**")
st.sidebar.markdown("---")

# Filter Rentang Tanggal
min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

start_date, end_date = st.sidebar.date_input(
    label="Rentang Tanggal Analysis:",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Filter Musim
all_seasons = ['Spring', 'Summer', 'Fall', 'Winter']
selected_seasons = st.sidebar.multiselect(
    label="Pilih Musim (Season):",
    options=all_seasons,
    default=all_seasons
)

# Filter Cuaca
all_weather = day_df['weather_label'].unique().tolist()
selected_weather = st.sidebar.multiselect(
    label="Pilih Kondisi Cuaca:",
    options=all_weather,
    default=all_weather
)

# Filter Dataframe berdasarkan Input Sidebar
filtered_day = day_df[
    (day_df['dteday'].dt.date >= start_date) &
    (day_df['dteday'].dt.date <= end_date) &
    (day_df['season_label'].isin(selected_seasons)) &
    (day_df['weather_label'].isin(selected_weather))
]

filtered_hour = hour_df[
    (hour_df['dteday'].dt.date >= start_date) &
    (hour_df['dteday'].dt.date <= end_date) &
    (hour_df['season_label'].isin(selected_seasons)) &
    (hour_df['weather_label'].isin(selected_weather))
]

# --- MAIN DASHBOARD CONTENT ---
st.title("🚲 Dashboard Analisis Penyewaan Sepeda (Bike Sharing)")
st.markdown("Visualisasi data interaktif untuk mengeksplorasi pola penyewaan sepeda berdasarkan tren bulanan, siklus jam sibuk, pengaruh kondisi cuaca/musim, serta segmentasi pengguna.")
st.markdown("---")

# KPI Metrics Section
st.subheader("📌 Key Performance Indicators (KPI)")
col1, col2, col3, col4 = st.columns(4)

total_rentals = filtered_day['cnt'].sum()
total_registered = filtered_day['registered'].sum()
total_casual = filtered_day['casual'].sum()
registered_pct = (total_registered / total_rentals * 100) if total_rentals > 0 else 0

with col1:
    st.metric(label="Total Penyewaan Sepeda", value=f"{total_rentals:,}")
with col2:
    st.metric(label="Pengguna Terdaftar (Registered)", value=f"{total_registered:,}")
with col3:
    st.metric(label="Pengguna Kasual (Casual)", value=f"{total_casual:,}")
with col4:
    st.metric(label="Proporsi Registered", value=f"{registered_pct:.1f}%")

st.markdown("---")

# TAB SYSTEM
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Tren Bulanan", 
    "⏰ Pola Jam Sibuk", 
    "🌤️ Dampak Cuaca & Musim", 
    "📊 Analisis Lanjutan & Segmentasi"
])

# --- TAB 1: TREN BULANAN ---
with tab1:
    st.header("📈 Performa dan Tren Penyewaan Bulanan (2011 vs 2012)")
    
    monthly_df = filtered_day.groupby(['yr_label', 'mnth']).agg(
        casual=('casual', 'sum'),
        registered=('registered', 'sum'),
        cnt=('cnt', 'sum')
    ).reset_index()
    monthly_df['period'] = monthly_df['yr_label'] + '-' + monthly_df['mnth'].astype(str).str.zfill(2)
    
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(monthly_df['period'], monthly_df['registered'], marker='o', color='#1f77b4', linewidth=2.5, label='Registered Users')
    ax.plot(monthly_df['period'], monthly_df['casual'], marker='s', color='#ff7f0e', linewidth=2.5, label='Casual Users')
    ax.plot(monthly_df['period'], monthly_df['cnt'], marker='^', color='#2ca02c', linestyle='--', linewidth=2, label='Total Rentals (cnt)')
    
    ax.set_title("Grafik Tren Penyewaan Sepeda Bulanan", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Periode (Tahun-Bulan)", fontsize=10)
    ax.set_ylabel("Jumlah Penyewaan", fontsize=10)
    ax.set_xticklabels(monthly_df['period'], rotation=45, ha='right')
    ax.legend(frameon=True, facecolor='white')
    ax.grid(True, linestyle=':', alpha=0.6)
    
    st.pyplot(fig)
    
    st.info("""
    💡 **Insight Utama Tren Bulanan:**
    - Terjadi kenaikan total peminjaman sepeda dari tahun 2011 hingga 2012 sebesar **+64,8%**.
    - **Pengguna Registered** menjadi kontributor terbesar konstan (~81,8%) dengan pertumbuhan yang stabil.
    - **Pengguna Casual** menunjukkan variasi musiman yang tajam, memuncak pada bulan musim panas (Juni - September).
    """)

# --- TAB 2: POLA JAM SIBUK ---
with tab2:
    st.header("⏰ Pola Penyewaan Jam Sibuk (Hari Kerja vs Akhir Pekan)")
    
    hourly_pattern = filtered_hour.groupby(['workingday_label', 'hr'])['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(
        data=hourly_pattern, 
        x='hr', 
        y='cnt', 
        hue='workingday_label',
        palette={'Working Day': '#1f77b4', 'Weekend / Holiday': '#e377c2'},
        linewidth=3,
        markers=True,
        ax=ax
    )
    
    ax.axvspan(7.5, 8.5, color='#1f77b4', alpha=0.15, label='Puncak Pagi Hari Kerja (08:00)')
    ax.axvspan(16.5, 18.5, color='#1f77b4', alpha=0.15, label='Puncak Sore Hari Kerja (17:00-18:00)')
    
    ax.set_title("Rata-Rata Penyewaan Sepeda per Jam (00:00 - 23:00)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Jam Harian", fontsize=10)
    ax.set_ylabel("Rata-Rata Sepeda Tersewa per Jam", fontsize=10)
    ax.set_xticks(range(0, 24))
    ax.legend(frameon=True, facecolor='white')
    ax.grid(True, linestyle=':', alpha=0.6)
    
    st.pyplot(fig)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🏢 Hari Kerja (Working Day)")
        st.write("• **Puncak Pagi:** Pukul 08:00 (Rata-rata 477 penyewaan/jam)")
        st.write("• **Puncak Sore:** Pukul 17:00 - 18:00 (Rata-rata 525 penyewaan/jam)")
        st.write("• **Karakteristik:** Mobilitas komuter pekerja/pelajar.")
    with col_b:
        st.subheader("🏖️ Akhir Pekan / Libur (Weekend/Holiday)")
        st.write("• **Puncak Siang-Sore:** Pukul 12:00 - 16:00 (Rata-rata ~373 penyewaan/jam)")
        st.write("• **Karakteristik:** Didominasi aktivitas santai/rekreasi pengguna casual.")

# --- TAB 3: DAMPAK CUACA & MUSIM ---
with tab3:
    st.header("🌤️ Pengaruh Faktor Lingkungan (Musim & Cuaca)")
    
    col_x, col_y = st.columns(2)
    
    with col_x:
        st.subheader("Distribusi Berdasarkan Musim")
        season_order = ['Spring', 'Summer', 'Fall', 'Winter']
        season_df = filtered_day.groupby('season_label')[['casual', 'registered']].mean().reindex(season_order)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        season_df.plot(kind='bar', stacked=False, color=['#ff7f0e', '#1f77b4'], ax=ax, width=0.7)
        ax.set_title("Rerata Penyewaan harian per Musim", fontsize=11, fontweight='bold')
        ax.set_xlabel("Musim", fontsize=9)
        ax.set_ylabel("Rata-Rata Penyewaan Harian", fontsize=9)
        ax.set_xticklabels(season_order, rotation=0)
        ax.legend(['Casual', 'Registered'])
        ax.grid(axis='y', linestyle=':', alpha=0.7)
        st.pyplot(fig)
        
    with col_y:
        st.subheader("Distribusi Berdasarkan Cuaca")
        weather_df = filtered_day.groupby('weather_label')[['casual', 'registered']].mean()
        
        fig, ax = plt.subplots(figsize=(6, 4))
        weather_df.plot(kind='bar', stacked=False, color=['#ff7f0e', '#1f77b4'], ax=ax, width=0.7)
        ax.set_title("Rerata Penyewaan harian per Cuaca", fontsize=11, fontweight='bold')
        ax.set_xlabel("Cuaca", fontsize=9)
        ax.set_ylabel("Rata-Rata Penyewaan Harian", fontsize=9)
        ax.set_xticklabels(weather_df.index, rotation=15)
        ax.legend(['Casual', 'Registered'])
        ax.grid(axis='y', linestyle=':', alpha=0.7)
        st.pyplot(fig)
        
    st.info("""
    💡 **Insight Cuaca & Musim:**
    - **Musim Gugur (Fall)** merupakan musim favorit dengan rata-rata peminjaman tertinggi (**5.644 unit/hari**).
    - Cuaca **Cerah (Clear / Few Clouds)** mendorong utilisasi tertinggi. Kehadiran hujan/salju menurunkan penyewaan secara drastis hingga **>60%**.
    """)

# --- TAB 4: ANALISIS LANJUTAN & SEGMENTASI ---
with tab4:
    st.header("📊 Analisis Lanjutan & Segmentasi Permintaan (Non-ML)")
    
    st.subheader("1. Manual Clustering / Binning Permintaan Harian")
    labels_demand = ['Low Demand', 'Medium Demand', 'High Demand', 'Peak Demand']
    filtered_day['demand_cluster'] = pd.qcut(filtered_day['cnt'], q=4, labels=labels_demand)
    
    cluster_summary = filtered_day.groupby('demand_cluster', observed=False).agg(
        Jumlah_Hari=('cnt', 'count'),
        Rerata_Total=('cnt', 'mean'),
        Rerata_Casual=('casual', 'mean'),
        Rerata_Registered=('registered', 'mean'),
        Rerata_Suhu_C=('temp_c', 'mean')
    ).reset_index()
    
    st.dataframe(cluster_summary, use_container_width=True)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(data=cluster_summary, x='demand_cluster', y='Rerata_Total', palette='Blues_d', ax=ax)
    ax.set_title("Rata-Rata Total Penyewaan per Segmen Permintaan", fontsize=12, fontweight='bold')
    ax.set_xlabel("Segmen Permintaan (Binning)", fontsize=10)
    ax.set_ylabel("Rata-Rata Sepeda Tersewa (cnt)", fontsize=10)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=9, fontweight='bold')
    st.pyplot(fig)
    
    st.markdown("---")
    st.subheader("2. Adaptasi Analisis RFM Bulanan")
    max_d = filtered_day['dteday'].max()
    filtered_day['yr_act'] = 2011 + filtered_day['yr']
    filtered_day['period_rfm'] = filtered_day['yr_act'].astype(str) + '-' + filtered_day['mnth'].astype(str).str.zfill(2)
    
    rfm_monthly = filtered_day.groupby('period_rfm').agg(
        Recency=('dteday', lambda x: (max_d - x.max()).days),
        Frequency=('cnt', lambda x: (x >= 4500).sum()),
        Monetary=('cnt', 'sum')
    ).reset_index()
    
    st.dataframe(rfm_monthly.tail(12), use_container_width=True)

st.markdown("---")
st.caption("Copyright © 2026 Afdha Auliya Atiq - Proyek Analisis Data Dicoding")
