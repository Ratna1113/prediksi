import sqlite3
import pandas as pd

DATABASE = "database.db"


# ===================================================
# MEMBUAT DATABASE DAN TABEL
# ===================================================

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediksi(

            id_prediksi INTEGER PRIMARY KEY AUTOINCREMENT,

            tanggal TEXT,

            suhu REAL,

            curah_hujan REAL,

            ph_tanah REAL,

            dosis_pupuk REAL,

            intensitas_cahaya REAL,

            umur_tanaman INTEGER,

            hasil_prediksi REAL

        )
    """)

    conn.commit()

    conn.close()


# ===================================================
# SIMPAN DATA
# ===================================================

def simpan_prediksi(
    tanggal,
    suhu,
    curah_hujan,
    ph_tanah,
    dosis_pupuk,
    intensitas_cahaya,
    umur_tanaman,
    hasil_prediksi
):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO prediksi(

            tanggal,

            suhu,

            curah_hujan,

            ph_tanah,

            dosis_pupuk,

            intensitas_cahaya,

            umur_tanaman,

            hasil_prediksi

        )

        VALUES(?,?,?,?,?,?,?,?)

    """,(

        tanggal,

        suhu,

        curah_hujan,

        ph_tanah,

        dosis_pupuk,

        intensitas_cahaya,

        umur_tanaman,

        hasil_prediksi

    ))

    conn.commit()

    conn.close()


# ===================================================
# AMBIL SELURUH DATA
# ===================================================

def ambil_semua_prediksi():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(

        "SELECT * FROM prediksi ORDER BY id_prediksi DESC",

        conn

    )

    conn.close()

    return df


# ===================================================
# HAPUS DATA
# ===================================================

def hapus_semua_prediksi():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM prediksi")

    conn.commit()

    conn.close()


# ===================================================
# MEMBUAT DATABASE SAAT DIJALANKAN
# ===================================================

create_database()