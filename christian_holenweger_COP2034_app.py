import streamlit as st
from PIL import Image, ImageFilter
import io

import streamlit as st

# Set up the app title and description
st.title("Filters on filters")
st.sidebar.write("Web App created using Python Streamlit library. This app supports ('jpg','png',jpeg') files!.")

# Set up the center column with Name, Project, and Due Date
st.header("Name: Christian Holenweger")
st.header("Project: Filter Changer")
st.header("Due Date: May 3, 2023")

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
