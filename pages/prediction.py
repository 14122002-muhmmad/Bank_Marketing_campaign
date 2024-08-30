from PIL import Image
import requests
from io import BytesIO
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the preprocessor and model
with open(r'preprocessor.pkl, 'rb') as f:
    preprocessor = pickle.load(f)

with open(r'RFC3.pkl', 'rb') as f:
    model_data = pickle.load(f)
model = model_data['model']
threshold = model_data['threshold']

# Define all the expected feature names after preprocessing
expected_features = [
    'age', 'balance', 'last_contact_day', 'duration', 'campaign',
    'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
    'job_management', 'job_retired', 'job_self-employed', 'job_services',
    'job_student', 'job_technician', 'job_unemployed', 'marital_divorced',
    'marital_married', 'marital_single', 'month_apr', 'month_aug',
    'month_dec', 'month_feb', 'month_jan', 'month_jul', 'month_jun',
    'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep',
    'loan_0', 'loan_1', 'housing_0', 'housing_1', 'education_encoded'
]

# Define the input fields
def get_user_input():
    with st.form("user_input_form"):
        st.header("Client Information")
        
        # Split into columns for better layout
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=18, max_value=100, value=30)
            last_contact_day = st.number_input('Last Contact Day', min_value=1, max_value=31, value=15)
            campaign = st.number_input('Campaign', min_value=1, max_value=50, value=1)
        
        with col2:
            balance = st.number_input('Balance', min_value=-10000, max_value=100000, value=0)
            duration = st.number_input('Duration', min_value=0, max_value=5000, value=0)
        
        with col3:
            job = st.selectbox('Job', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
                                       'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed'])
            marital = st.selectbox('Marital Status', ['divorced', 'married', 'single'])
            month = st.selectbox('Last Contact Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])

        st.header("Additional Information")
        col4, col5 = st.columns(2)
        with col4:
            loan = st.selectbox('Loan', ['yes', 'no'])
        with col5:
            housing = st.selectbox('Housing', ['yes', 'no'])
        
        education = st.selectbox('Education', ['primary', 'secondary', 'tertiary'])

        user_data = {
            'age': age,
            'balance': balance,
            'last_contact_day': last_contact_day,
            'duration': duration,
            'campaign': campaign,
            'job': job,
            'marital': marital,
            'month': month,
            'loan': loan,
            'housing': housing,
            'education': education
        }
        
        # Submit button
        submit_button = st.form_submit_button(label='Predict')
        
    return pd.DataFrame(user_data, index=[0]), submit_button

# Display the input fields
st.markdown("<h1 style='text-align: center; color: Blue ;'> Will deposit or not </h1>",unsafe_allow_html=True)
st.image('https://storage.googleapis.com/gweb-cloudblog-publish/original_images/DataAnalytics.gif', use_column_width=True)
st.write('Fill in the details below to predict the likelihood of a successful marketing campaign.')

user_input, submit_button = get_user_input()

# Preprocess the input data
preprocessed_input = preprocessor.transform(user_input)

# Convert preprocessed input to DataFrame with expected feature names
preprocessed_df = pd.DataFrame(preprocessed_input, columns=expected_features)

# Make predictions
pred_proba = model.predict_proba(preprocessed_df)[:, 1]

# Display the result
threshold_ = threshold
if submit_button:
    st.write("---")
    st.header("Prediction Result")
    
    if pred_proba > threshold:
        st.success(f'**The client is likely to subscribe to a term deposit.**')
        st.image(r"https://blog.bankbazaar.com/wp-content/uploads/2017/02/SBT-cuts-lending-rates.gif",use_column_width=True)
    else:
        st.error(f'**The client is unlikely to subscribe to a term deposit.**\n\n The Client 👇')
        st.image(r"https://y.yarn.co/a89591cd-4d09-4b79-95a6-3e5e57a85d03_text.gif",use_column_width=True)
    st.write('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
