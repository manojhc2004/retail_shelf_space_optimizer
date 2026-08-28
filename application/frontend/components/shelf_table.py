import streamlit as st
import pandas as pd


def show_table(data):

    df = pd.DataFrame(data)

    st.subheader("📦 Shelf Layout")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )