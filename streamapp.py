import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.title("Financial Management System")
st.write("A Machine Learning Tool to Detect Frauds in Transactoins")

type = st.selectbox(
    'Whats type of your Transaction',
    ('PAYMENT', 'TRANSFER', 'CASH_OUT', 'CASH_IN', 'DEBIT'))
step = st.number_input("What is the step", key=1)
nameorigin = st.text_input("Enter a nameorigin", key=1)
oldbalanceOrg = st.number_input("Enter a oldbalanceOrg", key=2)
newbalanceOrig = st.number_input("Enter a newbalanceOrig  ", key=3)
amount = st.number_input("Enter a amount", key=6)
nameDest = st.text_input("Enter a name_destination", key=3)
oldbalanceDest = st.number_input("Enter a oldbalanceDest", key=4)
newbalanceDest = st.number_input("Enter a newbalanceDest  ", key=5)

joblib_in = open("model_joblib", "rb")
clas = joblib.load(joblib_in)

df = pd.DataFrame({'type': [type], 'step': [step], 'nameorigin': [nameorigin],
                   'oldbalanceOrg': [oldbalanceOrg], 'newbalanceOrig': [newbalanceOrig],
                   'oldbalanceDest': [oldbalanceDest], 'newbalanceDest': [newbalanceDest],
                   'amount': [amount], 'nameDest': [nameDest]})

if st.button("Fraud ?"):
    result = clas.predict(df)
    st.success(f"{result}")
