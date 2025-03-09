import streamlit as st
import mimetypes
from google import genai
import config

API_KEY = config.api

client = genai.Client(api_key=API_KEY)

st.write("Hello World \n\nThis is page 1 of many")

prompt = st.text_input("Enter a prompt for Gemini 2.0")
fileUpload = st.file_uploader("Please input a file")

if st.checkbox("I want to only look at my prompt response"):
    response1 = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    st.write(f"Below is Google Gemini 2.0 flash's response to '{prompt}'")
    st.write(response1.text)
    st.write("End Gemini")

if fileUpload is not None:
    mime_type, _ = mimetypes.guess_type(fileUpload.name)
    if mime_type is None:
        mime_type = "application/octet-stream"

    file = client.files.upload(file=fileUpload, mime_type=mime_type)

    if st.checkbox("I want to see the response to my prompt and file"):
        response2 = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[{"text": prompt}, {"file": file.name}]
        )
        st.write(f"Below is Google Gemini 2.0 flash's response to your prompt '{prompt}' and file upload")
        st.write(response2.text)
        st.write("End Gemini")
else:
    st.write("Please upload a file to proceed with a file response.")

