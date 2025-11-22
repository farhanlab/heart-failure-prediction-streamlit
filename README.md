Heart Failure Prediction - Random Forest
Machine learning web app for predicting heart failure risk using Random Forest algorithm.

Tech Stack
• Python 3.8+
• Streamlit
• Scikit-learn
• Pandas
• Joblib

Features
• Real-time heart failure risk prediction
• 11 medical parameters input
• Random Forest classification model
• Feature scaling with StandardScaler

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
📁 venv/                           # Virtual environment (active)
📄 app.py                          # Main application
📄 random_forest_model.joblib      # Trained model
📄 scaler.joblib                   # Feature scaler
📄 feature_names.joblib            # Model features
📄 requirements.txt                # Dependencies

Input Parameters
Age - Patient age (years)
Sex - F/M
ChestPainType - TA/ATA/NAP/ASY
RestingBP - Blood pressure (mmHg)
Cholesterol - mg/dL
FastingBS - 0/1
RestingECG - Normal/ST/LVH
MaxHR - Maximum heart rate
ExerciseAngina - Y/N
Oldpeak - ST depression
ST_Slope - Up/Flat/Down

Model Info
Algorithm: Random Forest Classifier
Preprocessing: StandardScaler
Output: Binary classification (Risk/No Risk)
