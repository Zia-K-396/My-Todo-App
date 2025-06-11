import streamlit as st
import functions

if "user" not in st.session_state:
    user = st.text_input("""ENTER YOUR USERNAME TO ACCESS YOUR TODO LIST\n
    (The username entered first time will be used throughout.\n
     Please try to include alphabets and numbers in your username)""")
    if st.button("Continue") and user:
        st.session_state.user = user
        st.rerun()
    else:
        st.stop()

else:
    user = st.session_state.user
    todos = functions.get_todos(user)

    def add_todo():
        todos_in_file=functions.get_todos(user)

        todo = st.session_state['new_todo']+"\n"
        if todo not in todos_in_file:
            todos.append(todo)
            functions.write_todos(todos,user)
        else:
            st.info("Already in the list!", icon="🚨")
        st.session_state["new_todo"] = ""




    st.title("My ToDo App")



    for index,todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos,user)
            del st.session_state[todo]
            st.rerun()

    st.text_input(label="ToDo App",label_visibility="hidden", placeholder="Type in a ToDo", on_change=add_todo, key='new_todo')