import streamlit as st
import functions

todos = functions.get_todos()

st.title("Checklist App")
st.subheader("This is my first python web app")
st.write("Just plowing right through all these videos here")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add something:", placeholder=("Add something here..."))