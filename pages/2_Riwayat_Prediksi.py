import streamlit as st
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
from database import ambil_semua_prediksi, hapus_semua_prediksi

st.title(" RIWAYAT PREDIKSI HASIL PANEN PEPAYA BANGKOK")

st.markdown("---")

# ===========================
# Ambil Data
# ===========================

history = ambil_semua_prediksi()

if history.empty:

    st.info("Belum ada data prediksi.")

else:

    tampil = history[
        [
            "id_prediksi",
            "tanggal",
            "suhu",
            "curah_hujan",
            "ph_tanah",
            "dosis_pupuk",
            "intensitas_cahaya",
            "umur_tanaman",
            "hasil_prediksi"
        ]
    ]

    tampil.columns = [
        "ID Prediksi",
        "Tanggal",
        "Suhu (°C)",
        "Curah Hujan (mm)",
        "pH Tanah",
        "Dosis Pupuk (kg)",
        "Intensitas Cahaya",
        "Umur (bulan)",
        "Hasil Prediksi (Kg)"
    ]

    # ==========================
    # Format angka
    # ==========================

    tampil["Suhu (°C)"] = tampil["Suhu (°C)"].round(2)
    tampil["Curah Hujan (mm)"] = tampil["Curah Hujan (mm)"].round(2)
    tampil["pH Tanah"] = tampil["pH Tanah"].round(2)
    tampil["Dosis Pupuk (kg)"] = tampil["Dosis Pupuk (kg)"].round(2)
    tampil["Intensitas Cahaya"] = tampil["Intensitas Cahaya"].round(2)
    tampil["Hasil Prediksi (Kg)"] = tampil["Hasil Prediksi (Kg)"].round(2)

    # ==========================
    # Tampilkan tabel
    # ==========================

    st.dataframe(
        tampil,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("")

    csv = tampil.to_csv(index=False).encode("utf-8")

    st.download_button(
    ":material/download: Download Riwayat",
    csv,
    "riwayat_prediksi.csv",
    "text/csv",
    use_container_width=True
)

    st.markdown("")

    if st.button(
    "🗑 Hapus Semua Riwayat",
    type="primary",
    use_container_width=True
):
     hapus_semua_prediksi()
    st.rerun()
