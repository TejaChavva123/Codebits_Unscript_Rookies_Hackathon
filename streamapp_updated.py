import streamlit as st
import pandas as pd
import joblib



st.title("Financial Management System")
st.write("A Machine Learning Tool to Detect Frauds in Transactoins")

type1 = st.selectbox(
    'Whats type of your Transaction',
    ('PAYMENT', 'TRANSFER', 'CASH_OUT', 'CASH_IN', 'DEBIT'))
t = type1
step = st.number_input("What is the step", key=1)
nameorigin = st.text_input("Enter a nameorigin", key=1)
oldbalanceOrg = st.number_input("Enter a oldbalanceOrg", key=2)
newbalanceOrig = st.number_input("Enter a newbalanceOrig  ", key=3)
amount = st.number_input("Enter a amount", key=6)
nameDest = st.text_input("Enter a name_destination", key=3)
oldbalanceDest = st.number_input("Enter a oldbalanceDest", key=4)
newbalanceDest = st.number_input("Enter a newbalanceDest  ", key=5)

def func1(x):
    if (t==x):
        return 1
    else:
        return 0

joblib_in = open("model_joblib", "rb")
clas = joblib.load(joblib_in)
df = pd.DataFrame({'step': [step], 'amount': [amount],'newbalanceOrig': [newbalanceOrig], 'newbalanceDest': [newbalanceDest],'type_CASH_IN':[func1('CASH_IN')], 'type_CASH_OUT':[func1('CASH_OUT')],'type_DEBIT':[func1('DEBIT')],
                    'type_PAYMENT':[func1('PAYMENT')],'errorOrg':[newbalanceOrig-oldbalanceOrg],'errorDest':[oldbalanceDest-newbalanceDest]
                  })

if st.button("Fraud ?"):
    result = clas.predict(df)
    if (result==0):
        st.success('Transaction is not fraud')
    else:
        st.success('Transaction is fraud')
    # st.success(f"{result}")
