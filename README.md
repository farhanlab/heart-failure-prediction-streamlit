# Heart Failure Prediction
Web app machine learning untuk memprediksi risiko gagal jantung menggunakan algoritma Random Forest, dibangun dengan Streamlit.

## Tech stack
- Python 3.8+
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## Fitur
- Prediksi risiko gagal jantung secara real-time
- Input 11 parameter medis
- Model klasifikasi Random Forest
- Feature scaling dengan StandardScaler

## Struktur proyek
```
venv/                        # Virtual environment (active)
app.py                       # Aplikasi utama
random_forest_model.joblib   # Model terlatih
scaler.joblib                # Feature scaler
feature_names.joblib         # Nama-nama fitur model
requirements.txt             # Dependencies
```

## Instalasi
Clone repo:
```bash
git clone <repo-url>
cd Web_Prediksi_Gagal_Jantung_RandomForest
```

Buat dan aktifkan virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Jalankan aplikasi:
```bash
streamlit run app.py
```
Aplikasi bisa diakses di [http://localhost:8501](http://localhost:8501)

## Parameter input
| No | Parameter | Keterangan |
|---|---|---|
| 1 | Age | Usia pasien (tahun) |
| 2 | Sex | F/M |
| 3 | ChestPainType | TA/ATA/NAP/ASY |
| 4 | RestingBP | Tekanan darah saat istirahat (mmHg) |
| 5 | Cholesterol | mg/dL |
| 6 | FastingBS | 0/1 |
| 7 | RestingECG | Normal/ST/LVH |
| 8 | MaxHR | Detak jantung maksimum |
| 9 | ExerciseAngina | Y/N |
| 10 | Oldpeak | ST depression |
| 11 | ST_Slope | Up/Flat/Down |

## Info model
- Algoritma: Random Forest Classifier
- Preprocessing: StandardScaler
- Output: Klasifikasi biner (Risk / No Risk)

## Penulis
Muhammad Farhan Nurkhaeri
