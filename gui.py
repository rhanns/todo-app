import functions
import PySimpleGUI as gui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

gui.theme("DarkTeal2")

clock = gui.Text('', key="clock")
label = gui.Text("Type in a to do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[(45),(10)])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 10))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(values['todos'][0])
        case 'Exit':
            break
        case gui.WIN_CLOSED:
            window.close()

window.close()
