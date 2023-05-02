import streamlit as st
from PIL import Image
import numpy as np

# App Name and Description
st.sidebar.title("My Streamlit App")
st.sidebar.write("This is a simple app created using Streamlit!")

# Full Name, Project, and Due Date
st.title("Welcome to my Streamlit app!")
st.write("Created by: Your Name")
st.write("Project: Your Project Name")
st.write("Due Date: MM/DD/YYYY")

# FAU owl logo
image = Image.open('fau-owl.png')
st.sidebar.image(image, caption='', use_column_width=True)

# File uploader to upload an image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)


# Set page title and icon
st.set_page_config(page_title="Image Filters", page_icon=":camera:")

# Page title and description
st.title('Filters on Filters')
st.write('This is an app that lets the user change how an uploaded image looks by using filters to change the appearance.')
st.write('Web App created using Python Streamlit library. This app supports (.jpg, .png, .jpeg)')

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
