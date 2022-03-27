import PySimpleGUI as sg 

def criar_janela_inicial():
    sg.theme('DarkBlue13')
    linha = [ 
        [sg.Checkbox('',checkbox_color='Green'),sg.Input('')]
    ]
    layout = [ 
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List',layout=layout,finalize=True)

janela = criar_janela_inicial()

while True:
    event,values = janela.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox('',checkbox_color='Green'),sg.Input('')]])

    if event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()

