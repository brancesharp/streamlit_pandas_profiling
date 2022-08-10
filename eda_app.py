import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title("EDA with Pandas-Profiling")

tab1, tab2 = st.tabs(("Load Data", "EDA"))

with tab1:
    st.header("Load CSV Data")
    csv_file = st.file_uploader("Choose File", type=["csv"])
    if csv_file is not None:
        @st.cache
        def load_data():
            data = pd.read_csv(csv_file)
            return data
        df = load_data()
        report = ProfileReport(df, explorative=True)
        st.write(df)

with tab2:
    if csv_file is not None:
        st.header("Exploratory Data Analysis")
        st_profile_report(report)
    else:
        st.header("Input CSV Data")

