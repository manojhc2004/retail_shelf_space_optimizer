import streamlit as st


def sidebar():

    st.sidebar.header("⚙️ Optimization Settings")

    uploaded_file = st.sidebar.file_uploader(
        "Upload Retail Dataset",
        type=["csv"]
    )

    min_support = st.sidebar.number_input(
        "Min Support",
        min_value=0.001,
        max_value=0.1,
        value=0.005,
        step=0.001,
        format="%.3f"
    )

    threshold = st.sidebar.number_input(
        "Confidence",
        min_value=0.01,
        max_value=1.0,
        value=0.11,
        step=0.01
    )

    greater_than = st.sidebar.number_input(
        "Lift",
        min_value=1,
        value=1,
        step=1
    )

    shelf_capacity = st.sidebar.number_input(
        "Shelf Capacity",
        min_value=1,
        value=4
    )

    run = st.sidebar.button(
        "Run Optimization",
        use_container_width=True
    )

    return (
        uploaded_file,
        min_support,
        threshold,
        greater_than,
        shelf_capacity,
        run
    )