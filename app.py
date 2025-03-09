import streamlit as st
import pandas as pd
import time
#import cv2
import numpy as np
from PIL import Image
import requests

# Define the pages
page_1 = st.Page("pages/page1.py", title="Page 1", icon="❄️")
page_2 = st.Page("pages/page2.py", title="Page 2", icon="🎉")
page_3 = st.Page("pages/page3.py", title="Page 3", icon="🎉")
page_4 = st.Page("pages/readPDF.py", title="PDF", icon="🎉")
page_5 = st.Page("pages/download.py", title="Download", icon="🎉")
page_8 = st.Page("pages/page8.py", title="page8", icon="🎉")


# Set up navigation
pg = st.navigation([page_1, page_2, page_3, page_4, page_5, page_8])

# Run the selected page
pg.run()


