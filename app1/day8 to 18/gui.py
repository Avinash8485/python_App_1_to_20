import functions
import FreeSimpleGUI as sq
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt','w') as file:
        pass
sq.theme("DarkPurple4")

clock = sq.Text('',key='clock')
label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo",key='todo')
add_button =sq.Button("Add")
exit_button = sq.Button("exit")
list_box = sq.Listbox(values = functions.get_todos(),key='todos',enable_events=True,size=[45,10])
edit_button = sq.Button("edit")
complete_button = sq.Button("complete")

window = sq.Window('My To-Do App', 
                   layout=[[clock],[label],[input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]], 
                   font=('Helvetic',12))

while True:
    event , values =window.read(timeout=200)
    window['clock'].update(value = time.strftime("%b %d,%Y %H %M %S"))
    print(event)
    print(values)
    match event:
        case 'Add':

            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.set_todos(todos)
            window['todos'].update(values=todos)

        case 'edit':
            try:
                todo =values['todos'][0]
                new_todo = values['todo']+'\n'
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index]= new_todo
                functions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sq.popup("please select the item")

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'complete':
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo)
                functions.set_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sq.popup("please select the item")

        case 'exit':
            exit()

        case sq.WIN_CLOSED:
            break



window.close()