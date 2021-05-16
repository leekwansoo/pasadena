import streamlit as st

#def load_image(image_file):
#   img = Image.open(image_file)
#   return img

def main():
    st.title("File Uploader")

    menu = ["Home", "Dataset", "Documents", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
     
    elif choice == "Dataset":
        st.subheader("Dataset")
            
    elif choice == "Documents":
        st.subheader("Documents")
            
    else:
        st.subheader("About")  
                       
if __name__ == '__main__':
    main()