import streamlit as st
from datetime import datetime

st.title("Age Calculator")

dob = st.date_input("Enter your date of birth:")

if st.button("Calculate Age"):
    today = datetime.today().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Your age is: {age} years")
