import PySimpleGUI as sg
import random
import string
import sys
import json
import Validador_palabra

BOX_SIZE=25
matriz=[]#Matriz de nombres de las figuras
matriz2=[]#Matriz de si esta pintado o no
matriz3=[]#Matriz del color al cual tiene q cambiar esa cordenada al ser seleccionada

LOGO="./IMAGENES/logosopa.png"
JUGAR="./IMAGENES/jugar.png"
CANCELAR="./IMAGENES/cancelar.png"
DECORACION="./IMAGENES/logo_decoracion.png"
SIGNO="./IMAGENES/signo.png"
REPORTE="./REPORTE/Reportes_aux.json"


def mayor_palabra(palabras):
    '''Retorna la longitud de la palabra mas grande de todas las palabras validadas '''
    max=-1
    for lis in palabras:
        for a in lis:
            if len(a[0])>max:
                max=len(a[0])
    return max

def palabras_en_la_linea(coordenadas,x_o_y):
    '''Retorna true o false, si hay una palabra en una determinada fila o una determinada columna '''
    for c in coordenadas:
        if c[0]== x_o_y:
            return True
    return False

def interpretar_reporte(fuente,fuente2):
    '''Analiza el archivo .json de reportes para mostrarlo en pantalla '''
    arch=open("./REPORTE/Reportes_aux.json")
    data= json.load(arch)
    tx='\n'
    for pal in data:
        tx+= list(pal.keys())[0]+'  :'
        tx+= list(pal.values())[0]+' \n \n'
    if(fuente2=="MAYUSCULAS"):
        tx=tx.upper()
    else:
        tx=tx.lower()
    sg.Popup(tx,font=fuente,title='Reporte',)

def mostrar_sugerencias():
    sg.Popup('''
        1- ELEGIR EL COLOR ,CON QUE SE MOSTRARAN LOS DISTITNTOS TIPOS DE PALABRAS .
        2- ELEGIR LA CANTIDAD DE CADA TIPO DE PALABRA QUE SE VAN A INGRESAR (opcional).
        3- ELEGIR LA ORIENTACION DE LAS PALABRAS(horizontal o vertical).
        4- ELEGIR SI SE DESEA TENER AYUDAS O NO(la ayuda implica contar con las definiciones de las palabras).
        5- ELEGIR LA FUENTE(opcional).
        6- ESCRIBIR LAS PALABRAS A AGREGAR DEBAJO DE "OPCIONES DE PALABRAS" Y APRETAR EL BOTON "AGREGAR" PARA AGREGAR UNA PALABRA A LA SOPA.
        7- APRETAR EN "JUGAR" PARA INICIAR LA SOPA, SINO EN "CANCELAR" PARA SALIR.  ''',font="Trebuchet 10",no_titlebar=True,grab_anywhere=True)

def elimin_palabra(palabra,dic):
    for tipo in dic.keys():
        for palabra_act in dic[tipo]:
            if palabra in palabra_act :
                dic[tipo].remove(palabra_act)
                break
    return dic

def mostrar_sugerencias_sopa():
        sg.Popup('''
                    1- CLIKEAR SOBRE LAS LETRAS QUE CREEMOS COMPONEN ALGUNA DE LAS PALABRAS BUSCADAS. CUANDO ESTEMOS SEGUROS QUE HEMOS FINALIZADOS, APRETAREMOS "CONTROLAR". 
                    2-"CONTROLAR" VERIFICARA EL RESULTADO DEL JUEGO. ES DECIR, SI SE MARCARON LAS PALABRAS CORRECTAMENTE Y, ADEMAS, SI SE HAN MARCADO LETRAS QUE NO CORRESPONDEN A NINGUNA PALABRA.
                    3- SOLO SE PUEDE CONTROLAR TRES VECES. DESPUES DE ELLO, SE MOSTRARAN LAS PALABRAS QUE HAN QUEDADO SIN MARCAR.
                    4- EL JUEGO TERMINARÁ SI EL PARTICIPANTE HA GANADO, O HA UTILIZADO SUS TRES INTENTOS. FINALMENTE SE MOSTRARÁ EL RESULTADO FINAL DE LA ACTIVIDAD ''',no_titlebar=True,grab_anywhere=True)

def color_temperatura(num):
    resul=""
    if(num <15):
        resul="blue"
    if(num>15 and num<25):
        resul="orange"
    if (num > 25):
        resul="red"
    return resul

def leer_json():
    with open ("./OFICINAS/datos-oficinas.json","r") as jsonFile:
        data = json.load(jsonFile)
        temp = data["oficina1"][0]["temp"]
        return temp


#----------------------------CONFIGURACION---------------------------

temperatura=leer_json()
color_fondo=color_temperatura(temperatura)

config1 =  [
            [sg.T(" "),sg.Image(LOGO)],
            [sg.T(" "  * 45),sg.Text(" OPCIONES DE PALABRAS ",font="Trebuchet",background_color="#C6C6C6")],
            [sg.T(" "  * 30),sg.InputText("",size=(30, 12),key="palabra_agregar"),sg.Button("Agregar",font="Trebuchet 10",size=(10,1))],
            [sg.T(" "  * 30)],
            [sg.T(" " * 20 ),sg.Listbox(values=[], size=(25, 5),key="lbox",font="Trebuchet"),sg.Button("Eliminar",font="Trebuchet 12",size=(10,5)),sg.T(" "  * 2)],
            [sg.T(" "  * 45),sg.Button("JUGADA RAPIDA",font="Trebuchet 10",key="Jugada rapida")],
            [sg.T(" "  * 30),sg.RButton("",button_color=sg.TRANSPARENT_BUTTON,image_filename=JUGAR, image_subsample=2, border_width=0,key="jugar"),sg.T(" "  * 2),],
            [sg.T(" "  * 30)],
            ]

config2= [	[sg.T(" "  * 30)],
            [sg.T(" "  * 50),sg.T("GUIA DE CONFIGURACION",font="Trebuchet 9"),sg.RButton("",image_filename=SIGNO,button_color=sg.TRANSPARENT_BUTTON,size=(2,2),auto_size_button=True,key='Guia')],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 35),sg.ColorChooserButton("COLOR",key="color_sustantivos"),sg.Text(" "*4,background_color='white',key="cuadrado_sustantivos"),sg.Text("SUSTANTIVOS    -",font="Trebuchet"),sg.Text("CANT:",font="Trebuchet"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_sustantivos",font="Trebuchet 11",readonly=True)],
            [sg.T(" "  * 35),sg.ColorChooserButton("COLOR",key="color_verbos"),sg.Text(" "*4,key="cuadrado_verbos",background_color="white"),sg.Text("VERBOS    -",font="Trebuchet"),sg.Text("CANT:",font="Trebuchet"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_verbos",font="Trebuchet 11",readonly=True)],
            [sg.T(" "  * 35),sg.ColorChooserButton("COLOR",key="color_adjetivos"),sg.Text(" "*4,background_color="white",key="cuadrado_adjetivos"),sg.Text("ADJETIVOS    -",font="Trebuchet"),sg.Text("CANT:",font="Trebuchet"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_adjetivos",font="Trebuchet 11",readonly=True)],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 25),sg.Text("ORIENTACION DE LAS PALABRAS:",font="Trebuchet"), sg.InputCombo(["HORIZONTAL","VERTICAL"],key="orientacion",font="Trebuchet 10",size=(17,5),readonly=True)],
            [sg.T(" "  * 25),sg.Text("¿QUE TIPO DE AYUDA DESEA DAR?:",font="Trebuchet"), sg.InputCombo(["DEFINICIONES","LISTA DE PALABRAS"],key="ayuda",font="Trebuchet 10",size=(17,5),readonly=True)],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 50),sg.Text(" FORMA DE LETRAS ",font="Trebuchet",background_color="#C6C6C6")],
            [sg.T(" "  * 30),sg.Text("FUENTE: ",font="Trebuchet"),sg.InputCombo(["Trebuchet","Impact","Arial","Georgia","ComicSansMS"],font="Trebuchet 10",size=(12,5),key="fuente",readonly=True) ,sg.InputCombo(["MAYUSCULAS","MINUSCULAS"],font="Trebuchet 10", size=(12,5),key= "may_o_min",readonly=True)],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 55),sg.Button("VER REPORTE",font="Trebuchet 10")],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 35),sg.RButton("",image_filename=CANCELAR,button_color=sg.TRANSPARENT_BUTTON, image_subsample=2, border_width=0,key="Cancelar")],
            [sg.T(" "  * 30)],
            ]
config = [
            [sg.Column(config1), sg.Column(config2)],
         ]

palabras={"sustantivos":[],"verbos":[],"adjetivos":[]}
windowC = sg.Window("SOPA DE LETRAS",disable_close=True,background_color=color_fondo).Layout(config)
lista_palabras=[]
lbox=windowC.Element("lbox")
while True:
    try:
        eventC, configuracion = windowC.Read()
        if configuracion["color_verbos"]!= "":#Controlamos si no le ingresamos ningun color a los verbos
            windowC.Element("cuadrado_verbos").Update(background_color=configuracion["color_verbos"])
        if configuracion["color_adjetivos"]!= "":#Controlamos si no le ingresamos ningun color a los adjetivos 
            windowC.Element("cuadrado_adjetivos").Update(background_color=configuracion["color_adjetivos"])
        if configuracion["color_sustantivos"]!= "":#Controlamos si no le ingresamos ningun color a los sustantivos 
            windowC.Element("cuadrado_sustantivos").Update(background_color=configuracion["color_sustantivos"])
        if (eventC=="Jugada rapida"):#Preparamos una configuracion predeterminada y lanzamos el juego
            palabras["sustantivos"].append(["perro"," Variedad doméstica del lobo de muchas y diversas razas, compañero del hombre desde tiempos prehistóricos."])
            palabras["sustantivos"].append(["cuaderno","conjunto de hojas donde se lleva la cuenta de una determinada actividad."])
            palabras["verbos"].append(["correr","Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas."])
            palabras["verbos"].append(["saltar","Impulsarse o lanzarse al aire."])
            palabras["adjetivos"].append(["lindo","Que es agradable a la vista o al ánimo, con un toque de ternura"])
            configuracion["color_sustantivos"]="#61ff9c"
            configuracion["color_verbos"]="#d9ff00"
            configuracion["color_adjetivos"]="#8900ff"
            windowC.Close()
            break
        if(eventC=="Guia"):
            mostrar_sugerencias()
        if(eventC=="Agregar"):
            sg.Popup('Procesando palabra... esto podria tardar unos segundos.   Presione OK para continuar',no_titlebar=True,auto_close_duration=4)
            palabra=configuracion["palabra_agregar"]
            resul=Validador_palabra.validar_palabra(palabra.lower())
            if(resul[0]== True):               
                    sg.Popup("Palabra verificada correctamente!")
                    aux=lbox.GetListValues()
                    if (not palabra in aux):#SI YA EXISTE LA PALABRA NO LA AGREGO
                        palabras[list(resul[1].keys())[0]+"s"].append(list(resul[1].values())[0])
                        aux.append(palabra)
                        lbox.Update(aux)
                    else:
                        sg.Popup('Esta palabra ya fue agregada anteriormente. Intente con una nueva')
        if(eventC=="Eliminar"):
            a_eliminar=configuracion["lbox"][0]
            palabras=elimin_palabra(a_eliminar,palabras)
            aux=lbox.GetListValues()
            aux.remove(a_eliminar)
            lbox.Update(aux)
        if(eventC=='VER REPORTE'):
            interpretar_reporte(configuracion['fuente'],configuracion['may_o_min'])
        if(eventC=="Cancelar"):
            sys.exit()
        if (eventC=="jugar"):
            if (configuracion["color_verbos"]== "" or configuracion["color_adjetivos"]== "" or configuracion["color_sustantivos"]== ""):#controla que se seleccionaron colores
                sg.Popup("Seleccione los colores faltantes para los tipos de palabra!")
            else:
                windowC.Close()
                break
    except(IndexError):
        continue


# -------------------------------------------------------------------

# ------------------------ VAR --------------------------------------

cant_palabras={"Sustantivos":0,"Verbos":0 ,"Adjetivos":0}#DESPUES DE FILTRAR SE CUANTOS HAY REALMENTE


tamaño_max=mayor_palabra(list(palabras.values()))
nume_palabras=0

for lis in list(palabras.values()): nume_palabras+=len(lis)

cant_ubicaciones=int(tamaño_max)+nume_palabras#tiene que ser el canta de las palabras


if(nume_palabras>12):
    BOX_SIZE=(BOX_SIZE * 25)//30
    cant_ubicaciones=(cant_ubicaciones * 25)//30

# ------------------------ VAR --------------------------------------

#------------------------------PREPARACION PARTE GRAFICA------------------------

sin_ayuda = [
            [sg.Image(DECORACION,size=(100,100))],
            [sg.T("SUGERENCIA",font=configuracion["fuente"]),sg.RButton("",image_filename=SIGNO,button_color=sg.TRANSPARENT_BUTTON,size=(2,2),auto_size_button=True,key='Sugerencia')],
            [sg.T('Intentos : ',font=configuracion["fuente"]),sg.T('3',font=configuracion["fuente"],key='Intentos',)],
            [sg.Text("Sustantivos:",text_color=configuracion["color_sustantivos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(len(palabras["sustantivos"]),font="Trebuchet 10")],
            [sg.Text("Verbos:",text_color=configuracion["color_verbos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(len(palabras["verbos"]),font="Trebuchet 10")],
            [sg.Text("Adjetivos:",text_color=configuracion["color_adjetivos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(len(palabras["adjetivos"]),font="Trebuchet 10")],

            ]


sopa = [
        [sg.Graph(canvas_size=(cant_ubicaciones*38, cant_ubicaciones*38), graph_bottom_left=(0,cant_ubicaciones*26), graph_top_right=(cant_ubicaciones*26,0), change_submits=True, drag_submits=False,background_color="white", key="graph", tooltip="SELECCIONE LAS LETRAS QUE CONFORMAN LAS PALABRAS!!")],
        [sg.T(" "  * 30)],
        [sg.Button("Controlar",font="Trebuchet 10",size=(20,3))],
        ]

if (sg.PopupYesNo("QUIERE LAS AYUDAS?",no_titlebar=True)=="Yes"):
    sin_ayuda.append([sg.Text("INFORMACION DE AYUDA:",font="Trebuchet 10")],)
    texto=""
    for t in palabras.keys():
            for info in palabras[t]:
                if(len(info) !=0):
                    if(configuracion["ayuda"] == "DEFINICIONES"):
                        texto+= info[1]+" \n \n"
                    else:
                        texto+=info[0]+" \n \n"
    sin_ayuda.append([sg.Multiline(texto, size=(30,10),key="info_ayuda",font=configuracion["fuente"],enter_submits=True,disabled=True)],)
    sin_ayuda.append([sg.T(" "  * 30)])



layout = [
            [sg.Column(sopa), sg.Column(sin_ayuda,)],
         ]



window = sg.Window("SOPA DE LETRAS",background_color=color_fondo).Layout(layout).Finalize()





g = window.Element("graph")

#-----------------------------------------------------------------------

#------------INICIALIZACION DE MATRICES--------------------

for i in range(cant_ubicaciones):
    matriz.append([0]*cant_ubicaciones)
    matriz2.append([False]*cant_ubicaciones)
    matriz3.append(["white"]*cant_ubicaciones)

#-----------------------------------------------------------

#-------------------------MATRIZ DIBUJO-----------------------------------------------

for row in range(cant_ubicaciones):
    for col in range(cant_ubicaciones):
            matriz[col][row]=g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color="black")

#---------------------------------------------------------------------------------------

#FORMATO DE LAS LETRAS

Fuente=configuracion["fuente"]

#------------------------------------------------------------------------------------

#-------------------------ESCRIBIR PALABRA-----------------------------------------------



lista_coor_palabras=[]#lista de cordenadas de cada palabra
for tipo in palabras.keys():
    l_palabras=palabras[tipo]
    for palabra in l_palabras:
        insertada=False
        X=random.randint(0,cant_ubicaciones-2)
        Y=random.randint(0,cant_ubicaciones-2)
        while not insertada:
            if(configuracion["orientacion"]== "HORIZONTAL"):
                while(cant_ubicaciones - Y < len(palabra[0])):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ
                    Y-=1
            else:
                while(cant_ubicaciones - X < len(palabra[0])):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ
                    X-=1
            if(configuracion["orientacion"]== "HORIZONTAL"):
                            coor=(X,range(Y,Y+len(palabra[0])))
            else:
                            coor=(Y,range(X,X+len(palabra[0])))

            if(configuracion["orientacion"]== "HORIZONTAL"):
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,X)

            else:
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,Y)
            if(not hay_palabra):
                    yI=Y
                    xI=X
                    for letra in palabra[0]:
                        if(configuracion["may_o_min"]== "MAYUSCULAS"):
                            letra=letra.upper()
                        else:
                            letra=letra.lower()
                        g.DrawText(letra , (yI * BOX_SIZE + 18, xI * BOX_SIZE + 17),font=Fuente)
                        try:
                            matriz3[yI][xI]=configuracion["color_"+ tipo]
                        except(IndexError):
                            continue
                        if(configuracion["orientacion"]== "HORIZONTAL"):
                            yI+=1
                        else:
                            xI+=1
                    lista_coor_palabras.append(coor)
                    insertada=True
            else:
                    X=random.randint(0,cant_ubicaciones)
                    Y=random.randint(0,cant_ubicaciones)

#-----------------------LETRAS ALEATOREAS--------------------------------------------------------------

for row in range(cant_ubicaciones):
    for col in range(cant_ubicaciones):
        if(configuracion["may_o_min"]== "MAYUSCULAS"):
            letra=string.ascii_uppercase
        else:
            letra=string.ascii_lowercase
        if(configuracion["orientacion"]== "HORIZONTAL"):
                if(matriz3[col][row] == "white"):
                    g.DrawText(random.choice(letra) , (col * BOX_SIZE + 18, row * BOX_SIZE + 17),font=Fuente)
        else:
            if(matriz3[row][col] == "white"):
                    g.DrawText(random.choice(letra) , (row * BOX_SIZE + 18, col * BOX_SIZE + 17),font=Fuente)

#-------------------------ESCRIBIR PALABRA-----------------------------------------------

intento=3
while True:            
    try:
        event, values = window.Read()
        intentos=window.Element("Intentos")
        if event is None or event == "Exit":
            break
        mouse = values["graph"]
        if event == "Sugerencia":
            mostrar_sugerencias_sopa()
        if event == "graph":
            if mouse == (None, None):
                continue
            box_x = mouse[0]//BOX_SIZE
            box_y = mouse[1]//BOX_SIZE
            if(matriz2[box_x][box_y] == False):
                if (matriz3[box_x][box_y]!="white"):
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill=matriz3[box_x][box_y])
                else:
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill="#CFF5E3")
                matriz2[box_x][box_y] = True
            else :
                g.TKCanvas.itemconfig(matriz[box_x][box_y], fill="white")
                matriz2[box_x][box_y] = False
        elif (event=="Controlar"):#MODIFICA ACAAAA
             intento=int(intento)-1
             intentos.Update(intento)
             if (intento>0):
                 gano=True
                 matriz2_aux=matriz2.copy()
                 matriz_aux=matriz3.copy()
                 for cor in lista_coor_palabras:
                    y=cor[0]
                    for x in cor[1]:
                        if  (matriz2[x][y]):
                            if(configuracion["orientacion"]== "HORIZONTAL"):
                                g.TKCanvas.itemconfig(matriz[x][y], fill="green")
                            else:
                                g.TKCanvas.itemconfig(matriz[y][x], fill="green")
                        else:
                            gano=False
                 sg.Popup('Lo marcado en verde son tus aciertos!')
                 matriz2=matriz2_aux.copy()
                 matriz3=matriz_aux.copy()
                 if (gano):
                     sg.Popup("GANASTE !",title="Resultado" ,text_color="green",font=configuracion["fuente"])
                     break

                 for cor in lista_coor_palabras:
                    y=cor[0]
                    for x in cor[1]:
                        if  (matriz2[x][y]):
                            if(configuracion["orientacion"]== "HORIZONTAL"):
                                g.TKCanvas.itemconfig(matriz[x][y], fill=matriz3[x][y])
                            else:
                                g.TKCanvas.itemconfig(matriz[y][x], fill=matriz3[x][y])
                        
             else:
                 perdio=True
                 for cor in lista_coor_palabras:
                    y=cor[0]
                    for x in cor[1]:
                        if  not(matriz2[x][y]):
                            if(configuracion["orientacion"]== "HORIZONTAL"):
                                g.TKCanvas.itemconfig(matriz[x][y], fill="red")
                            else:
                                g.TKCanvas.itemconfig(matriz[y][x], fill="red")
                        else: pedrio=False
                 if (perdio):
                            sg.Popup("PERDISTE :c",title="Resultado" ,text_color="red",font=configuracion["fuente"])
                            break
                 intento-= intento
                 intentos.Update(intento)
                 


    except(IndexError):
        continue

sg.Popup('Gracias por jugar :D',font=configuracion["fuente"]+ " 20",no_titlebar=True,auto_close_duration=4)
window.Close()
