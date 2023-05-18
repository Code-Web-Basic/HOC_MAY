

import streamlit as st
from PIL import Image
image = Image.open('uteicon.jpg')
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

mid, col2 = st.columns([1,5 ])
with mid: st.image(image, width=100)
with col2:
    st.write('###  HCMC University of Technology and Education')


st.write("# Welcome to Machine Learning project! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Build a Machine Learning web application in Python with Streamlit. 
    
    ### Contents in the project:
    - Handwriting recognition
    - Face recognition
    - California house price prediction
    - Emotion recognition
    - Recommend movies
    - Fruit recognition
    ### How to run this application
    - Open project in VSCode
    - Open Terminal in VSCode
    - Run "streamlit run D:\HocMay\MachineLearning\👋_Hello.py [ARGUMENTS]" (Please change your path)
    - If there is an error please import the library and run it again
    ### Student
    - Nguyễn Đình Hiếu - 20110472
    - Nguyễn Văn Tú - 20110563
    
    ### Teacher
    - Trần Tiến Đức
    ### Source code
    - code: https://github.com/CunoVox/MachineLearning.git
    ### Reference
    - Teacher Tran Tien Duc
    - https://www.youtube.com/watch?v=1xtrIEwY_zY
    - https://www.datacamp.com/tutorial/streamlit
"""
)
