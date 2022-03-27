import PySimpleGUI as sg
sg.theme('DarkBlue13')

tasks = []
feitas = ["FEITAS"]

layout = [
    [sg.Text('Todo List')],
    [sg.InputText('Nova Tarefa', key='todo_item'), sg.Button(button_text='Salvar', key="add_save")],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button('Feito',button_color='Green'), sg.Button('Editar tarefa')],
   
]

window = sg.Window('Todo List', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Salvar")
    elif event == "Feito":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
    elif event == "Editar tarefa":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Salvar")
    elif event == None:
        break

window.Close()