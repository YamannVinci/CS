import streamlit as st
import pickle
import pandas as pd
from PIL import Image
im = Image.open("Flowchart-1.png")
st.image(im, width = 700, caption = "Methodology")


html_temp = """
<div style="background-color:blue;padding:1.5px">
<h1 style='color:white;text-align:center;">Compressive Strength Predicition </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.sidebar.title('Enter the Following Parameters')
RH=st.sidebar("Rebound Number", 14, 55.50, step=10)
UPV=st.sidebar("Ultrasonic Pulse Velocity", 1.82, 5.22, step=10)

def csMPa():
my_dict = {"RH" : RH,
          "UPV" : UPV}
df_sample = pd.DataFrame.from_dict(my_dict)
return df_sample
dfc = csMPa()
model = pickle.load(open("model_xg", "rb"))

if st.sidebar.button("Submit"):
  result = (model.predict(dfc))
  st.success(f"Compressive Strength Prediction of the Concrete is (result) MPa")
         
  
