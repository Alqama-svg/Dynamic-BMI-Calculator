# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:59:49 2024

@author: Alqama
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height(cm):", 100, 250, 175)
weight = st.slider("Enter your weight(kg):", 20, 200, 70)

bmi = weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI between 30 or greater")
