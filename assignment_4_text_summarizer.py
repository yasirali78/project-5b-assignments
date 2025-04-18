import streamlit as st

st.title("Text Summarizer")

text = st.text_area("Paste your paragraph here:")

if st.button("Summarize"):
    words = text.split()
    if len(words) > 20:
        summary = ' '.join(words[:20]) + "..."
    else:
        summary = text
    st.write("Summary:")
    st.write(summary)v
