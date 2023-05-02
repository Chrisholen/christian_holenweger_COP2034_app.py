import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image

# Set up the UI
st.title("Image Filter App")
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image")

if uploaded_file is not None:
    # Check if the uploaded file is an image
    file_ext = uploaded_file.name.split(".")[-1]
    if file_ext.lower() not in ["png", "jpg", "jpeg"]:
        st.error("Please upload a valid image file.")
    else:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image")
    
    # Define the filter options
filters = {
    "None": lambda x: x,
    "Grayscale": lambda x: cv2.cvtColor(np.array(x), cv2.COLOR_RGB2GRAY),
    "Canny Edge Detection": lambda x: cv2.Canny(np.array(x), 100, 200),
    "Gaussian Blur": lambda x: cv2.GaussianBlur(np.array(x), (5, 5), 0),
    "Invert Colors": lambda x: cv2.bitwise_not(np.array(x)),
}

# Display the radio buttons for filter selection
selected_filter = st.radio("Select a filter", list(filters.keys()))

# Apply the selected filter to the image
if selected_filter != "None":
    filtered_image = filters[selected_filter](image)
else:
    filtered_image = image

# Display the filtered image
st.image(filtered_image, caption="Filtered Image")
    
 # Display the original and filtered images side by side
st.image([image, filtered_image], caption=["Original Image", "Filtered Image"])
   
if selected_filter == "Gaussian Blur":
    # Add a slider to adjust the blur radius
    blur_radius = st.slider("Blur Radius", 1, 20, 5)
    filtered_image = cv2.GaussianBlur(np.array(image

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
