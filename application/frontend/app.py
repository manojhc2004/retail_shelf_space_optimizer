import streamlit as st

from api import run_pipeline

from components.header import show_header
from components.sidebar import sidebar
from components.metrics import show_metrics
from components.shelf_table import show_table
from components.network_graph import show_network
from components.download import download_csv


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Retail Shelf Space Optimizer",
    page_icon="📦",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
show_header()

# -----------------------------
# Sidebar
# -----------------------------
uploaded_file, min_support, threshold, greater_than, shelf_capacity, run = sidebar()

# -----------------------------
# Run Pipeline
# -----------------------------
if run:

    # Check if file is uploaded
    if uploaded_file is None:
        st.warning("⚠ Please upload a CSV file.")

    else:

        try:

            with st.spinner("Running Retail Shelf Optimization..."):

                # Call FastAPI
                result = run_pipeline(
                    uploaded_file,
                    min_support,
                    greater_than,
                    threshold,
                    shelf_capacity
                )

            # Success Message
            st.success(result["message"])

            # -----------------------------
            # Summary
            # -----------------------------
            show_metrics(
                result["summary"]["total_shelves"]
            )

            st.divider()

            # -----------------------------
            # Shelf Layout
            # -----------------------------
            show_table(
                result["summary"]["data"]
            )

            st.divider()

            # -----------------------------
            # Product Network
            # -----------------------------
            st.subheader("🌐 Product Association Network")

            show_network(
                result["summary"]["html_path"]
            )

            st.divider()

            # -----------------------------
            # Download CSV
            # -----------------------------
            download_csv(
                result["summary"]["data"]
            )

        except Exception as e:

            st.error(f"❌ {e}")