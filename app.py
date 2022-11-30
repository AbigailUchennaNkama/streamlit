import streamlit as st
import tensorflow as tf
import matplotlib as plt
import pandas as pd
from PIL import Image, ImageOps
header = st.container()
button = st.container()


CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://momentousinstitute.org/assets/site/blog/clouds.jpg);
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

with header:
    st.title('Welcome to our awesome rain cloud website')


st.set_option('deprecation.showfileUploaderEncoding', False)

Image_uploaded = st.file_uploader("Upload an image file", type="jpeg")

if Image_uploaded is not None:
    data = Image.open(Image_uploaded)
    st.write(data)
