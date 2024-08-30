import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st. set_page_config(layout="wide")


df = pd.read_csv(r"G:\Machine_learning\Final_Project\Bank_Marketing_Cleaned.csv")
st.markdown("<h1 style='text-align: center; color: Purple ;'> Answers to Busness Question using 📊s </h1>",unsafe_allow_html=True)

col11, col12,col13 = st.columns([2,4,1])
with col12:
    st.image('https://y.yarn.co/b774f0a9-4795-48df-89fe-091e0fb582e7_text.gif')

st.divider()

col1, col2, col3,  = st.columns([4,1,4])
with col1: 
    acc_dur_job = df[df['deposit'] == 1 ].groupby('job')['duration'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(acc_dur_job, x = 'job', y = 'duration',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.markdown("<h3 style='text-align: center; color: Green ;'>what is the average duration does each job take on phone to accept the offer to deposit ?</h3>",unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
  

    edu_dur = df[df['deposit'] == 1 ].groupby('education')['duration'].mean().sort_values(ascending=False).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does the level of education matter in this case (duration of call to persue )?</h3>",unsafe_allow_html=True)
    fig = px.pie(edu_dur,names='education',values='duration',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    last_cntact_deposite = df.groupby('last_contact_day')['deposit'].mean().sort_index(ascending=True).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>We have to keep in contact with customers ?</h3>",unsafe_allow_html=True)
    fig = px.line(last_cntact_deposite,x='last_contact_day',y='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    edu_balnce = df.groupby('education')['balance'].mean().sort_values(ascending=False).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does the level of education affect the balance in the account?</h3>",unsafe_allow_html=True)
    fig = px.pie(edu_balnce,names='education',values='balance',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    sunburst_data = df.groupby(['marital', 'education'])['deposit'].mean().reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does marital status and education level affect the decision to deposit?</h3>", unsafe_allow_html=True)
    fig = px.sunburst(sunburst_data, path=['marital', 'education'], values='deposit', color='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r, template='presentation')
    st.plotly_chart(fig, use_container_width=True)


with col3:
    marital_deposite = df.groupby('marital')['deposit'].mean().sort_values(ascending=False).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does the marital status affect the decision to deposit ?</h3>",unsafe_allow_html=True)
    fig = px.pie(marital_deposite,names='marital',values='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    housing_deposite = df.groupby('housing')['deposit'].mean().sort_values(ascending=False).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does having a housing loan affect the decision to deposit ?</h3>",unsafe_allow_html=True)
    fig = px.pie(housing_deposite,names='housing',values='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    loan_deposite = df.groupby('loan')['deposit'].mean().sort_values(ascending=False).reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does having a personal loan affect the decision to deposit ?</h3>",unsafe_allow_html=True)
    fig = px.pie(loan_deposite,names='loan',values='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r,template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    age_deposite = df.groupby('age')['deposit'].mean().reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does age affect the decision to deposit?</h3>",unsafe_allow_html=True)
    fig = px.line(age_deposite, x='age', y='deposit', color_discrete_sequence=px.colors.sequential.GnBu_r, template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    age_balance = df.groupby('age')['balance'].mean().reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does age affect the average balance?</h3>", unsafe_allow_html=True)
    fig = px.scatter(age_balance, x='age', y='balance', size='balance', color='balance',color_discrete_sequence=px.colors.sequential.GnBu_r, template='presentation')
    st.plotly_chart(fig, use_container_width=True)

    


with col3:
    # a graph shows the relation between the duration of the call and the decision to deposit
    duration_deposite = df.groupby('duration')['deposit'].mean().reset_index()
    st.markdown("<h3 style='text-align: center; color: Green ;'>Does the duration of the call affect the decision to deposit?</h3>",unsafe_allow_html=True)
    fig = px.scatter(duration_deposite, x='duration', y='deposit', size='deposit', color='deposit',color_discrete_sequence=px.colors.sequential.GnBu_r, template='presentation')
    st.plotly_chart(fig, use_container_width=True)   
        
   
   





    
 
    
