import PySimpleGUI as sg
from .compute_units import convert_units

def convert_units_gui():

	# sg.theme('DarkAmber')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Text('Introduce your number with units:'), sg.InputText(key='in_text_with_units', )],
				[sg.Text('Introduce the new units:'), sg.InputText(key='new_units')],
				[sg.Text('the result will appear here',key='Result', size=(80,1))],
	            [sg.Button('Compute!'), sg.Button('to SI', key='to_SI'), sg.Button('Exit')], 
	            ]

	# Create the Window
	window = sg.Window('Window Title', layout, font=("Helvetica", 22))

	# Event Loop to process "events" and get the "values" of the inputs
	while True:
	    event, values = window.read()
	    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
	        break
	    
	    in_text_with_units = values['in_text_with_units']
	    new_units          = values['new_units']


	    if event == 'to_SI':
	        number_with_new_units = convert_units(in_text_with_units)
	    else: 
	    	number_with_new_units = convert_units(in_text_with_units, new_units)


	    window['Result'].update(number_with_new_units)

	window.close()