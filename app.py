import streamlit as st

st.write("Hello World")

st.header("This is a header with a divider", divider='rainbow')
st.subheader("This is a subheader")

st.markdown("This is a markdown text")

x =st.slider("Select a value", 1, 10)
st.write("The value of ***x*** is ", x)