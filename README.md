Heart Failure Prediction - Random Forest
Machine learning web app for predicting heart failure risk using Random Forest algorithm.

Tech Stack
1. Python 3.8+
2. Streamlit
3. Scikit-learn
4. Pandas
5. Joblib

Features
1. Real-time heart failure risk prediction
2. 11 medical parameters input
3. Random Forest classification model
4. Feature scaling with StandardScaler

Installation
1. Clone repository
git clone <repository-url>
cd "Web_Prediksi Gagal Jantung (RandomForest)"

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Usage
streamlit run app.py
Access at: http://localhost:8501

Project Structure
<img width="740" height="194" alt="image" src="https://github.com/user-attachments/assets/b4cefc54-84de-4455-892a-f270f2081d84" />


Input Parameters
1. Age - Patient age (years)
2. Sex - F/M
3. ChestPainType - TA/ATA/NAP/ASY
4. RestingBP - Blood pressure (mmHg)
5. Cholesterol - mg/dL
6. FastingBS - 0/1
7. RestingECG - Normal/ST/LVH
8. MaxHR - Maximum heart rate
9. ExerciseAngina - Y/N
10. Oldpeak - ST depression
11. ST_Slope - Up/Flat/Down

Model Info
Algorithm: Random Forest Classifier
Preprocessing: StandardScaler
Output: Binary classification (Risk/No Risk)
