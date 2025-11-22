Aplikasi web sederhana untuk memprediksi risiko gagal jantung menggunakan algoritma Random Forest. Aplikasi ini menganalisis data medis pasien dan memberikan prediksi risiko.

🎯 Fitur
Prediksi Real-time: Input data pasien dan dapatkan prediksi risiko gagal jantung secara instan
Model Machine Learning: Menggunakan algoritma Random Forest yang telah dilatih dengan datasets terkait
Interface User-Friendly: Antarmuka web yang mudah digunakan dengan Streamlit
Visualisasi Data: Menampilkan hasil prediksi dengan jelas

📋 Parameter Input
Aplikasi ini menerima berbagai parameter medis pasien:
Umur (Age): Usia pasien dalam tahun
Jenis Kelamin (Sex): F (Female) atau M (Male)
Tipe Nyeri Dada (ChestPainType): TA, ATA, NAP, ASY
Tekanan Darah Istirahat (RestingBP): Dalam mmHg
Kolesterol (Cholesterol): Level kolesterol dalam mg/dL
Gula Darah Puasa (FastingBS): 0 atau 1
Hasil ECG (RestingECG): Normal, ST, LVH
Detak Jantung Maksimum (MaxHR): Detak per menit
Nyeri Dada Saat Olahraga (ExerciseAngina): Y atau N
Depresi ST (Oldpeak): Nilai numerik
Kemiringan ST (ST_Slope): Up, Flat, Down

🚀 Instalasi
Clone repository
bashgit clone <repository-url>
cd "Web_Prediksi Gagal Jantung (RandomForest)"

Buat virtual environment
bashpython -m venv venv

Aktifkan virtual environment
venv/Scripts/activate

Install dependencies
pip install -r requirements.txt

🎮 Cara Menjalankan
Pastikan virtual environment sudah aktif
Jalankan aplikasi dengan perintah:
streamlit run app.py

Aplikasi akan terbuka di browser pada http://localhost:8501

📦 Dependencies
streamlit: Framework untuk membuat web app
pandas: Library untuk manipulasi data
joblib: Untuk loading model machine learning
Dan library pendukung lainnya (lihat requirements.txt)
