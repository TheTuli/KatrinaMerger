import streamlit as st
from utilities import *

st.title("Katrina's nice CSV Merger")


def file_upload():
    uploaded_files = st.sidebar.file_uploader(label="Choose Files to Merge",
                                              accept_multiple_files=True)
    if uploaded_files is not None:
        return uploaded_files


files = file_upload()

if files:
    if st.button("Start Merge(Based on 15 pre-select columns)"):
        df = read_and_drop(files)

        st.write(df)
        st.write("DataFrame Size:", df.shape)

        st.markdown(get_table_download_link(df), unsafe_allow_html=True)
