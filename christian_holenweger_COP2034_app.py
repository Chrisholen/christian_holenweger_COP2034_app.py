import streamlit as st
from PIL import Image, ImageFilter
import io

import streamlit as st

# Set up the app title and description
st.title("My Streamlit App")
st.sidebar.write("Welcome to my app! This is a demo of how to create a simple layout with Streamlit.")

# Set up the center column with Name, Project, and Due Date
st.header("Name: John Smith")
st.header("Project: Image Classifier")
st.header("Due Date: May 31, 2023")

# Set up the right column with the FAU owl logo
image = "https://www.fau.edu/president/assets/images/owl.svg"
st.sidebar.image(image, use_column_width=True)

# Set up the file uploader for images
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if a file was uploaded and display it if so
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
else:
    st.write("Please upload an image.")
