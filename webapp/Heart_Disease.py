
import pickle
import streamlit as st
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))




st.markdown("<h1 style='text-align: center; color: black;'>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)

add_bg_from_local("img.jpg")
col1, col2, col3 = st.columns(3)

with col1:
    age = float(st.number_input("Age: "))

with col2:
    sel = st.selectbox("Sex", ['Male', 'Female'])
    if sel=='Male':
        sex=0
    if sel == 'Female':
        sex = 1



with col3:
    cp = float(st.number_input("Chest Pain types:"))

with col1:
    trestbps = float(st.number_input('Resting Blood Pressure'))

with col2:
    chol = float(st.number_input('Serum Cholestoral in mg/dl'))

with col3:
    fbs = float(st.number_input('Fasting Blood Sugar > 120 mg/dl'))

with col1:
    restecg = float(st.number_input('Resting Electrocardiographic results'))

with col2:
    thalach = float(st.number_input('Maximum Heart Rate achieved'))

with col3:
    exang =float(st.number_input('Exercise Induced Angina'))

with col1:
    oldpeak = float(st.number_input('ST depression induced by exercise'))

with col2:
    slope = float(st.number_input('Slope of the peak exercise ST segment'))

with col3:
    ca = float(st.number_input('Major vessels colored by flourosopy'))

with col1:
    thal = float(st.number_input('thallium: 0 = normal; 1 = fixed defect; 2 = reversable defect'))




# code for Prediction
heart_diagnosis = ''

# creating a button for Prediction

if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[int(age), int(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])

    if (heart_prediction[0] == 1):
      st.markdown("<h3 style='text-align: center; color: black;'>The person have  heart disease</h3>", unsafe_allow_html=True)
    else:
      st.markdown("<h3 style='text-align: center; color: black;'>The person does not have any heart disease</h3>", unsafe_allow_html=True)


        
    
    






