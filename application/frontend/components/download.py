import streamlit as st
import pandas as pd


def download_csv(data):

    df = pd.DataFrame(data)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Shelf Layout",
        data=csv,
        file_name="Shelf_Layout.csv",
        mime="text/csv"
    )