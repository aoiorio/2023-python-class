import PySimpleGUI as sg


layout = [[sg.Text("Hello from PySimpleGUI")], 
        [sg.Text("GoodMorning from PySimpleGUI")], 
        [sg.Text("GoodMorning from PySimpleGUI"), sg.InputText()],]

window = sg.Window('title', layout)
evnet, values = window.read()
window.close()