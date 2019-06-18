import PySimpleGUI as sg
import json
import os

def consulta(word,tipo): #interfaz para verificar si el usuario desea quedarse con la palabra, aunque no este en wikt.
	layout = [[sg.Text('La palabra ' +word+ ' aparentemente es un '+tipo+'.¿Desea conservar palabra?')],
			  [sg.Button('Si'), sg.Button('No')]]

	window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)

	while True:
		ok = True
		event, values = window.Read()
		if event is None or event == 'Si': #La persona desea conservar la palabra. Pido una definición por teclado
		  if (escribir_definicion(word)==False): # Si la funcion devuelve True, significa que la persona cargó la definicion de la palabra. No se arrepintió
			  continue
		  break
		if event == 'No':
			ok=False #La persona no desea conservar la palabra
			break
	window.Close()

	return ok


def escribir_definicion(word): #interfaz para ingresar la definicion de una palabra

	layout = [
				[sg.Text('Definicion', size=(15, 1)), sg.InputText()],
				[sg.Button('Cargar'), sg.Button('Cancelar')]
				]
	window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)

	event,values = window.Read()

	while True:
		ok=True
		if event is None or event == 'Cancelar':
			ok=False
			break
		if event == 'Cargar':
			cargar_definicion(word,str (values[0]))
			break
	window.Close()

	return ok

def cargar_definicion(palabra,definicion): #carga la palabra con su definicion al archivo de definiciones(que es .json)
	if os.path.isfile('definiciones_sopa_prueba.json')==False or (os.path.getsize('definiciones_sopa_prueba.json')==0):
		with open("definiciones_sopa_prueba.json", "w") as jsonFile:
			datos = [{palabra:definicion}]
			json.dump(datos, jsonFile)
	else:
		with open("definiciones_sopa_prueba.json", "r+") as jsonFile:
			data = json.load(jsonFile)
			data.append({palabra:definicion})
			jsonFile.seek(0)
			json.dump(data, jsonFile)
			jsonFile.truncate()

consulta('german','velazquez')


# print('starting up...') # Seems to help repl.it

# layout = [[sg.Text('My one-shot window.')],
          # [sg.InputText()],
          # [sg.Submit(), sg.Cancel()]]

# window = sg.Window('Window Title', layout)

# event, values = window.Read()

# window.Close()

# print('text input was', values[0], 'button pressed was', event)

