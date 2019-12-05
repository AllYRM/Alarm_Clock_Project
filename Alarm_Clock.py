import PySimpleGUI as sg
from datetime import datetime as dt

#========== Get Time and Date ==========#
now = dt.now()

if __name__ == '__main__':

    #========== Environment Theme ==========#
    sg.change_look_and_feel("Reddit")

    #=========== Menu Definition ===========#
    menu_def = [['&File', ['&Open', '&Save', '&Exit', 'Properties']],
                ['&Alarm', ['&Add', '&Delete']],
                ['&Options', ['Run on Windows Start Up', 'About']]]

    #========== Cofigure layout of the Main window ==========#
    layout = [ [sg.Menu(menu_def, tearoff=True)],
               [sg.Text('Some Text on Row 1')],
               [sg.Text('Enter something on Row 2'), sg.InputText()],
               [sg.Listbox(values=('Alarm 1', 'Alarm 2', 'Alarm 3'), size=(75, 3), no_scrollbar=True, right_click_menu= ['&Right', ['Add', 'Change', 'Delete']], enable_events=True)]
                ]
    #=========== Configure layout of Add Alarm Window ==========#
    add_alarm = [[sg.Text('Some Text on Row 1')],
                [sg.Frame(layout=[[sg.CBox('Every Sunday', size=(10, 1))],
                [sg.CBox('Every Monday', size=(10, 1))], [sg.CBox('Every Tuesday', size=(10, 1))],
                [sg.CBox('Every Wednesday', size=(10, 1))], [sg.CBox('Every Thuresday', size=(10, 1))],
                [sg.CBox('Every Friday', size=(10, 1))], [sg.CBox('Every Saturday', size=(10, 1))]], title='Repeat', border_width=1)]
                #[sg.Text('Enter something on Row 2'), sg.InputText()],
                #[sg.Listbox(values=('Alarm 1', 'Alarm 2', 'Alarm 3'), size=(75, 3), no_scrollbar=True)]
                ]

    #========== Create Windows using Window Class ==========#
    window = sg.Window(now.strftime('%A, %d %B %Y' + ' Alarm Clock GUI'), layout)
    alarm_window = sg.Window('Create Alarm', add_alarm, auto_size_text=True, default_element_size=(50, 1))

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

        elif event == 'Exit':
            filename = sg.popup_yes_no('Are you sure you want to Exit?')
            if filename == 'Yes':
                window.close()
            print(filename)

        elif event == 'Add':
            filename = sg.popup(alarm_window.read())

    alarm_window.close()
    window.close()

