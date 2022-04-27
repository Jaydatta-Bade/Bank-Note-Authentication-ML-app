# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 23:28:54 2022

@author: Jaydatta 
"""

"""
@author: Jaydatta 
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:#00BFFF;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    
    <h6>If output is [0] then Bank Note is not Authenticate and
    if output is [1] then it is authenticate.</h6>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","")
    skewness = st.text_input("skewness","")
    curtosis = st.text_input("curtosis","")
    entropy = st.text_input("entropy","")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")
        st.text("By Jaydatta")

if __name__=='__main__':
    main()
    
    
    