import streamlit as st
import pandas as pd
import numpy as np
import cv2

import streamlit as st
from PIL import Image

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

# Function to apply grayscale filter
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Radio buttons to select filter
filter_choice = st.radio("Select a filter", ("Grayscale",))

# Apply selected filter
if filter_choice == "Grayscale":
    grayscale_image = grayscale(np.array(image))
    st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)
# Function to apply brightness filter
def brightness(img, brightness_level):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - brightness_level
    v[v > lim] = 255
    v[v <= lim] += brightness_level
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

# Radio buttons to select filter
filter_choice = st.radio("Select a filter", ("Grayscale", "Brightness"))

# Apply selected filter
if filter_choice == "Grayscale":
    grayscale_image = grayscale(np.array(image))
    st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)
elif filter_choice == "Brightness":
    brightness_level = st.slider
