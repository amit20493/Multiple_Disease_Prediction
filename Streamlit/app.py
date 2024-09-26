pip install streamlit-option-menu
 
import pickle

import streamlit as st

from streamlit_option_menu import option_menu


# loading saved models


diabetes_model = pickle.load(open('..\Models\diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('..\Models\heart_model.sav', 'rb'))
cancer_model = pickle.load(open('..\Models\cancer_model.sav', 'rb'))


# side bar for navigation


with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast cancer Prediction'],
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


# Breast cancer  Disease prediction

if (selected == 'Breast cancer Prediction'):

    # page ttiel

    st.title('Breast Cancer Prediction using ML')

    # getting input data from user

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mean_radius = st.text_input('mean radius')

    with col2:
        mean_texture = st.text_input('mean texture')

    with col3:
        mean_perimeter = st.text_input('mean perimeter')

    with col4:
        mean_area = st.text_input('mean area')
    with col5:
        mean_smoothness = st.text_input('mean smoothness')
    with col1:
        mean_compactness = st.text_input('mean compactness')

    with col2:
        mean_concavity = st.text_input(
            'mean concavity')

    with col3:
        mean_concave_points = st.text_input("mean concave points")

    with col4:
        mean_symmetry = st.text_input('mean symmetry')

    with col5:
        mean_fractal_dimension = st.text_input('mean fractal dimension')
    with col1:

        radius_error = st.text_input('radius error')
    with col2:

        texture_error = st.text_input('texture error')

    with col3:

        perimeter_error = st.text_input('perimeter error')
    with col4:
        area_error = st.text_input('area error')

    with col5:
        smoothness_error = st.text_input('smoothness error')

    with col1:
        compactness_error = st.text_input('compactness error')

    with col2:
        concavity_error = st.text_input('concavity error')

    with col3:
        concave_points_error = st.text_input('concave points error')

    with col4:
        symmetry_error = st.text_input('symmetry error')

    with col5:
        fractal_dimension_error = st.text_input('fractal dimension error')

    with col1:
        worst_radius = st.text_input('worst radius')

    with col2:
        worst_texture = st.text_input('worst texture')
    with col3:
        worst_perimeter = st.text_input('worst perimeter')
    with col4:
        worst_area = st.text_input('worst area')
    with col5:
        worst_smoothness = st.text_input('worst smoothness')
    with col1:
        worst_compactness = st.text_input('worst compactness')
    with col2:
        worst_concavity = st.text_input('worst concavity')

    with col3:
        worst_concave_points = st.text_input('worst concave points')
    with col4:
        worst_symmtery = st.text_input('worst symmetry')
    with col5:
        worst_fractal_dimension = st.text_input('worst fractal dimension')

    # code for prediction

    cancer_diagnosis = ''

    if st.button('Parkinsons Diagnosis  Test Result'):

        cancer_prediction = cancer_model.predict(
            [[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
              mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
              radius_error, texture_error, perimeter_error, area_error, smoothness_error,
              compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error,
              worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness,
              worst_concavity, worst_concave_points, worst_symmtery, worst_fractal_dimension]])

        if (cancer_prediction[0] == 1):
            cancer_diagnosis = 'The person is Benign'

        else:
            cancer_diagnosis = ' the person is Malignant'

        st.success(cancer_diagnosis)
