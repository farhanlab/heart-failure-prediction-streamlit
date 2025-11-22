import streamlit as st
import pandas as pd
import joblib

# === Load model, scaler, dan feature names ===
rf_clf = joblib.load("random_forest_model.joblib")
scaler = joblib.load("scaler.joblib")
feature_names = joblib.load("feature_names.joblib")

# === Konfigurasi Halaman ===
st.set_page_config(
    page_title="Prediksi Gagal Jantung",
    page_icon="❤️",
    layout="wide"
)

# === Header Aplikasi ===
st.markdown(
    """
    <div style='text-align:center;'>
        <h1>🫀 Prediksi Risiko Gagal Jantung</h1>
        <p style='font-size:18px;'>Analisis data medis dengan <strong>Random Forest</strong> untuk menilai risiko gagal jantung.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# === Form Input ===
st.header("Masukkan Data Pasien")
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Umur (Age)", min_value=1, max_value=120, value=35, help="Masukkan umur pasien dalam tahun")
        Sex = st.selectbox("Jenis Kelamin (Sex)", ["F", "M"], help="F = Female, M = Male")
        ChestPainType = st.selectbox("Tipe Nyeri Dada (ChestPainType)", ["TA", "ATA", "NAP", "ASY"],
                                     help="TA = Typical Angina, ATA = Atypical Angina, NAP = Non-anginal Pain, ASY = Asymptomatic")
        RestingBP = st.number_input("Tekanan Darah Istirahat (RestingBP)", 60, 200, 120, help="Dalam mmHg")
        Cholesterol = st.number_input("Kolesterol (Cholesterol)", 100, 600, 200, help="Dalam mg/dL")
        FastingBS = st.selectbox("Gula Darah Puasa > 120 mg/dl? (FastingBS)", [0, 1],
                                 help="0 = Tidak, 1 = Ya")

    with col2:
        RestingECG = st.selectbox("Hasil ECG (RestingECG)", ["Normal", "ST", "LVH"], help="Normal / ST-T Abnormal / Left Ventricular Hypertrophy")
        MaxHR = st.number_input("Detak Jantung Maksimum (MaxHR)", 60, 210, 150, help="Nilai detak jantung maksimum saat tes")
        ExerciseAngina = st.selectbox("Nyeri Dada Saat Olahraga? (ExerciseAngina)", ["Y", "N"], help="Y = Ya, N = Tidak")
        Oldpeak = st.number_input("Depresi ST (Oldpeak)", 0.0, 10.0, 1.0, step=0.1, help="ST depression induced by exercise relative to rest")
        ST_Slope = st.selectbox("Kemiringan ST (ST_Slope)", ["Up", "Flat", "Down"], help="Kemiringan ST segment")

st.markdown("---")

# === Prediksi ===
if st.button("🔍 Prediksi Sekarang"):
    new_patient = pd.DataFrame([{
        "Age": Age,
        "Sex": Sex,
        "ChestPainType": ChestPainType,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": FastingBS,
        "RestingECG": RestingECG,
        "MaxHR": MaxHR,
        "ExerciseAngina": ExerciseAngina,
        "Oldpeak": Oldpeak,
        "ST_Slope": ST_Slope
    }])

    categorical_cols = ['Sex', 'ChestPainType', 'ExerciseAngina', 'ST_Slope', 'RestingECG']
    new_patient_encoded = pd.get_dummies(new_patient, columns=categorical_cols, drop_first=True)
    new_patient_aligned = new_patient_encoded.reindex(columns=feature_names, fill_value=0)
    new_patient_scaled = scaler.transform(new_patient_aligned)

    prediction = rf_clf.predict(new_patient_scaled)[0]
    probas = rf_clf.predict_proba(new_patient_scaled)[0]

    # === Hasil Prediksi dengan Card ===
    st.subheader("📊 Hasil Prediksi")
    if prediction == 1:
        st.markdown(
            f"""
            <div style='padding:20px; background-color:#FFCDD2; border-radius:10px;'>
                <h3 style='color:#B71C1C;'>⚠️ Terdeteksi Potensi Gagal Jantung</h3>
                <p>Probabilitas: <strong>{probas[1]:.2%}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='padding:20px; background-color:#C8E6C9; border-radius:10px;'>
                <h3 style='color:#1B5E20;'>✅ Tidak Terdeteksi Gagal Jantung</h3>
                <p>Probabilitas: <strong>{probas[0]:.2%}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Tampilkan Data Input
    with st.expander("📋 Lihat Data Pasien"):
        st.table(new_patient)

st.markdown("---")
st.caption("Dibuat oleh **Muhammad Farhan Nurkhaeri** — Model: Random Forest | Streamlit © 2025")
