import streamlit as st
from PIL import Image
import numpy as np

# App Name and Description
st.sidebar.title('Filters change pictures')
st.sidebar.write('This is an app that lets the user change how an uploaded image looks by using filters to change the appearance.')
st.sidebar.write('Web App created using Python Streamlit library. This app supports (.jpg, .png, .jpeg)')


# Full Name, Project, and Due Date
st.title("Christian_Holenweger_COP2034_app.py")
st.write("Final Project COP2034")
st.write("Due Date: 05/03/2023")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
