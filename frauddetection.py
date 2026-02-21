import streamlit as st
import pandas as pd
import joblib

def load_model():
    return joblib.load('fraud_detection_model.pkl')

model = load_model()


st.title('Transaction Fraud Detection System')
st.write('Enter transaction details to check if it\'s fraudulent')


st.subheader('Transaction Details')

col1, col2 = st.columns(2)

with col1:
    transaction_type = st.selectbox('Transaction Type', 
                                    ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
    amount = st.number_input('Amount', min_value=0.0, value=1000.0, step=100.0)
    oldbalanceOrg = st.number_input('Sender Old Balance', min_value=0.0, value=5000.0, step=100.0)
    newbalanceOrig = st.number_input('Sender New Balance', min_value=0.0, value=4000.0, step=100.0)

with col2:
    oldbalanceDest = st.number_input('Receiver Old Balance', min_value=0.0, value=2000.0, step=100.0)
    newbalanceDest = st.number_input('Receiver New Balance', min_value=0.0, value=3000.0, step=100.0)
    
balancedifforg = oldbalanceOrg - newbalanceOrig
balancediffdest = newbalanceDest - oldbalanceDest

st.write(f'**Sender Balance Change:** {balancedifforg:,.2f}')
st.write(f'**Receiver Balance Change:** {balancediffdest:,.2f}')


if st.button('🔍 Check Transaction', type='primary'):
    input_data = pd.DataFrame({
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'balancedifforg': [balancedifforg],
        'balancediffdest': [balancediffdest],
        'type': [transaction_type]
    })
    
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    
    st.divider()
    if prediction == 1:
        st.error(' **FRAUDULENT TRANSACTION DETECTED!**')
        st.write(f'Fraud Probability: **{probability[1]*100:.2f}%**')
    else:
        st.success('✅ **Transaction appears LEGITIMATE**')
        st.write(f'Fraud Probability: **{probability[1]*100:.2f}%**')
