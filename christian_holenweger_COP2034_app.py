import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import cv2
import sys
sys.path.append('\env\Lib\site-packages')

st.title('Christian Holenweger')
st.title('Final Project COP2034')
st.title('May 03, 2023')

st.sidebar.title("Filters on Filters")
st.sidebar.write("This is a app that lets the user change how an uploaded image looks by using filters to change the apperence.!")
st.sidebar.write("Web App created using Python Streamlit library. this app supports ('jpg','png','jpeg')")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    import cv2
import numpy as np
import streamlit as st


def grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def blur(img):
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    return blur


def canny(img):
    edges = cv2.Canny(img, 100, 200)
    return edges


def sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    sobel = np.sqrt(sobelx ** 2 + sobely ** 2).astype(np.uint8)
    return sobel


def cartoonize(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


# Main program
st.set_page_config(page_title="Image Filters", page_icon=":camera:")
st.title("Apply Image Filters")

# Load image
img_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if img_file is not None:
    img = cv2.imdecode(np.fromstring(img_file.read(), np.uint8), 1)
    st.image(img, caption="Original Image", use_column_width=True)

    # Display filter options
    filter_name = st.sidebar.radio("Choose a filter", ("Grayscale", "Blur", "Canny", "Sobel", "Cartoonize"))

    # Apply selected filter
    if filter_name == "Grayscale":
        filtered_img = grayscale(img)
    elif filter_name == "Blur":
        filtered_img = blur(img)
    elif filter_name == "Canny":
        filtered_img = canny(img)
    elif filter_name == "Sobel":
        filtered_img = sobel(img)
    elif filter_name == "Cartoonize":
        filtered_img = cartoonize(img)

    # Display filtered image
    st.image(filtered_img, caption=f"{filter_name} Filtered Image", use_column_width=True)
