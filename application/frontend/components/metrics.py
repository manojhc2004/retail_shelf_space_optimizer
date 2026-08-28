import streamlit as st


def show_metrics(total_shelves):

    st.subheader("📊 Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Shelves",
            total_shelves
        )

    with col2:
        st.metric(
            "Pipeline Status",
            "Completed"
        )