import streamlit as st
import pickle
from pickle import load
import pandas as pd
import numpy as np

filename='saved_steps_tension.pkl'
data=load(open(filename,'rb'))

xgb_model_tension = data["model_tension"]

def show_predict_page_tension():
    st.title("Prediction of the Residual Tensile Strength of RAC")

    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Water = st.number_input("Water (kg/$m^3$)")
        st.write("Min: 172, Max: 237")
        Cement = st.number_input("Cement (kg/$m^3$)")
        st.write("Min: 268, Max: 581")
        Sand = st.number_input("Sand (kg/$m^3$)")
        st.write("Min: 570, Max: 829")
        NA = st.number_input("NA (kg/$m^3$)")
        st.write("Min: 0, Max: 1200")

    with col2:
        RCA = st.number_input("RCA (kg/$m^3$)")
        st.write("Min: 0, Max: 1108")
        RCA_Size= st.number_input("RCA Maximum Size (mm)")
        st.write("Min: 0, Max: 20")
        NA_Size= st.number_input("NA Maximum Size (mm)")
        st.write("Min: 0, Max: 20")
        RCA_Density= st.number_input("RCA Density(kg/$m^3$)")
        st.write("Min: 0, Max: 2610")

    with col3:
        NA_Density= st.number_input("NA Density(kg/$m^3$)")
        st.write("Min: 0, Max: 2780")
        RCA_Water_absorption= st.number_input("RCA Water Absorption (%)")
        st.write("Min: 0, Max: 5.3")
        NA_Water_absorption= st.number_input("NA Water Absorption (%)")
        st.write("Min: 0, Max: 1.8")
        Temperature = st.number_input("Temperature (°C)")
        st.write("Min: 22, Max: 800")

    with col4:
        Rate = st.number_input("Heating Rate (°C/min)")
        st.write("Min: 0, Max: 10")
        Exposure_time = st.number_input("Exposure Period (hour)")
        st.write("Min: 0, Max: 4")
        Age = st.number_input("Heat Exposure Age (days)")
        st.write("Min: 0, Max: 90")

    ok = st.button("Calculate the Residual Tensile Strength of RAC")
    if ok:
        
        X = np.array([[Water, Cement, Sand, NA, RCA, RCA_Size, NA_Size, RCA_Density, NA_Density,
                         RCA_Water_absorption, NA_Water_absorption, Temperature,Rate, Exposure_time,Age]])
        
        
        X = X.astype(float)
        if np.sum(X[:, :-1]) == 0:
            Tension = np.array([0])
        elif Temperature <= 25:
            Tension = np.array([1])  # Set tension to 1 if Temperature is 20 to 25
        elif Rate ==0:
            Tension = np.array([1])  # Set Tension to 1 if rate is 0  
        else:
            Tension = xgb_model_tension.predict(X)
            
        st.subheader(f"The Residual Tensile Strength of RAC after Heat Exposure is  {Tension[0]:.2f} ")

#show_predict_page_tension()