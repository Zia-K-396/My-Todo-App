import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todos_in_file=functions.get_todos()

    todo = st.session_state['new_todo']+"\n"
    if todo not in todos_in_file:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        st.info("Already in the list!", icon="🚨")




st.title("My ToDo App")



for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="ToDo App",label_visibility="hidden", placeholder="Type in a ToDo", on_change=add_todo, key='new_todo')
print("Heloo")