import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Optimasi Produksi Risol", layout="centered")
st.title("📈 Aplikasi Produksi Risol Tetap (40 Mayo & 20 Sayur)")

st.subheader("Masukkan Data Produksi")

# Input keuntungan
profit_mayo = st.number_input("Keuntungan per Risol Mayo", min_value=1.0, value=5000.0)
profit_sayur = st.number_input("Keuntungan per Risol Sayur", min_value=1.0, value=3000.0)

st.markdown("### Batasan (Kendala Produksi)")

col1, col2 = st.columns(2)
with col1:
    a1 = st.number_input("Bahan baku per Risol Mayo", value=2.0)
    a2 = st.number_input("Bahan baku per Risol Sayur", value=1.0)
    b1 = st.number_input("Total bahan baku tersedia", value=100.0)

with col2:
    a3 = st.number_input("Waktu per Risol Mayo (menit)", value=1.0)
    a4 = st.number_input("Waktu per Risol Sayur (menit)", value=2.0)
    b2 = st.number_input("Total waktu tersedia (menit)", value=60.0)  # 1 JAM

# Tetapkan jumlah produksi tetap
x_fixed = 40  # risol mayo
y_fixed = 20  # risol sayur

# Hitung kebutuhan bahan dan waktu
kebutuhan_bahan = a1 * x_fixed + a2 * y_fixed
kebutuhan_waktu = a3 * x_fixed + a4 * y_fixed

# Hitung keuntungan
total_profit = profit_mayo * x_fixed + profit_sayur * y_fixed

if st.button("🔍 Cek Produksi Tetap (40 Mayo & 20 Sayur)"):
    st.write("### 📦 Rencana Produksi Tetap")
    st.write(f"- Risol Mayo: {x_fixed}")
    st.write(f"- Risol Sayur: {y_fixed}")
    st.write(f"- Total Keuntungan: Rp {total_profit:,.2f}")
    st.write("### 🔧 Pemeriksaan Kendala")

    if kebutuhan_bahan <= b1 and kebutuhan_waktu <= b2:
        st.success("✅ Produksi memungkinkan dengan batasan saat ini.")
        st.success(f"Total bahan baku yang dibutuhkan: {kebutuhan_bahan} / tersedia: {b1}")
        st.success(f"Total waktu yang dibutuhkan: {kebutuhan_waktu} menit / tersedia: {b2} menit")
    else:
        st.error("❌ Produksi tidak memungkinkan!")
        if kebutuhan_bahan > b1:
            st.error(f"Bahan baku kurang! Dibutuhkan: {kebutuhan_bahan}, tersedia: {b1}")
        if kebutuhan_waktu > b2:
            st.error(f"Waktu tidak cukup! Dibutuhkan: {kebutuhan_waktu} menit, tersedia: {b2} menit")

    # GRAFIK VISUALISASI BATASAN
    x = np.linspace(0, 100, 400)
    y1 = (b1 - a1 * x) / a2
    y2 = (b2 - a3 * x) / a4

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label="Batasan Bahan Baku", color="blue")
    plt.plot(x, y2, label="Batasan Waktu", color="green")
    plt.fill_between(x, 0, np.minimum(y1, y2), where=(y1 >= 0) & (y2 >= 0), color="skyblue", alpha=0.5)
    plt.plot(x_fixed, y_fixed, 'ro', label="Rencana Produksi (40,20)")
    plt.xlabel("Risol Mayo")
    plt.ylabel("Risol Sayur")
    plt.title("Visualisasi Kendala Produksi")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
