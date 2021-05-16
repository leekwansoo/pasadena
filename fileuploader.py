import streamlit as st
from PIL import Image
from streamlit.caching import cache 
import pandas as pd
import docx2txt
from PyPDF2 import PdfFileReader
import pdfplumber


# Load Images
@st.cache 
def load_image(image_file):
    img = Image.open(image_file)
    return img

def main():
    st.title("File Uploader")

    menu = ["Home", "Dataset", "Documents", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images",
            type=["png","jpg","jpeg"])
        if image_file is not None:
            st.write(type(image_file))
            # st.write(dir(image_file))
            file_details = {"filename":image_file.name, 
            "file_type":image_file.type, "file_size":image_file.size}
            st.write(file_details)

            st.image(load_image(image_file))

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["CSV"])
        if data_file is not None:
                st.write(type(data_file))
                df = pd.read_csv(data_file)
                st.dataframe(df)

    elif choice == "Documents":
        st.subheader("Documents")
        docx_file = st.file_uploader("Upload Document",
            type=["pdf","docx", "txt"])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"filename":docx_file.name, 
                    "file_type":docx_file.type, "file_size":docx_file.size}
                st.write(file_details)
                if docx_file.type == "text/plain":
                    raw_text = str(docx_file.read(), "utf-8")
                    st.text(raw_text)

                elif docx_file.type =="applicatio/pdf":
                    try:
                        with pdfplumber.open(docx_file)as pdf:
                            pages = pdf.pages[0]
                            st.write(pages.extract_text())
                    except:
                        st.write("None")
                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
                    st.text(raw_text)
                    
                     
        else:
            st.subheader("About")
    
if __name__ == '__main__':
    main()
