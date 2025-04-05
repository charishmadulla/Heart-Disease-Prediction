import streamlit as st
import joblib

cl=joblib.load('hdp.joblib')

st.title('HEART DISEASE PREDICTION')

a=st.number_input('Enter Age')
c=st.number_input('Enter no.of Cigarettes per day')
chl=st.number_input('Enter total Cholestrol value')
sbp=st.number_input('Enter Systolic BP')
dbp=st.number_input('Enter Diastolic BP')
bmi=st.number_input('Enter Body Mass Index')
hr=st.number_input('Enter HeartRate')
g=st.number_input('Enter Glucose levels')
if st.button('PREDICT'):
    prediction=cl.predict([[a,c,chl,sbp,dbp,bmi,hr,g]])
    if prediction=='Y':
        st.text('MIGHT SUFFER WITH HEART DISEASE')
    else:
        st.text('MIGHT NOT SUFFER WITH HEART DISEASE')
