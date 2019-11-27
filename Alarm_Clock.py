import PySimpleGUI as sg
from datetime import datetime as dt

#========== Get Time and Date ==========#
now = dt.now()

#========== Environment Theme ==========#
sg.change_look_and_feel("Reddit")

#=========== Menu Definition ===========#
menu_def = [['&File', ['&Open', '&Save', '&Exit', 'Properties']],
            ['&Alarm', ['&Add', '&Delete']],
            ['&Options', ['Run on Windows Start Up', 'About']]]

#========== Cofigure layout of the intended window ==========#
layout = [ [sg.Menu(menu_def, tearoff=True)],
           [sg.Text('Some Text on Row 1')],
           [sg.Text('Enter something on Row 2'), sg.InputText()],
           [sg.Listbox(values=('Alarm 1', 'Alarm 2', 'Alarm 3'), size=(75, 3), no_scrollbar=True)]
            ]

#========== Create Window using Window Class ==========#
window = sg.Window(now.strftime('%A, %d %B %Y' + ' Alarm Clock GUI'), layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('You entered ', values[0])

#========== Menu Functions ==========#
    if event == 'About':
        sg.popup('About this program', 'Version 1.0', 'PySimpleGUI')
    elif event == 'Open':
        filename = sg.popup_get_file('file to open', no_window=True)
        print(filename)
    elif event == 'Save':
        filename = sg.popup_get_file('file to save', no_window=True, default_extension='.txt', save_as=True)

#TODO Implement a function to exit on 'Yes' button and return on 'No' button press
    elif event == 'Exit':
        filename = sg.popup_yes_no('Are you sure you want to Exit?')
        print(values[0])

#Test Change#
window.close()

