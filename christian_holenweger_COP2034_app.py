import streamlit as st
from PIL import Image
import numpy as np

# Set page title and icon
st.set_page_config(page_title="Image Filters", page_icon=":camera:")

# Page title and description
st.title('Filters on Filters')
st.write('This is an app that lets the user change how an uploaded image looks by using filters to change the appearance.')
st.write('Web App created using Python Streamlit library. This app supports (.jpg, .png, .jpeg)')

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
