import streamlit as st
from PIL import Image, ImageFilter
import io

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

# Set up the app title and description
st.title("Image Filter App")
st.sidebar.write("Choose a filter option and adjust intensity if needed:")

# Define the available filter options as a dictionary with display names and filter functions
FILTER_OPTIONS = {
    "Grayscale": lambda img: img.convert("L"),
    "Blur": lambda img, intensity: img.filter(ImageFilter.GaussianBlur(radius=intensity)),
    "Sharpen": lambda img, intensity: img.filter(ImageFilter.UnsharpMask(radius=intensity, percent=150, threshold=3)),
}

# Add the filter options as radio buttons in the sidebar
filter_name = st.sidebar.radio("Filter Option", list(FILTER_OPTIONS.keys()))

# If the selected filter option requires an intensity value, add a slider to adjust it
if filter_name in ["Blur", "Sharpen"]:
    intensity = st.sidebar.slider("Intensity", min_value=0, max_value=10, value=5)
else:
    intensity = None

# Add a file uploader for images
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if a file was uploaded and display it if so
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    filtered_img = FILTER_OPTIONS[filter_name](img, intensity) if intensity is not None else FILTER_OPTIONS[filter_name](img)
    st.image(filtered_img, caption="Filtered Image", use_column_width=True)

    # Add a download button for the filtered image
    buffered = io.BytesIO()
    filtered_img.save(buffered, format="JPEG")
    st.download_button(
        label="Download Filtered Image",
        data=buffered.getvalue(),
        file_name="filtered_image.jpg",
        mime="image/jpeg"
    )
else:
    st.write("Please upload an image.")
