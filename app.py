import streamlit as st
clf=joblib.load('C:/Users/Vidhya Bro/Downloads/loan.joblib')

st.title('LOAN APP ZEBRA')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.numbeer_input('Enter Martial status 0:No 1:Yes')
ai=st.number_input('Enter Applicant Income in thousands')
la=st.number_input('Enter loan amount in thousands')

if st.button('PREDICT'):
    prediction=clf.predict([g,m,ai,la])
    if prediction=='y':
        st.txt('LOAN IS APPROVED')
    else:
        st.txt('LOAN IS REJECTED')
