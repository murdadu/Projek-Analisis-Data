import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Konversi tanggal menjadi datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Judul Dashboard
st.title("🚲 Dashboard Analisis Penyewaan Sepeda")

# Sidebar Filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(day_df['dteday'].dt.year.unique()))
filtered_df = day_df[day_df['dteday'].dt.year == selected_year]

# 1️⃣ Tampilkan Data Penyewaan Harian
st.subheader(f"📅 Data Penyewaan Sepeda Tahun {selected_year}")
st.dataframe(filtered_df.head())

# 2️⃣ Grafik Tren Penyewaan Sepeda
st.subheader("📈 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=filtered_df['dteday'], y=filtered_df['cnt'], marker="o", ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan")
plt.grid()
st.pyplot(fig)

st.markdown("📌 **Insight:** Penyewaan sepeda cenderung meningkat pada bulan tertentu dan berfluktuasi sesuai dengan musim.")

# 3️⃣ Heatmap Korelasi Antar Variabel
st.subheader("🔍 Heatmap Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(filtered_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig)

st.markdown("📌 **Insight:** Variabel seperti suhu dan hari kerja memiliki pengaruh terhadap jumlah penyewaan sepeda.")

# 4️⃣ Distribusi Penyewaan Berdasarkan Cuaca
st.subheader("🌦️ Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=filtered_df['weathersit'], y=filtered_df['cnt'], ax=ax)
plt.xlabel("Kondisi Cuaca (1: Cerah, 2: Mendung, 3: Hujan)")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.markdown("📌 **Insight:** Penyewaan sepeda lebih tinggi saat cuaca cerah dan lebih rendah saat hujan.")

# 5️⃣ Distribusi Penyewaan Berdasarkan Musim
st.subheader("🍂 Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=filtered_df['season'], y=filtered_df['cnt'], ax=ax)
plt.xlabel("Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.markdown("📌 **Insight:** Penyewaan sepeda tertinggi terjadi di musim panas dan terendah di musim dingin.")

# Kesimpulan
st.subheader("📊 Kesimpulan")
st.markdown("""
- Penyewaan sepeda **meningkat saat cuaca cerah** dan **menurun saat hujan**.
- **Musim panas** adalah periode dengan penyewaan tertinggi, sedangkan musim dingin lebih rendah.
- **Korelasi menunjukkan** bahwa suhu dan hari kerja memiliki hubungan kuat terhadap penyewaan sepeda.
""")

# Jalankan dengan `streamlit run dashboard.py`
