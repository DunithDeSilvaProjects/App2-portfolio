import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dunith De Silva")
    content = """When it comes to high stress projects where logical thinking, hard work and pure 
    dedication to team work are key factors in operational success, that's where I thrive. 
    I would consider myself to be a highly imaginative, motivated and hard-working individual who 
    finds passion in being a part of a team and working towards bringing forth new ideas
    """
    st.info(content)


content2 = """ Below you can find some of the apps i have built
"""

st.write(content2)

col3 , col4 = st.columns(2)

df = pd.read_csv("data.csv",sep=";")


with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:20].iterrows():
        st.header(row["title"])

