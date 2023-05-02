import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import cv2

st.title('Christian Holenweger')
st.title('Final Project COP2034')
st.title('May 03, 2023')

st.sidebar.title("Filters on Filters")
st.sidebar.write("This is a app that lets the user change how an uploaded image looks by using filters to change the apperence.!")
st.sidebar.write("Web App created using Python Streamlit library. this app supports ('jpg','png','jpeg')")


# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    st.image(image, caption='Original Image')

    # Filter selection
    filter_type = st.selectbox("Select a filter:", ('Grayscale', 'Canny Edge Detection', 'Blur'))

    # Apply filter
    if filter_type == 'Grayscale':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        st.image(gray, caption='Grayscale Image')
    elif filter_type == 'Canny Edge Detection':
        edges = cv2.Canny(image, 100, 200)
        st.image(edges, caption='Canny Edge Detection')
    elif filter_type == 'Blur':
        blurred = cv2.GaussianBlur(image, (11, 11), 0)
        st.image(blurred, caption='Blurred Image')
