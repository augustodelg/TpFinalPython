#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import json
import os
from pattern.web import Wiktionary
from pattern.es import parse,split


def validar_palabra(word):
    lis_resultados = [None,None] #lista a retornar, donde la posicion 0 dice si la palabra es válida, y en la posicion 1, un diccionario.
    lis_tipo_validos = ["sustantivo","adjetivo","verbo"]
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
                    if tipo in lis_tipo_validos:
                        definicion = buscar_definicion(word,section.string)
                        valida = True
                        if (tipo!=tipo_pattern(word)):
                            generar_reporte(word,"La palabra es valida, sin embargo algunos criterios de busqueda pudieron diferir")
                    else:
                        definicion = None
                    break                    
            lis_resultados[0] = valida
            lis_resultados[1] = {tipo: [word,definicion]}
            return lis_resultados
       
        except AttributeError: # Error en el caso de que la palabra no exista en wiktionary
            tipo_aux = tipo_pattern(word)
            lis_consul =consulta(word,tipo_aux)########################################3
            if (lis_consul[0]==False):
                generar_reporte(word,"La palabra no es valida, ya que ningun criterio de busqueda pudo determinarla")
            lis_resultados[0] = lis_consul[0]
            lis_resultados[1] = {tipo_aux: [word,lis_consul[1]]} 
            return lis_resultados

def buscar_definicion(word,texto):
    punto_final=0
    punto_index=0
    cont=0
    definicion=""
    for caracter in texto:
        if caracter.isdigit():
            numero_index=cont
            break
        cont=cont+1	

    for x in range(numero_index,len(texto)+1):
        if texto[x] ==".":
            punto_index=cont
            break
        cont=cont+1

    aux=texto[punto_index+1]

    if aux.isalpha():
        for y in range (punto_index+1,len(texto)+1):
            if texto[y] ==".":
                punto_final=cont
                break
            cont=cont+1
        definicion = texto[numero_index+1:punto_final+1]
    else:
        definicion =texto[numero_index+1:punto_index+1]
        
    return definicion


def generar_reporte(palabra,motivo):
     if os.path.isfile('Reportes_aux.json')==False or (os.path.getsize('Reportes_aux.json')==0):
         with open("Reportes_aux.json", "w") as jsonFile:
             datos = [{palabra:motivo}]
             json.dump(datos, jsonFile,indent=4)
     else:
         with open("Reportes_aux.json", "r+") as jsonFile:
             data = json.load(jsonFile)
             data.append({palabra:motivo})
             jsonFile.seek(0)
             json.dump(data, jsonFile,indent=4)
             jsonFile.truncate()

                           

def consulta(word,tipo): #interfaz para verificar si el usuario desea quedarse con la palabra, aunque no este en wikt.
    layout = [[sg.Text('La palabra ' +word+ ' aparentemente es un '+tipo+'.¿Desea conservar palabra?')],
              [sg.Button('Si'), sg.Button('No')]]

    window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)
    lis_resul = [None,None]

    while True:
        ok = True
        event, values = window.Read()
        if event is None or event == 'Si': #La persona desea conservar la palabra. Pido una definición por teclado
          definicion = escribir_definicion(word)
          if (definicion == "False"):
              continue
          lis_resul[1] = definicion
          break
        if event == 'No':
            ok=False #La persona no desea conservar la palabra
            break
    window.Close()
    lis_resul[0] = ok
    return lis_resul


def escribir_definicion(word): #interfaz para ingresar la definicion de una palabra

    layout = [
                [sg.Text('Definicion', size=(15, 1)), sg.InputText(key="definicion")],
                [sg.Button('Cargar')]
                ]
    window = sg.Window('-JUEGO CON SOPA DE LETRAS-').Layout(layout)

    event,values = window.Read()

    while True:
        ok=True
        if event is None:
            ok=False
            return str(ok)
            break
        if event == 'Cargar': #----------ENVIAR LA PALABRA Y LA DEFINICION A LA LISTA DE PALABRAS VALIDAS
            definicion = values["definicion"]
            break
    window.Close()
    
    return definicion

def tipo_pattern(word): #retorna el tipo gramatico de la palabra, definido por pattern.es
    diccionario_de_tipos = {"NN": "sustantivo", "JJ": "adjetivo", "VB": "verbo"}
    aux = parse(word).split("/")
    tipo_pat = aux[1] #NN.JJ.VB u otros
    if tipo_pat in ["JJ","JJR","JJS","MD"]:
        tipo_pat = "adjetivo"
    if tipo_pat in ["NN","NNS","NNP","NNPS"]:
        tipo_pat = "sustantivo"
    if tipo_pat in ["VB","VBZ","VBP","VBD","VBN","VBG"]:
        tipo_pat = "verbo"
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
        if (title_aux[1]=="sustantiva"):
            tipo = "sustantivo" 
    if (title_aux[0] in lis_gramatica):
        sg.PopupError("La palabra ingresada, no está en las categorías gramaticales permitidas. Ingrese un sustantivo, adjetivo o verbo")
        tipo = "inválido"
    return tipo


