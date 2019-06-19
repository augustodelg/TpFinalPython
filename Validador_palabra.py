#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pattern.web import Wiktionary
from pattern.es import parse,split


def validar_palabra(word):
    wik = Wiktionary(language="es")
    valida = False
    ok = False
    while (ok == False):
        article = wik.search(word)
        try:
            lis_sections = list(article.sections)
            title_aux = []
            lis_sections.pop(0)# saco de la lista el primer elemento que, es siempre, la misma palabra buscada.
            tipo = "zzz"
            ok = True
            for section in lis_sections:
                title = section.title  # guardo en title el titulo correspondiente a cada seccion
                title_aux = title.split(" ")
                tipo = evaluar(title_aux,tipo)
                if (tipo != "zzz"): #esto sucede cuando la palabra encontrada es de alguno de los tipos tratatos en evaluar()
                    break
            if (tipo==tipo_pattern(word)):
                valida = True
       
        except AttributeError: # Error en el caso de que la palabra no exista en wiktionary
            tipo_aux = tipo_pattern(word)
            valida =consulta(word,tipo_aux)
            return valida

    return valida 
                           

def escribir_definición(word):
    layout = [           
                [sg.Text('Definicion', size=(15, 1)), sg.InputText()],            
                [sg.Button('Cargar')]      
                ]     
    window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)
    
	while True:
      ok = True  
	  event, values = window.Read()
	  if event is None or event == 'No': #Si la persona desea conservar la palabra, pido una definición por teclado
		  escribir_definición(word)  
		  break  
	  if event == 'Si':
          ok=False #Significa que la palabra no es válida
		  break
	window.Close()


def consulta(word,tipo):
	layout = [[sg.Text('La palabra ' +word+ ' aparentemente es un '+tipo+'.¿Desea elegir una nueva palabra?')],  
			  [sg.Button('Si'), sg.Button('No')]]  

	window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)

	while True:
      ok = True  
	  event, values = window.Read()
	  if event is None or event == 'No': #Si la persona desea conservar la palabra, pido una definición por teclado
		  escribir_definición(word)  
		  break  
	  if event == 'Si':
          ok=False #Significa que la palabra no es válida
		  break
	window.Close()  

def tipo_pattern(word): #retorna el tipo gramatico de la palabra, definido por pattern.es
    diccionario_de_tipos = {"NN": "sustantivo", "JJ": "adjetivo", "VB": "verbo"}
    aux = parse(word).split("/")
    tipo_pat = aux[1] #NN.JJ.VB u otros
    llaves_diccionario = list(diccionario_de_tipos.keys())
    if (tipo_pat in llaves_diccionario):
        return diccionario_de_tipos[tipo_pat] # si el tipo_pat retorna NN,JJ o VB, entonces retorno la clave correspondiente 
    else: 
        return tipo_pat
     

def evaluar(title_aux,tipo):
    lis_gramatica = ["Artículo", "Pronombre", "Adverbio","Interjección", "Preposición", "Conjunción"]
    if (title_aux[0] == 'Verbo'):
        tipo = "verbo"
    if title_aux[0] == 'Sustantivo':
        tipo = "sustantivo"
    if (title_aux[0] == "Adjetivo"):
        tipo = "adjetivo"
    if (title_aux[0] == 'Forma'):
        if (title_aux[1] == 'verbal'):
            tipo = "verbo"
        if (title_aux[1] == 'adjetiva'):
            tipo = "adjetivo"
    if (title_aux[0] in lis_gramatica):
        print("La palabra ingresada, no está en las categorías gramaticales permitidas. Ingrese un sustantivo, adjetivo o verbo")
        tipo = "inválido"
    return tipo
    



