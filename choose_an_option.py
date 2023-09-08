import streamlit as st
import os

def delete_and_download():
    files = os.listdir(r'C:\py')

    for file in files:
        st.write(file)
        if st.button(f'delete {file}'):
            os.remove(fr'C:\py\{file}')
        with open(fr'C:\py\{file}') as foo:
            st.download_button(f'Download {file}', foo, file)
def uploading():
    uploaded_files = st.file_uploader("Choose a TXT file", accept_multiple_files=True)
    encoding = 'utf8'

    for uploaded_file in uploaded_files:

        if uploaded_file.name.endswith('txt'):
            ttt = open(fr'C:\py\{uploaded_file.name}', 'w')
            ttt.write((uploaded_file.read()).decode(encoding))
            ttt.close()

        else:
            st.write('our programm need another type of file!!!!!')
page_names_to_funcs = {
    "working with our files": delete_and_download,
    "uploading some your files": uploading
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
