
import streamlit as st
import pandas as pd

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')


st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.multiselect("Pick some fruits:" , list(fruit_list.index),['Avocado','Strawberries'])

st.dataframe(fruit_list)

