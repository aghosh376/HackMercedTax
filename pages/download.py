import streamlit as st
import pandas as pd
from io import StringIO
from google import genai
from google.genai import types
import config

API_KEY = config.api

client = genai.Client(api_key= API_KEY)


st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

with open("TaxForms/2024_Form_1040.pdf", "rb") as file:
    st.download_button(
        label = "Download Form 1040",
        data = file,
        file_name = "2024_Form_1040.pdf",
        mime = "application/pdf",
        type= "primary"
    )
    
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
st.write("Section for uploading files and downloading files")

prompt = st.text_input("Enter a prompt for Gemini 2.0")
@st.cache_data
def getPDF():
    return st.file_uploader("Please input a file")
fileUpload = getPDF()

if fileUpload is not None:
    file = client.files.upload(file=fileUpload, config=dict(mime_type='application/pdf'))

    if st.checkbox("I want to only look at my prompt response"):
        response1 = client.models.generate_content(model="gemini-2.0-flash", contents= prompt)
        st.write(f"Below is google gemini 2.0 flash's response to '{prompt}'")
        st.write(response1.text)
        st.write("End gemini")

    if st.checkbox("I want to see the response to my prompt and file"):
        response2 = client.models.generate_content(model="gemini-2.0-flash", contents=[prompt, file])
        st.write(f"Below is google gemini 2.0 flash's response to your prompt '{prompt}' and file upload")
        st.write(response2.text)
        st.write("End gemini")
        
        
else:
    st.write("Please upload a file to proceed.")

