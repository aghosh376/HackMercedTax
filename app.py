import streamlit as st
import pandas as pd
import numpy as np
import time


st.header("Hello World", divider='blue')

st.header("This is a header with a divider", divider='rainbow')
st.subheader("This is a subheader")

st.markdown("This is a markdown text")

col1, col2 = st.columns(2)

with col1:
    x_slider =st.slider("Select a value", 1, 10)
    st.write("This is col 1")
with col2:
    st.write("The value of :blue[***x***] is ", x_slider)
    st.write("This is col 2")

st.write("Here's our first attempt at using data to create a table:")
st.write("Col 2 is col 1 x 10 x slider value")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10*x_slider, 20*x_slider, 30*x_slider, 40*x_slider]
}))

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
    
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# This should display the value under selectbox in the sidebar
st.sidebar.write("You want to be contacted through", add_selectbox)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
    
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10*x_slider, 20*x_slider, 30*x_slider, 40*x_slider]
    })

num_option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', num_option

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

