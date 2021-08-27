import streamlit as st
from PIL import Image


st.title("This is My BMI calculator")

img = Image.open("bmi.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")

st.text("""

If your BMI is less than 18.5 , it falls within the underweight range.
If your BMI is 18.5 to <25 , it falls within the healthy weight range.
If your BMI is 25.0 to <30 , it falls within the overweight range.
If your BMI is 30.0 or higher , it falls within the obesity range.


""")
#input

weight = st.number_input("Enter your weight in Kg", step = 0.1)

height = st.number_input("Enter your Height in Meters")




bmi = weight/(height)**2

st.success(f"Your BMI is {bmi}")