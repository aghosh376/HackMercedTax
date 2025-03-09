import streamlit as st
from google import genai
#from google.genai import types
import os
import config

API_KEY = config.api

client = genai.Client(api_key= API_KEY)

st.write("Hello World \n\nThis is page 1 of many")


prompt = st.text_input("Enter a prompt for Gemini 2.0")
fileUpload = st.file_uploader("Please input a file")

if st.checkbox("I want to only look at my prompt response"):
        response1 = client.models.generate_content(model="gemini-2.0-flash", contents= prompt)
        st.write(f"Below is google gemini 2.0 flash's response to '{prompt}'")
        st.write(response1.text)
        st.write("End gemini")

if fileUpload is not None:
    file = client.files.upload(file=fileUpload)

    if st.checkbox("I want to see the response to my prompt and file"):
        response2 = client.models.generate_content(model="gemini-2.0-flash", contents=[prompt, file])
        st.write(f"Below is google gemini 2.0 flash's response to your prompt '{prompt}' and file upload")
        st.write(response2.text)
        st.write("End gemini")
else:
    st.write("Please upload a file to proceed.")
