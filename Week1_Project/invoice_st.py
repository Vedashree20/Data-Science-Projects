import streamlit as st
from PIL import Image
import pandas as pd
import requests
from pdf2image import convert_from_path
import pytesseract as tess
import re
#image=Image.open('C:\\Users\\Admin\\OneDrive\\Desktop\\virtualenv\\FAST-API\\logo.png')
#st.image(image,width=390)
#st.sidebar.header('Input Options')
st.title('Invoice total amount generator app')
st.markdown(""" This app generates the total amount from the invoice""")
path_input = st.text_input('Input your path here:') 
@st.cache
def result():
    tess.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    images = convert_from_path(path_input,500,poppler_path=r'C:\Users\Admin\OneDrive\Desktop\poppler-21.10.0\Library\bin')
    images[0].save('invoice_.png','JPEG')
    image = Image.open('invoice_.png')
    image_to_text =tess.image_to_string(image, lang='eng')
    print(image_to_text)
    res=image_to_text.split()
    fl=[]
    regex = '[+-]?[0-9]+\.[0-9]+'
    for s in res:
      if(re.search(regex, s)): 
         fl.append(s)
    return(max(fl))
df = result()

st.header('Total amount')

st.write(df)

#st.write( df.transpose() )


#---------------------------------#
# About

