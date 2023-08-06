# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:08:45 2023

@author: Vasundhra Srivastava
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model = pickle.load(open('C:/Users/Vasundhra Srivastava/Desktop/multiple disease prediction system/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Vasundhra Srivastava/Desktop/multiple disease prediction system/saved models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/Vasundhra Srivastava/Desktop/multiple disease prediction system/saved models/parkinsons_model.sav', 'rb'))



#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Emergency Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # Page Title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
        
    # code for prediction
    diab_diagnosis = ''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic and needs emergency assistance'
            
        else:
            diab_diagnosis = 'The person is not Diabetic and does not need emergency assistance'
    
    st.success(diab_diagnosis)
    
    

        
    
    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction')
    
    # getting the input data from user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the person')
        
    with col2:
        sex= st.text_input('Sex of the person')
        
    with col3:
        cp = st.text_input('cp level')
    
    with col1:
        trestbps = st.text_input('Resting Blood pressure value')
    
    with col2:
        chol = st.text_input('Cholestrol Level')
    
    with col3:
        fbs = st.text_input('FBS Value')
    
    with col1:
        thalach = st.text_input('Thalach value')
        
    with col2:
        restecg = st.text_input('Rest ECG value')
        
    with col3:
        exang = st.text_input('Exchange value')
    
    with col1:
        oldpeak = st.text_input('Oldpeak value')
        
    with col2:
        slope = st.text_input('Slope value')
        
    with col3:
        ca = st.text_input('CA value')
        
    with col1: 
        thal = st.text_input('Thalassemia value')
        
        
    # code for prediction
    heart_diagnosis = ''
    
    #creating button for prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person has a heart disease and needs emergency assistance'
            
        else:
            heart_diagnosis = 'The person does not have a heart disease and does not need emergency assistance'
    
    st.success(heart_diagnosis)
    
    
    
    
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction')
    
    # getting the input data from user
    # columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo value')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi value')
        
    with col3:
        flo = st.text_input('MDVP:Flo value')
    
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
         Shimmer = st.text_input('MDVP:Shimmer')
         
    with col5:
         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
    
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
    
    with col2:
        RDPE = st.text_input('RDPE')
        
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
    park_diagnosis = ''
    
    #creating button for prediction
    
    if st.button('Parkinsons Test Result'):
        park_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RDPE, DFA, spread1, spread2, D2, PPE]])
        
        if (park_prediction[0]==1):
            park_diagnosis = 'The person has parkinsons disease and needs emergency assistance'
            
        else:
            park_diagnosis = 'The person does not have parkinsons disease and does not need emergency assistance'
    
    st.success(park_diagnosis)
    
    

    