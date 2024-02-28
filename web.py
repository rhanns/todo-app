import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["input_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Checklist App")
st.subheader("This is my first python web app")
st.write("Just plowing right through all these videos here")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add something:", placeholder="Add something here...",
              on_change=add_todo, key='input_todo')
