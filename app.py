import streamlit as st
import numpy as np
import joblib
from streamlit_lottie import st_lottie 
import json 

# Load model
model = joblib.load("model/model.pkl")
scaler = joblib.load('model/scaler.pkl')

st.set_page_config(page_title="Heart Aware", layout="wide", page_icon="🫀")
with open("Heart.json", "r") as f:
    heart_animation = json.load(f)

col1, col2 = st.columns([0.1, 1])  

with col1:
    st_lottie(heart_animation, height=100, width=100, key="heart") 

with col2:
    st.title("Heart Disease Awareness & Prediction")

# Red box for the description
st.markdown("""
<div style='background-color: rgba(244, 67, 54, 0.15); border-left: 5px solid #f44336; padding: 15px; margin-bottom: 25px; border-radius: 5px;'>
<p style='margin: 0; color: #ffffff;'>Heart disease is the <strong>#1 cause of death worldwide</strong>. Early detection and healthy lifestyle choices can make a difference. Learn about the risks and assess your own with our prediction tool below.</p>
</div>
""", unsafe_allow_html=True)

    
# styling
st.markdown("""
<style>

h1 {
    color: white;
    display: flex;
    align-items: center; 
    margin-top: 0; 
    margin-bottom: 0;
    margin-left:-60px;
}
        
h2 {
    color: white;
}
h3 {
    color: white;
    font-size: 30px;
    margin-bottom: 10px;
}
p{
    font-size: 23px;
}
            
[data-testid="stHorizontalBlock"] {
    gap: 15px; 
}
            
[data-testid="stTab"] > div[data-testid="stMarkdownContainer"] p {
    font-size: 20px; 
    font-weight: 600; 
    margin-right: 15px;  
    padding: 10px 20px
}
            
            
[data-baseweb="tab-panel"] p,
[data-baseweb="tab-panel"] li {
    font-size: 23px;
}
.stButton>button {
    background-color: white;
    color: black;
    border: 2px solid #ccc;
    border-radius: 5px;
    font-size: 18px;
    font-weight: bold;
    padding: 8px 16px;
}

li[role="option"] {
    padding: 10px 10px;
    display: flex;
    align-items: center;
}
            
[data-testid="stSelectbox"] label p {
    font-size: 23px;
    font-weight: 500;
}

[data-testid="stSelectbox"] {
    max-width: 650px; 
    margin-bottom: 25px; 
}
            
.st-dj.st-ay.st-dk.st-dl.st-cz.st-cd.st-dm.st-bx.st-dn {
    font-size: 19px;    
}
            

.stSlider {
    max-width: 600px;
}
[data-testid="stNumberInput"] label p {
    font-size: 23px;
    font-weight: 500;
}
[data-testid="stNumberInputContainer"] {
    max-width: 650px;
    height: 68px; 
    margin-bottom: 25px;
    
}
[data-testid="stNumberInputField"] {
    font-size: 18px;
    height: 68px;
    width: 250px;
    padding: 10px 15px;
    border-radius: 8px;
}
[data-testid="stSlider"] label p {
    font-size: 23px;
    font-weight: 500;
}
[data-testid="stSliderThumbValue"] {
    font-size: 20px;
    top: -35px;  
}
[data-baseweb="slider"] > div:first-child {
    margin-top: 30px;
    padding-top: 20px;
}

[data-testid="stSliderTickBar"] {
    font-size: 20px;
}
            
[data-testid="stSlider"] {
    margin-bottom: 20px;
    max-width: 600px;
}
            
.health-factors-header {
    display: flex;
    align-items: flex-start; 
    gap: 8px;
}
.info-icon-container {
    display: inline-block;
    margin-top: 0px; 
    margin-left: 1530px; 
    position: relative;
    cursor: pointer;
    font-size: 20px; 
}
.tooltip-table {
    display: none;
    position: absolute;
    z-index: 100;
    background-color: #000;
    color: #fff;
    padding: 12px;
    width: 750px;
    top: 0;
    left: -770px; /* Show to the left of the icon */
    border-radius: 8px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
}
.info-icon-container:hover .tooltip-table {
    display: block;
}
.tooltip-table table {
    width: 100%;
    border-collapse: collapse;
    color: white;
}
.tooltip-table th, .tooltip-table td {
    border: 1px solid #444;
    padding: 6px;
    text-align: center;
}
.tooltip-table th {
    background-color: #222;
    font-weight: bold;
}
            
           
</style>
""", unsafe_allow_html=True)

# Heart Disease Information Tabs
tabs = st.tabs(["What is Heart Disease?", "Symptoms", "Risk Factors", "Prevention Tips"])
with tabs[0]:
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
    st.image("images/diagram.png", width=500)
    st.markdown("""
    Heart disease refers to conditions that involve narrowed or blocked blood vessels, which can lead to a heart attack, chest pain or stroke. Common types include coronary artery disease, heart rhythm problems, and heart defects.

    Several health factors can increase the risk of developing heart disease:
    <ul>
      <li>
        <strong>Cholesterol (HDL & LDL):</strong>
        <ul>
          <li><strong>LDL (bad cholesterol):</strong> Can build up in the walls of your arteries, making them narrow and hard. This blocks blood flow to the heart.</li>
          <li><strong>HDL (good cholesterol):</strong> Helps remove LDL from your blood. Low HDL levels mean less protection for your heart.</li>
        </ul>
      </li>
      <li>
        <strong>Triglyceride Level:</strong>
        High triglycerides (a type of fat in your blood) can also lead to plaque buildup in the arteries. This increases the chance of heart disease, especially when combined with high LDL or low HDL.
      </li>
      <li>
        <strong>Fasting Blood Sugar:</strong>
        High blood sugar, often seen in diabetes, can damage blood vessels and the nerves that control the heart. Over time, this raises the risk of heart disease.
      </li>
      <li>
        <strong>CRP Level (C-Reactive Protein):</strong>
        CRP shows inflammation in your body. When CRP is high, it may mean your blood vessels are inflamed, which can speed up the process of artery blockage.
      </li>
      <li>
        <strong>Homocysteine Level:</strong>
        High homocysteine levels can damage the lining of the arteries and increase the risk of blood clots. This raises the chance of a heart attack or stroke.
      </li>
      <li>
        <strong>Blood Pressure:</strong>
        High blood pressure (also called hypertension) forces your heart to work harder to pump blood. Over time, it damages the arteries and increases the risk of heart disease, heart attack, or stroke.
      </li>
    </ul>
    """, unsafe_allow_html=True)
with tabs[1]:
    st.write("""
    Common symptoms include:
    - Chest pain or discomfort
    - Shortness of breath
    - Fatigue
    - Irregular heartbeat
    """)
with tabs[2]:
    st.write("""
    Risk factors include:
    - High blood pressure and cholesterol
    - Smoking
    - Diabetes
    - Obesity
    - Lack of physical activity
    - Family history
    """)
with tabs[3]:
    st.write("""
    To reduce your risk:
    - Eat a heart-healthy diet
    - Exercise regularly
    - Avoid smoking
    - Manage stress
    - Get regular checkups
    """)

st.markdown("---")
st.header("Risk Assessment Tool")

with st.form("prediction_form"):
    # Section 1: Basic Information
    st.subheader("🔴 Basic Information")
    age = st.number_input("Age", min_value=1, max_value=120, placeholder="Please enter age")
    gender = st.selectbox("Gender", ["Female", "Male"])
    smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
    family_hd = st.selectbox("Family history of heart disease?", ["Yes", "No"])

    st.markdown("---")
    
    # Section 2: Health Factors
    st.markdown("""
    <div class="health-factors-header">
    <h3>🔴 Health Factors</h3>
    <div class="info-icon-container">ℹ️
        <div class="tooltip-table">
            <table>
                <tr>
                    <th>Factor</th>
                    <th>Low</th>
                    <th>Normal</th>
                    <th>High</th>
                </tr>
                <tr><td>Blood Pressure</td><td>&lt; 90/60</td><td>90–120 / 60–80</td><td>&gt; 140/90</td></tr>
                <tr><td>Cholesterol</td><td>-</td><td>&lt; 200 mg/dL</td><td>&gt;= 240 mg/dL</td></tr>
                <tr><td>BMI</td><td>&lt; 18.5</td><td>18.5 – 24.9</td><td>&gt;= 30</td></tr>
                <tr><td>Sleep Hours</td><td>&lt; 6 hrs</td><td>7 – 9 hrs</td><td>&gt; 10 hrs</td></tr>
                <tr><td>Triglyceride</td><td>-</td><td>&lt; 150 mg/dL</td><td>&gt;= 200 mg/dL</td></tr>
                <tr><td>Fasting Blood Sugar</td><td>&lt; 70</td><td>70 – 99 mg/dL</td><td>&gt;= 126 mg/dL</td></tr>
                <tr><td>CRP</td><td>-</td><td>&lt; 1 mg/L</td><td>&gt; 3 mg/L</td></tr>
                <tr><td>Homocysteine</td><td>&lt; 5</td><td>5 – 15 µmol/L</td><td>&gt; 15 µmol/L</td></tr>
            </table>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
    bp = st.number_input("Blood Pressure", min_value=0, placeholder="Please enter BP")
    chol = st.number_input("Cholesterol Level", min_value=0, placeholder="Please enter cholesterol level")
    bmi = st.number_input("BMI", min_value=0.0, placeholder="Please enter BMI")
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, placeholder="Please enter sleep hours")
    triglyceride = st.number_input("Triglyceride Level", min_value=0, placeholder="Please enter level")
    fbs = st.number_input("Fasting Blood Sugar", min_value=0, placeholder="Please enter sugar level")
    crp = st.number_input("CRP Level (C-reactive protein)", min_value=0.0, placeholder="Please enter CRP level")
    homo = st.number_input("Homocysteine Level", min_value=0.0, placeholder="Please enter value")
    diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])
    high_bp = st.selectbox("Do you have high blood pressure?", ["No", "Yes"])
    low_hdl = st.selectbox("Do you have low HDL cholesterol?", ["Yes", "No"])
    high_ldl = st.selectbox("Do you have high LDL cholesterol?", ["No", "Yes"])

    st.markdown("---")
    
    # Section 3: Lifestyle Factors
    st.subheader("🔴 Lifestyle Factors")
    exercise_encoded = st.slider("Exercise Habits", 0, 2, 1, help="0 = Never, 1 = Sometimes, 2 = Often")
    stress_encoded = st.slider("Stress Level", 0, 2, 1, help="0 = None, 1 = Mild, 2 = High")
    sugar_encoded = st.slider("Sugar Intake", 0, 2, 1, help="0 = Low, 1 = Moderate, 2 = High")
    alcohol_encoded = st.slider("Alcohol Intake", 0, 2, 1, help="0 = Never, 1 = Sometimes, 2 = Frequent")

    st.markdown("---")


    # Center the Predict button
    col1, col2, col3 = st.columns([4, 1, 4])
    with col2:
        submitted = st.form_submit_button("Predict")

# Prediction Logic
if submitted:
    gender_female = 1 if gender == "Female" else 0
    gender_male = 1 if gender == "Male" else 0
    smoking_no = 1 if smoking == "No" else 0
    smoking_yes = 1 if smoking == "Yes" else 0
    family_hd_yes = 1 if family_hd == "Yes" else 0
    family_hd_no = 1 if family_hd == "No" else 0
    diabetes_yes = 1 if diabetes == "Yes" else 0
    diabetes_no = 1 if diabetes == "No" else 0
    high_bp_no = 1 if high_bp == "No" else 0
    high_bp_yes = 1 if high_bp == "Yes" else 0
    low_hdl_yes = 1 if low_hdl == "Yes" else 0
    low_hdl_no = 1 if low_hdl == "No" else 0
    high_ldl_no = 1 if high_ldl == "No" else 0
    high_ldl_yes = 1 if high_ldl == "Yes" else 0

    input_data = np.array([[age, bp, chol, bmi, sleep_hours, triglyceride, fbs, crp, homo,
                            gender_female, gender_male,
                            smoking_no, smoking_yes,
                            family_hd_no, family_hd_yes,
                            diabetes_no, diabetes_yes,
                            high_bp_no, high_bp_yes,
                            low_hdl_no, low_hdl_yes,
                            high_ldl_no, high_ldl_yes,
                            exercise_encoded, stress_encoded, sugar_encoded, alcohol_encoded]])
    
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)[0]
    probabilities = model.predict_proba(input_data_scaled)[0]

    st.markdown("---")
    st.subheader("Your Result:")
    with st.container():
        if prediction == 1:
            st.markdown(f"""
            <div style="padding: 1rem; border-left: 6px solid #e63946; background-color: rgba(230, 57, 70, 0.1); border-radius: 6px;">
                <h4 style="color: #b00020;">⚠️ Risk Detected</h4>
                <p>You may be at risk of <strong>Heart Disease</strong>.</p>
                <p><strong>Probability:</strong> {probabilities[1]:.2%}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="padding: 1rem; border-left: 6px solid #2a9d8f; background-color: rgba(42, 157, 143, 0.1); border-radius: 6px;">
                <h4 style="color: #00695c;">✅ No Significant Risk Detected</h4>
                <p>Your heart health looks good based on the input.</p>
                <p><strong>Probability:</strong> {probabilities[0]:.2%}</p>
            </div>
            """, unsafe_allow_html=True)
st.markdown("---")
st.markdown("© 2025 HeartAware. Built for education and awareness.")