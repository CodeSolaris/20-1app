import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_botton = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_botton]])
window.read()
window.close()
