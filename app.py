'''import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://img.freepik.com/free-vector/various-timelines-flattening-curve_23-2148548838.jpg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes':pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/Diabetes_model.sav','rb')),
    'heart_disease': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/Thyroid_model.sav', 'rb'))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
    t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
    tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.success(thyroid_diagnosis)'''

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# Hide Streamlit UI elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Disease Prediction System") 
# Adding Background Image with Overlay
def set_bg():
    background_image_url = "https://img.freepik.com/free-vector/various-timelines-flattening-curve_23-2148548838.jpg"
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.6);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_bg()

# Load Models
models = {
    'diabetes':pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/Diabetes_model.sav','rb')),
    'heart_disease': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('/Users/keerthipriyareddy/Documents/projects/aicte/models/Thyroid_model.sav', 'rb'))
}

# Dropdown Menu
selected = st.sidebar.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
)

def display_input(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1)

# Prediction Logic
def predict_disease(model, features, message):
    prediction = model.predict([features])
    result = message if prediction[0] == 1 else f"The person does have {message.split(' ')[-1]}"
    st.success(result)

# UI for Each Disease
st.markdown(f"## {selected}")
st.write("Fill out the form below to get a prediction.")

if selected == 'Diabetes Prediction':
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = display_input('Pregnancies', 'Number of times pregnant', 'Pregnancies')
        Glucose = display_input('Glucose Level', 'Glucose concentration', 'Glucose')
        BloodPressure = display_input('Blood Pressure', 'Blood pressure value', 'BloodPressure')
        SkinThickness = display_input('Skin Thickness', 'Skin thickness value', 'SkinThickness')
    with col2:
        Insulin = display_input('Insulin', 'Insulin level', 'Insulin')
        BMI = display_input('BMI', 'Body Mass Index', 'BMI')
        DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'Heredity factor', 'DiabetesPedigreeFunction')
        Age = display_input('Age', 'Age of the person', 'Age')
    if st.button('Diabetes Test Result', use_container_width=True):
        predict_disease(models['diabetes'], [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age], 'The person is diabetic')

elif selected == "Heart Disease Prediction":

    col1, col2 = st.columns(2)
    with col1:
        age = display_input('Age', 'Age of the person', 'age')
        sex = display_input('Sex (1=Male, 0=Female)', 'Gender of the person', 'sex')
        cp = display_input('Chest Pain Type (0-3)', 'Type of chest pain', 'cp')
        trestbps = display_input('Resting Blood Pressure', 'Blood pressure at rest', 'trestbps')
        chol = display_input('Serum Cholesterol (mg/dl)', 'Cholesterol level', 'chol')
        fbs = display_input('Fasting Blood Sugar (>120 mg/dl: 1, else 0)', 'Fasting blood sugar', 'fbs')
    
    with col2:
        restecg = display_input('Resting ECG (0-2)', 'Resting electrocardiographic results', 'restecg')
        thalach = display_input('Max Heart Rate Achieved', 'Maximum heart rate achieved', 'thalach')
        exang = display_input('Exercise Induced Angina (1=Yes, 0=No)', 'Exercise-induced chest pain', 'exang')
        oldpeak = display_input('ST Depression Induced by Exercise', 'ST depression value', 'oldpeak')
        slope = display_input('Slope of Peak Exercise ST Segment (0-2)', 'Slope value', 'slope')
        ca = display_input('Number of Major Vessels (0-3)', 'Number of major vessels', 'ca')
        thal = display_input('Thalassemia (0-3)', 'Thalassemia category', 'thal')

    if st.button("Heart Disease Test Result", use_container_width=True):
        predict_disease(models['heart_disease'], [
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
        ], "The person may have not heart disease")

elif selected == "Parkinsons Prediction":

    col1, col2 = st.columns(2)
    with col1:
        fo = display_input('MDVP:Fo(Hz)', 'Fundamental frequency', 'fo')
        fhi = display_input('MDVP:Fhi(Hz)', 'Highest fundamental frequency', 'fhi')
        flo = display_input('MDVP:Flo(Hz)', 'Lowest fundamental frequency', 'flo')
        jitter_percent = display_input('MDVP:Jitter(%)', 'Jitter percentage', 'Jitter_percent')
        jitter_abs = display_input('MDVP:Jitter(Abs)', 'Absolute jitter', 'Jitter_abs')
        RAP = display_input('MDVP:RAP', 'Relative amplitude perturbation', 'RAP')
        PPQ = display_input('MDVP:PPQ', 'Pitch perturbation quotient', 'PPQ')
        jitter_ddp = display_input('Jitter:DDP', 'Jitter DDP', 'Jitter_ddp')
        shimmer = display_input('MDVP:Shimmer', 'Shimmer', 'Shimmer')
        shimmer_db = display_input('MDVP:Shimmer(dB)', 'Shimmer in dB', 'Shimmer_db')
        shimmer_apq3 = display_input('Shimmer:APQ3', 'Three-point amplitude perturbation quotient', 'Shimmer_apq3')

    with col2:
        shimmer_apq5 = display_input('Shimmer:APQ5', 'Five-point amplitude perturbation quotient', 'Shimmer_apq5')
        mdvp_apq = display_input('MDVP:APQ', 'Amplitude perturbation quotient', 'MDVP_APQ')
        shimmer_dda = display_input('Shimmer:DDA', 'Shimmer DDA', 'Shimmer_dda')
        NHR = display_input('NHR', 'Noise-to-Harmonic ratio', 'NHR')
        HNR = display_input('HNR', 'Harmonics-to-Noise ratio', 'HNR')
        RPDE = display_input('RPDE', 'Recurrence period density entropy', 'RPDE')
        DFA = display_input('DFA', 'Detrended fluctuation analysis', 'DFA')
        spread1 = display_input('Spread1', 'Spread1 value', 'spread1')
        spread2 = display_input('Spread2', 'Spread2 value', 'spread2')
        D2 = display_input('D2', 'D2 measure', 'D2')
        PPE = display_input('PPE', 'Pitch period entropy', 'PPE')

    if st.button("Parkinson's Test Result", use_container_width=True):
        predict_disease(models['parkinsons'], [
            fo, fhi, flo, jitter_percent, jitter_abs, RAP, PPQ, jitter_ddp, shimmer, shimmer_db, shimmer_apq3,
            shimmer_apq5, mdvp_apq, shimmer_dda, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ], "The person may have not Parkinson's disease")

elif selected == 'Lung Cancer Prediction':

    col1, col2 = st.columns(2)
    with col1:
        gender = display_input('Gender (1=Male, 0=Female)', 'Select Gender', 'gender')
        age = display_input('Age', 'Age of the person', 'age')
        smoking = display_input('Smoking (1=Yes, 0=No)', 'Smoking history', 'smoking')
        yellow_fingers = display_input('Yellow Fingers (1=Yes, 0=No)', 'Yellow stains on fingers', 'yellow_fingers')
        anxiety = display_input('Anxiety (1=Yes, 0=No)', 'History of anxiety', 'anxiety')
        peer_pressure = display_input('Peer Pressure (1=Yes, 0=No)', 'Influence of peers on habits', 'peer_pressure')
        chronic_disease = display_input('Chronic Disease (1=Yes, 0=No)', 'Any pre-existing chronic disease', 'chronic_disease')
        fatigue = display_input('Fatigue (1=Yes, 0=No)', 'Frequent fatigue', 'fatigue')
    
    with col2:
        allergy = display_input('Allergy (1=Yes, 0=No)', 'History of allergies', 'allergy')
        wheezing = display_input('Wheezing (1=Yes, 0=No)', 'Frequent wheezing', 'wheezing')
        alcohol_consuming = display_input('Alcohol Consumption (1=Yes, 0=No)', 'Drinks alcohol frequently', 'alcohol_consuming')
        coughing = display_input('Coughing (1=Yes, 0=No)', 'Persistent coughing', 'coughing')
        shortness_of_breath = display_input('Shortness of Breath (1=Yes, 0=No)', 'Experiences difficulty breathing', 'shortness_of_breath')
        swallowing_difficulty = display_input('Swallowing Difficulty (1=Yes, 0=No)', 'Experiences trouble swallowing', 'swallowing_difficulty')
        chest_pain = display_input('Chest Pain (1=Yes, 0=No)', 'Frequent chest pain', 'chest_pain')

    if st.button('Lung Cancer Test Result', use_container_width=True):
        predict_disease(models['lung_cancer'], [
            gender, age, smoking, yellow_fingers, anxiety, peer_pressure, 
            chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, 
            coughing, shortness_of_breath, swallowing_difficulty, chest_pain
        ], 'The person might have lung cancer')



elif selected == 'Hypo-Thyroid Prediction':
   
    col1, col2 = st.columns(2)
    with col1:
        age = display_input('Age', 'Age of the person', 'age')
        sex = display_input('Sex (1=Male, 0=Female)', 'Gender', 'sex')
        on_thyroxine = display_input('On Thyroxine (1=Yes, 0=No)', 'Currently on Thyroxine medication', 'on_thyroxine')

    with col2:
        TSH = display_input('TSH Level', 'Thyroid-Stimulating Hormone level', 'TSH')
        T3_measured = display_input('T3 Measured (1=Yes, 0=No)', 'Was T3 measured?', 'T3_measured')
        T3 = display_input('T3 Level', 'Triiodothyronine level', 'T3')
        TT4 = display_input('TT4 Level', 'Total Thyroxine level', 'TT4')

    if st.button('Hypo-Thyroid Test Result', use_container_width=True):
        predict_disease(models['thyroid'], [age, sex, on_thyroxine, TSH, T3_measured, T3, TT4], 'The person may have hypothyroid')




st.markdown("""---
### Disclaimer
 Consult a medical professional for more detailed and accurate diagnosis.
""")

