import pickle
import streamlit as st
from os import path
import numpy as np 


st.title("Milk Quality Prediction App")

file_name = "lr_model.pkl"
with open(path.join(file_name),'rb') as f:
    lr_modle = pickle.load(f)
ph = st.number_input("Insert a pH Value(3-9.5)")
tm = st.number_input("Insert Temprature of Milk (34-90)")
ta = st.number_input("Insert Taste of Milk (0/1)")
om = st.number_input("Insert Odor of Milk (0/1)")
fm = st.number_input("Insert Fat of Milk (0/1)")
tu = st.number_input("Insert Turbidity of Milk (0/1)")
cm = st.number_input("Insert Colour of Milk (240-255))")
if st.button("Predict"):
    pred = lr_modle.predict(np.array([[ph,tm,ta,om,fm,tu,cm]]))
    st.write("Quality of Milk is :",pred[0])
