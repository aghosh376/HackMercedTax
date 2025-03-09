import streamlit as st
from pypdf import PdfReader
#import pdfminer
from pdfminer.high_level import extract_text as fallback_text_extraction
import os


#asks user to upload a pdf file
temp = False

if st.button("Delete all uploaded forms"):
    for key in st.session_state.keys():
        del st.session_state[key]

if st.button("Toggle uploading forms"):
    temp = not temp


st.title("PDF Reader")
uploaded_files = st.file_uploader("Upload a PDF file of a tax form down below", type=["pdf"], accept_multiple_files=True)

 
formName = []

if (temp == True):
    st.write("**Uploads have been stopped**")
        
else:
    st.write("**Uploads are going through**")
        
st.divider()

for uploaded_file in uploaded_files:
    if (temp == True):
        break
    else:
        pass

    text = "" 
    try:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as exc:
        text = fallback_text_extraction(uploaded_file)

    index = text.find("OMB No.")
    formName.append(text[index:index+17])

    if index == -1:
        st.write("Sorry, we can't tell what form this is. Please try again.")
    else:
        st.write(f"Form {formName[-1]} found at char {index}!")
    
    if formName[-1] not in st.session_state:
        st.write(f"Form {formName[-1]} has been uploaded!")
    else:
        st.write(f"Form {formName[-1]} has already been uploaded")
    
    st.session_state.key = formName[-1]
    st.session_state[formName[-1]] = uploaded_file

    st.divider()


st.write(st.session_state.keys())
st.write(formName)

st.divider()
st.divider()

