import streamlit as st
import pandas as pd
import time
#import cv2
import numpy as np
from PIL import Image
import requests

# Define the pages
main_page = st.Page("pages/main_page.py", title="Main Page", icon="🎈")
page_1 = st.Page("pages/page1.py", title="Page 1", icon="❄️")
page_2 = st.Page("pages/download.py", title="Page 2", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_1, page_2])

# Run the selected page
pg.run()
