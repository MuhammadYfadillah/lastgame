import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data heatmap
polusi1 = pd.read_csv("dashboard/shunyixPM25.csv")  # Ganti dengan nama file CSV
polusi2 = pd.read_csv("dashboard/shunyixPM10.csv")  # Ganti dengan nama file CSV
polusi3 = pd.read_csv("dashboard/tiantanxPM25.csv")  # Ganti dengan nama file CSV
polusi4 = pd.read_csv("dashboard/tiantanxPM10.csv")  # Ganti dengan nama file CSV

# Load data plotline
cuaca1 = pd.read_csv("dashboard/shunyiRAIN.csv")  # Ganti dengan nama file CSV
cuaca2 = pd.read_csv("dashboard/shunyiTEMP.csv")  # Ganti dengan nama file CSV
cuaca3 = pd.read_csv("dashboard/tiantanRAIN.csv")  # Ganti dengan nama file CSV
cuaca4 = pd.read_csv("dashboard/tiantanRAIN.csv")  # Ganti dengan nama file CSV

# Fungsi untuk menampilkan Heatmap
def tampilkan_heatmap(polusi):
    plt.figure(figsize=(10, 6))  #Sesuaikan ukuran gambar jika diperlukan
    sns.heatmap(polusi, annot=True, fmt=".1f", cmap="viridis") #Sesuaikan anotasi dan peta warna
    plt.title('Tingkatan Kadar Polutan')
    plt.xlabel('Year')
    plt.ylabel('Month')
    st.pyplot(plt)

# Fungsi untuk menampilkan Plotline
def tampilkan_plotline(cuaca):
    cuaca.plot(kind='line')
    plt.title('Rata-rata Suhu Bulanan Tahun 2014')
    plt.xlabel('Bulan')
    plt.ylabel('Nilai')
    st.pyplot(plt)

# Judul Dashboard
st.title("Dashboard Kualitas Udara")

# Sidebar untuk Filter
st.sidebar.title("Filter")
filter_opsi = st.sidebar.radio("Pilih Visualisasi", ("Tren Polutan", "Tren Curah Hujan dan Suhu"))

# Menampilkan Visualisasi Berdasarkan Filter
if filter_opsi == "Tren Polutan":
    st.header("Tren Polutan")

    # Membuat Heatmap
    st.subheader("PM2.5 di Kota Shunyi")
    tampilkan_heatmap(polusi1)
    st.subheader("PM10 di Kota Shunyi")
    tampilkan_heatmap(polusi2)
    st.subheader("PM2.5 di Kota Tiantan")
    tampilkan_heatmap(polusi3)
    st.subheader("PM10 di Kota Tiantan")
    tampilkan_heatmap(polusi4)

elif filter_opsi == "Tren Curah Hujan dan Suhu":
    st.header("Tren Curah Hujan dan Suhu")

    # Membuat Plotline
    st.subheader("Curah Hujan di Kota Shunyi")
    tampilkan_plotline(cuaca1)
    st.subheader("Suhu di Kota Shunyi")
    tampilkan_plotline(cuaca2)
    st.subheader("Curah Hujan di Kota Tiantan")
    tampilkan_plotline(cuaca3)
    st.subheader("Suhu di Kota Tiantan")
    tampilkan_plotline(cuaca4)

