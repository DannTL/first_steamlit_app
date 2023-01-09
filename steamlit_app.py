
import streamlit as st
import pandas as pd
import requests

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')


st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = st.multiselect("Pick some fruits:" , list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)
