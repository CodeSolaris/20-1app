import functions
import PySimpleGUI as sg


todos = functions.read_todos()

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window(
    "My To-Do App",
    layout=[
        [label],
        [input_box, add_button],
        [list_box],
        [edit_button, complete_button],
    ],
    font=("Helvetica", 18),
)

while True:
    event, values = window.read()

    match event:
        case "Add":
            functions.add_todo(values["todo"])
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case sg.WIN_CLOSED:
            break

window.close()
