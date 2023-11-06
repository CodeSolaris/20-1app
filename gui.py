import datetime
import os

import PySimpleGUI as sg

import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todo_list = functions.get_todo_list()


sg.theme("Dark Blue")
background_color = sg.theme_background_color()

clock_label = sg.Text("", key="clock", font=("Helvetica", 18))

label = sg.Text("Type in a to-do")
input_todo = sg.InputText(tooltip="Enter todo", key="todo", pad=(7, 0))
add_button = sg.Button("Add", size=(4, 0), pad=(30, 0))
space = sg.Text("", size=(0, 1))

list_box = sg.Listbox(
    values=todo_list,
    key="todo_list",
    enable_events=True,
    size=[45, 10],
)

left_col = sg.Column([[list_box]])

edit_button = [sg.Button("Edit")]
vert_space = [sg.VerticalSeparator(pad=(50, 50), color=background_color)]
exit_button = [sg.Button("Exit")]

right_col = sg.Column([edit_button, vert_space, exit_button], vertical_alignment="top")
space1 = sg.Text("", size=(0, 1))
output_label = sg.Text("", key="output")

window = sg.Window(
    "My To-Do App",
    layout=[
        [clock_label],
        [label],
        [input_todo, add_button],
        [space],
        [left_col, right_col],
        [space1],
        [sg.Button("Complete"), output_label],
    ],
    font=("Helvetica", 18),
)


while True:
    event, values = window.read(timeout=200)

    current_time = datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
    window["clock"].update(value=current_time)

    match event:
        case "Add":
            todo = values["todo"]
            functions.add_todo(todo)
            todo_list = functions.get_todo_list()
            functions.window_update(todo_list, window)

        case "Exit":
            break

        case "Edit":
            try:
                todo_to_edit = values["todo_list"][0]
                new_todo = values["todo"]

                index = todo_list.index(todo_to_edit)
                todo_list[index] = new_todo
                functions.write_todo_list(todo_list)
                functions.window_update(todo_list, window)
            except IndexError:
                window["output"].update(value="Please, select a todo first.")

        case "todo_list":
            window["output"].update(value="")
            window["todo"].update(value=values["todo_list"][0])

        case "Complete":
            try:
                todo_to_complete = values["todo_list"][0]
                todo_list.remove(todo_to_complete)
                functions.write_todo_list(todo_list)
                functions.window_update(todo_list, window)
            except IndexError:
                window["output"].update(value="Please, select a todo first.")

        case sg.WIN_CLOSED:
            break

window.close()
