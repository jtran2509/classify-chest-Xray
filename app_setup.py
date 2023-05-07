import os
import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('export.pkl', 'rb')

st.title("Pneumonia Chest Xray detection")


# Heading
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> Pneumonia ML App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)



def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


if __name__ == '__main__':
    # Select a file
    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path', '.')
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)

