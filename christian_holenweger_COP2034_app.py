import streamlit as st
from PIL import Image, ImageFilter
import io
from PIL import Image

# App Name and Description
st.sidebar.title("Filters on filters")
st.sidebar.write("This is a app that lets the user change how an uploaded image looks by using filters to change the apperence.")
st.sidebar.write("Web App created using Python Streamlit library. This app supports ('jpg','png',jpeg') files!")

# Full Name, Project, and Due Date
st.title("Filters on filters")
st.write("Created by: Chrisitan Holenweger")
st.write("Project: Filters on Filters")
st.write("Due Date: 05/03/2023")

# FAU owl logo
image = Image.open('fau_owl.png')
st.sidebar.image(image, caption='', use_column_width=True)

# File uploader to upload an image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
