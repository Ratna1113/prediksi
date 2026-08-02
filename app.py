import streamlit as st

st.set_page_config(
    page_title="PREDIPABA",
    page_icon="🍈",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==========================================
# HALAMAN WELCOME
# ==========================================

# ==========================================
# HALAMAN WELCOME
# ==========================================

# ======================
# GAMBAR
# ======================

kiri, tengah, kanan = st.columns([1, 1, 1])

with tengah:
    st.image("assets/pepaya baangkok.png", width=280)

# ======================
# JUDUL
# ======================

st.markdown(
    "<h1 style='text-align:center;'>Selamat Datang di Sistem PREDIPABA</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>Sistem Prediksi Hasil Panen Pepaya Bangkok</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center;font-size:18px;'>
    Aplikasi ini digunakan untuk membantu pengguna dalam memprediksi hasil panen pepaya Bangkok
    berdasarkan kondisi pertanian yang dimasukkan ke dalam sistem.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("🌱 Prediksi")

        st.write(
            """
            Melakukan prediksi hasil panen pepaya Bangkok
            berdasarkan data pertanian yang dimasukkan
            oleh pengguna.
            """
        )

with col2:

    with st.container(border=True):

        st.subheader("📋 Riwayat")

        st.write(
            """
            Menampilkan seluruh data hasil prediksi
            yang telah disimpan ke database serta
            dapat diunduh dalam format CSV.
            """
        )