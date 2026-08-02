import streamlit as st
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
import pandas as pd
import joblib
from datetime import datetime

from database import simpan_prediksi

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("rf_model_hasil_panen_tuned_v3.pkl")

# ==========================================
# JUDUL
# ==========================================

st.title("PREDIKSI HASIL PANEN PEPAYA BANGKOK")

st.divider()

st.subheader("Input Data Pertanian")

# ==========================================
# SESSION STATE
# ==========================================

if "hasil_prediksi" not in st.session_state:
    st.session_state.hasil_prediksi = None

if "sudah_prediksi" not in st.session_state:
    st.session_state.sudah_prediksi = False

# ==========================================
# INPUT DATA
# ==========================================

col1, col2 = st.columns(2)

with col1:

    suhu = st.number_input(
        "Suhu (°C)",
        min_value=0.0,
        value=25.0
    )

    ph_tanah = st.number_input(
        "pH Tanah",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    intensitas_cahaya = st.number_input(
        "Intensitas Cahaya",
        min_value=0.0,
        value=8.0
    )

with col2:

    curah_hujan = st.number_input(
        "Curah Hujan (mm)",
        min_value=0.0,
        value=250.0
    )

    dosis_pupuk = st.number_input(
        "Dosis Pupuk (kg)",
        min_value=0.0,
        value=50.0
    )

    umur_tanaman = st.number_input(
        "Umur Tanaman (bulan)",
        min_value=1,
        value=8
    )

st.markdown("")

# ==========================================
# PREDIKSI
# ==========================================

if st.button(
    "🔍 Prediksi",
    use_container_width=True
):

    sekarang = datetime.now()

    input_data = pd.DataFrame([{
        "tahun": sekarang.year,
        "bulan": sekarang.month,
        "curah_hujan": curah_hujan,
        "suhu": suhu,
        "ph_tanah": ph_tanah,
        "dosis_pupuk": dosis_pupuk,
        "intensitas_cahaya": intensitas_cahaya,
        "umur_tanaman": umur_tanaman
    }])

    hasil = model.predict(input_data)

    st.session_state.hasil_prediksi = float(hasil[0])

    st.session_state.sudah_prediksi = True

# ==========================================
# HASIL PREDIKSI
# ==========================================

if st.session_state.sudah_prediksi:

    st.divider()

    st.subheader("📊 Hasil Prediksi")

    st.success(
        f"### 🌱 Estimasi Hasil Panen\n\n"
        f"# {st.session_state.hasil_prediksi:.2f} Kg"
    )

    st.markdown("")

    if st.button("💾 Simpan", use_container_width=True):

        sekarang = datetime.now()

        simpan_prediksi(
            tanggal=sekarang.strftime("%Y-%m-%d"),
            suhu=suhu,
            curah_hujan=curah_hujan,
            ph_tanah=ph_tanah,
            dosis_pupuk=dosis_pupuk,
            intensitas_cahaya=intensitas_cahaya,
            umur_tanaman=umur_tanaman,
            hasil_prediksi=round(st.session_state.hasil_prediksi, 2)
        )

        st.success("✅ Data berhasil disimpan ke database.")