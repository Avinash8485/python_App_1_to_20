import streamlit as s 
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = s.session_state["new_todo"]+'\n'
    todos.append(new_todo)
    functions.set_todos(todos)


s.title("My Todo App")
s.subheader("This is my todo App")
s.write("This App is to increase productivity")



for index,item in enumerate(todos):
    checkbox =s.checkbox(item , key=item)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del s.session_state[item]
        s.rerun()


s.text_input(label=" ",placeholder="Add new todo",
             on_change=add_todo,key='new_todo')


s.session_state