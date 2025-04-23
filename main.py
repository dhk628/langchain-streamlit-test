import streamlit as st
import langchain_helper

st.title('Baby Name Generator')

gender = st.pills(
    "Choose a gender",
    ["Girl", "Boy"],
    selection_mode='single'
)

nationality = st.text_input("Enter nationality", '')

button_input = st.button("Submit")

if button_input:
    if gender and nationality:
        baby_names = langchain_helper.generate_baby_names(gender.lower(), nationality)
        st.write('Top 5 baby names:')
        for name in baby_names:
            st.write("--", name)
    else:
        st.write("Error: Please enter a gender and nationality")
