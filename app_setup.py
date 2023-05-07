import os
import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('export.pkl', 'rb')

st.title("Pneumonia Chest Xray detection")
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> Pneumonia ML App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

safe_html ="""  
<div style="background-color:#80ff80; padding:10px >
<h2 style="color:white;text-align:center;"> The Abalone is young</h2>
</div>
"""
if st.button("Predict the type"):
output = predict_age(Length,Diameter,Height,Whole_weight, Shucked_weight,Viscera_weight,Shell_weight)
st.success('The age is {}'.format(output))

        if output == 1:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 2:
            st.markdown(warn_html,unsafe_allow_html=True)
        elif output == 3:
            st.markdown(danger_html,unsafe_allow_html=True)


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

