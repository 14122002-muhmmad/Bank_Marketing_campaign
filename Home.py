import streamlit as st
import pickle
import numpy as np
import pandas as pd
df = pd.read_csv(r'G:\Machine_learning\Final_Project\Bank_Marketing_Cleaned.csv')
st.markdown("<h1 style='text-align: center; color: Green ;'>Bank Marketing Campaign </h1>",unsafe_allow_html=True)
#i want to write description of the data and give the link of it
st.image('https://media.licdn.com/dms/image/v2/C4E12AQGyUGK7U54nWw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1580024684661?e=1730332800&v=beta&t=Imyhey6O1aQNmR4WFiJB0vXfGeUfw0ohKelSf_327eQ', use_column_width=True)
st.markdown("<h3 style='text-align: center; color: Purple ;'>Description of the data</h3>",unsafe_allow_html=True)
st.markdown("""The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.""",unsafe_allow_html=True)
st.markdown("""- **<span style="color:darkslategray">Age</span>**: Age of the individual.
- **<span style="color:green">Job</span>**: Job category or occupation of the individual.
- **<span style="color:purple">Marital</span>**: Marital status.
- **<span style="color:orange">Education</span>**: Education level.
- **<span style="color:red">Default</span>**: Indicator of whether the individual has credit in default.
- **<span style="color:brown">Balance</span>**: Account balance.
- **<span style="color:teal">Housing</span>**: Indicator of whether the individual has a housing loan.
- **<span style="color:darkgreen">Loan</span>**: Indicator of whether the individual has a personal loan.
- **<span style="color:navy">Contact</span>**: Contact communication type (e.g., telephone, mobile).
- **<span style="color:darkred">Day_of_week</span>**: Day of the week when the contact was made.
- **<span style="color:darkorange">Month</span>**: Month in which the contact was made.
- **<span style="color:darkblue">Duration</span>**: Duration of the last contact in seconds.
- **<span style="color:darkpurple">Campaign</span>**: Number of contacts performed during this campaign.
- **<span style="color:maroon">Pdays</span>**: Number of days passed after the client was last contacted from a previous campaign.
- **<span style="color:olive">Previous</span>**: Number of contacts performed before this campaign.
- **<span style="color:darkcyan">Poutcome</span>**: Outcome of the previous marketing campaign.
- **<span style="color:magenta">Deposit</span>**: Indicator of whether the customer subscribed to a bank term deposit.
<style>
    h2 {
        color: #1f618d; /* Change color of header */
    }
    ul {
        list-style-type: none; /* Remove bullet points */
        padding-left: 0; /* Remove default padding */
    }
    li {
        margin-bottom: 10px; /* Add spacing between items */
    }
    li strong {
        color: #c0392b; /* Change color of bold text */
    }
</style>
""", unsafe_allow_html=True)
st.divider()
st.markdown("<h2 style='text-align: center; color: Green ;'>Data Sources</h2>",unsafe_allow_html=True)
st.markdown("[archive.ics](https://archive.ics.uci.edu/dataset/222/bank+marketing)",unsafe_allow_html=True)
st.markdown("[Kaggle](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)",unsafe_allow_html=True)
st.divider()
st.markdown("<h1 style='text-align: center; color: Green ;'>Sample from the Data</h1>",unsafe_allow_html=True)
st.dataframe(df.sample(10), width=800, height=400, use_container_width=True, hide_index=True )
st.markdown("<h1 style='text-align: center; color: Green ;'>Now time to explore data</h1>",unsafe_allow_html=True) 
