import pickle

import streamlit as st

from streamlit_option_menu import option_menu


# loading saved models


diabetes_model = pickle.load(open('..\Models\diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('..\Models\heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('..\Models\parkinsons_model.sav', 'rb'))


# side bar for navigation


with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# diabetes prediction page


if (selected == 'Diabetes Prediction'):

    # page ttiel

    st.title('Diabetes Prediction using ML')

    # getting input data from user

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Insulin level')
    with col2:
        Insulin = st.text_input('Skin thickness value')
    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabtes Pedigree Function Value')

    with col2:
        Age = st.text_input("Age of the person")

    # code for prediction

    diab_diagnosis = ''

    if st.button('Diabtes Test Result'):

        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'

        else:
            diab_diagnosis = ' the person is non diabetic'

        st.success(diab_diagnosis)


# Heart Disease prediction

if (selected == 'Heart Disease Prediction'):

    # page ttiel

    st.title('Heart Disease  Prediction using ML')

    # getting input data from user

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('sex')

    with col3:
        cp = st.text_input('Chest Pain Types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Pressure >120 mg/dl')

    with col1:
        restecg = st.text_input(
            'Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input("Maximum Heart rate Achieved")

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:

        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:

        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:

        thal = st.text_input(
            'thal:0 = normal; 1 = fixed defect; 2 = reversible defect')

    # code for prediction

    heart_diagnosis = ''

    if st.button('Heart Diagnosis  Test Result'):

        heart_prediction = heart_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having Heart Disease'

        else:
            heart_diagnosis = ' the person does not have any heart disease'

        st.success(heart_diagnosis)


# Parkinsons  Disease prediction

if (selected == 'Parkinsons Prediction'):

    # page ttiel

    st.title('Parkisnons Disease  Prediction using ML')

    # getting input data from user

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP-Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP-Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP-Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP-Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP-Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP-RAP')

    with col2:
        PPQ = st.text_input(
            'MDVP-PPQ')

    with col3:
        DDP = st.text_input("Jitter-DDP")

    with col4:
        Shimmer = st.text_input('MDVP-Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP-Shimmer_dB ')
    with col1:

        APQ3 = st.text_input('Shimmer-APQ3')
    with col2:

        APQ5 = st.text_input('Shimmer-APQ5')

    with col3:

        APQ = st.text_input('MDVP-APQ')
    with col4:
        DDA = st.text_input('Shimmer-DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for prediction

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Diagnosis  Test Result'):

        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkisnons_diagnosis = 'The person is having Parkisnons Disease'

        else:
            parkisnons_diagnosis = ' the person does not have any Parkinsons disease'

        st.success(parkinsons_diagnosis)
