import streamlit as st
from google import genai
#from google.genai import types
import config

API_KEY = config.api

client = genai.Client(api_key= API_KEY)

response = client.models.generate_content(model="gemini-2.0-flash", contents="Write hello world in python")

st.write("Hello World \n\nThis is page 1 of many")
st.write("Below is google gemini 2.0 flash's response to 'Write hello world in python'")
st.write(response.text)
st.write("End gemini")