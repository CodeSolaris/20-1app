import streamlit as st
import functions

todo_list = functions.get_todo_list()

st.title("My To-Do App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    # if checkbox:
    #     todo_list.pop(index)
    #     functions.write_todo_list(todo_list)
    #     del st.session_state[todo]
    #     st.experimental_rerun()

st.button("Add To-Do")

st.text_input(
    "Add a new todo",
    placeholder="Add a new todo",
    key="new_todo",
    on_change=functions.add_todo,
)
