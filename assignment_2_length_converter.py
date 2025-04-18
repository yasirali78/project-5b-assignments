import streamlit as st

st.title("Length Converter")

meters = st.number_input("Enter length in meters:")

if st.button("Convert"):
    km = meters / 1000
    st.write(f"{meters} meters = {km} kilometers")
