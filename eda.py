import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#webapp title

st.markdown('''
# **Exploratory Data Analysis Web App**
            This app is developed by **me**
''')

#upload file 

with st.sidebar.header('upload your dataset here (.csv)'):
    uploaded_file = st.sidebar.file_uploader("Upload your dataset here (.csv)", type=["csv"])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown('[example csv file ](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)')

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative= True)
    st.header('**input data frame**')
    st.write(df)
    st.write('---')
    st.header('pandas profile report')
    st_profile_report(pr)


else:
    st.info('No data frame')

x_axis = st.sidebar.selectbox("Select x-axis feature", df.columns[:-1])
y_axis = st.sidebar.selectbox("Select y-axis feature", df.columns[:-1])