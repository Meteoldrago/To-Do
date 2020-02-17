import PySimpleGUI as sg
from data_base import *
sg.theme('DarkBrown4')
tasks = import_db()
edit_val = ''
while True:
    layout = [
        [sg.Text('ToDo')],
        [sg.InputText(edit_val,key='todo_item'), sg.Button(button_text='Add', key="add_save")],
        [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Update')],
    ]
    layout1 = [[sg.InputCombo(['High','Medium','Low'],key = 'ch')],[sg.Button('OK')]]
    layout2 = [[sg.InputText('DD-MM-YYYY',key = 'dt')],[sg.Button('OK')]]
    layout3 = [[sg.InputCombo(['High','Medium','Low'],key = 'ch1')],[sg.Button('OK')],[sg.Button('SKIP')]]
    layout4 = [[sg.InputText('DD-MM-YYYY', key='dt1')], [sg.Button('OK')],[sg.Button('SKIP')]]
    window = sg.Window('ToDo App', layout)
    window1 = sg.Window('Priority', layout1)
    window2 = sg.Window('Date', layout2)
    window3 = sg.Window('Priority1', layout3)
    window4 = sg.Window('Date1', layout4)

    event, values = window.Read()
    if event == "add_save":
        button, date1 = window2.read()
        pri, choice = window1.read()
        tasks_input(values['todo_item'],choice['ch'],date1['dt'])
        window1.Close()
        window2.Close()
        tasks = import_db()
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
    elif event == "Delete":
        tasks = import_db()
        tasks_delete(values["items"][0])
        tasks = import_db()
        window.FindElement('items').Update(values=tasks)
    elif event == "Update":
        tasks = import_db()
        edit_val = values['todo_item']
        button, date1 = window4.read()
        pri, choice = window3.read()
        if(button == 'SKIP'):
            date1['dt1'] = values["items"][0][2]
        if(pri == 'SKIP'):
            choice['ch1'] = values["items"][0][1]
        tasks_update(values["items"][0][0],values['todo_item'], choice['ch1'], date1['dt1'])
        window3.Close()
        window4.Close()
        tasks = import_db()
        window.FindElement('items').Update(values=tasks)
    elif event == None:
        break

window.Close()
