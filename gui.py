import PySimpleGUI as sg

import functions

todo_list = functions.get_todo_list()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todo_list, key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box, edit_button],
        [complete_button, exit_button],
    ],
    font=("Helvetica", 18),
)


while True:
    event, values = window.read()

    match event:
        case "Add":
            todo = values["todo"]
            functions.add_todo(todo)
            todo_list = functions.get_todo_list()
            functions.window_update(todo_list, window)

        case "Exit":
            break

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo
            functions.write_todo_list(todo_list)
            functions.window_update(todo_list, window)

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Complete":
            todo_to_complete = values["todos"][0]
            todo_list.remove(todo_to_complete)
            functions.write_todo_list(todo_list)
            functions.window_update(todo_list, window)

        case sg.WIN_CLOSED:
            break

window.close()
