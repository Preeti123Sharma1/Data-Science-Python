'''

to run, do not  click the play button, but instread, in the terminal, type:
=>  cd app_one
=> python -m streamlit run app.py
'''

from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Image App",
    page_icon="🏞",
    layout="wide"
)

st.title("Image Processing App")
st.sidebar.header("select image file")
image_file = st.sidebar.file_uploader("Upload Image", type=['png','jpg','jpeg'])
if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption=image_file.name)