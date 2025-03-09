import streamlit as st
import mimetypes
from google import genai
import config

API_KEY = config.api
client = genai.Client(api_key=API_KEY)

st.title("Gemini 2.0 Flash Analysis")
with open("prompts/message.txt", 'r') as file:
    prompt = file.read()

uploaded_file = st.file_uploader("Upload a file for analysis")

if st.button("Analyze"):
    contents = []
    
    # Add text prompt
    if prompt:
        contents.append({"text": prompt})
    
    # Handle file upload
    if uploaded_file is not None:
        # Guess MIME type
        mime_type, _ = mimetypes.guess_type(uploaded_file.name)
        if mime_type is None:
            mime_type = "application/octet-stream"  # Default if unknown

        # Upload file to Google GenAI
        file_data = uploaded_file.read()  # Read file as bytes
        file = client.files.upload(file=uploaded_file, config=dict(mime_type='application/pdf'))

        # Add file reference correctly
        contents.append(file)

    # Ensure there's something to send
    if contents:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents
        )
        st.write("Analysis Result:")
        st.write(response.text)
    else:
        st.warning("Please provide a prompt or upload a file for analysis.")
