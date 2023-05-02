import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Christian Holenweger')
st.title('Final Project COP2034')
st.title('May 03, 2023')

st.sidebar.title("Filters on Filters")
st.sidebar.write("This is a app that lets the user change how an uploaded image looks by using filters to change the apperence.!")
st.sidebar.write("Web App created using Python Streamlit library. this app supports ('jpg','png','jpeg')")

# Set page title
st.set_page_config(page_title="Image Uploader")

# Set page header
st.title("Image Uploader")

# Create an upload button
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image")

