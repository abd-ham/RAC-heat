import streamlit as st
from predict_page_compression import show_predict_page_compression
from predict_page_tension import show_predict_page_tension


page = st.sidebar.selectbox("Response", ("Resiual Compressive Strength", "Residual Tensile Strength"))

if page == "Resiual Compressive Strength":
    show_predict_page_compression()
else:
    show_predict_page_tension()