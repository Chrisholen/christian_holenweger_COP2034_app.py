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

# Page title and description
st.title('Filters on Filters')
st.write('This is an app that lets the user change how an uploaded image looks by using filters to change the appearance.')
st.write('Web App created using Python Streamlit library. This app supports (.jpg, .png, .jpeg)')

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
