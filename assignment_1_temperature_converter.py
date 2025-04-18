import streamlit as st

st.title("Temperature Converter")

celsius = st.number_input("Enter temperature in Celsius:")

if st.button("Convert"):
    fahrenheit = (celsius * 9/5) + 32
    st.write(f"{celsius}°C = {fahrenheit}°F")
