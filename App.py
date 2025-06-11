import streamlit as st
import functions

user = st.text_input("Please enter your username to access your todo list")

if not user:
    st.stop()


todos = functions.get_todos(user)

def add_todo():
    todos_in_file=functions.get_todos(user)

    todo = st.session_state['new_todo']+"\n"
    if todo not in todos_in_file:
        todos.append(todo)
        functions.write_todos(todos,user)
    else:
        st.info("Already in the list!", icon="🚨")




st.title("My ToDo App")



for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos,user)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="ToDo App",label_visibility="hidden", placeholder="Type in a ToDo", on_change=add_todo, key='new_todo')