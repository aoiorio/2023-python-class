import PySimpleGUI as sg # PySimpleGUIをimport(追加)

# layoutを決める
layout = [[sg.Text("Hello from PySimpleGUI")],
        [sg.Text("GoodMorning from PySimpleGUI")],
        [sg.Text("GoodMorning from PySimpleGUI"), sg.InputText()],] # テキストを入力することが出来る

window = sg.Window('title', layout) # windowを表示する
evnet, values = window.read()
window.close() #ファイルを閉じるコード
