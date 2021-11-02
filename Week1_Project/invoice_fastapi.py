from typing import ItemsView, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import streamlit as st
from PIL import Image
import requests
from pdf2image import convert_from_path
import pytesseract as tess
import re
app = FastAPI()
class Item(BaseModel):
      url:str
@app.post("/invoicegenerator/")
def generate_item(item: Item):
    tess.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    images = convert_from_path(item.url,500,poppler_path=r'C:\Users\Admin\OneDrive\Desktop\poppler-21.10.0\Library\bin')
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
    return max(fl)
    