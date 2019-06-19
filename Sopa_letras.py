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

    
def mayor_palabra(palabras):
    max=-1
    for lis in palabras:
        for a in lis:
            if len(a[0])>max:
                max=len(a[0])
    return max

def palabras_en_la_linea(coordenadas,x_o_y):
    for c in coordenadas:
        if c[0]== x_o_y:
            return True
    return False

def interpretar_reporte(fuente,fuente2):
    arch=open('Reportes_aux.json')
    data= json.load(arch)   
    tx='\n'
    for pal in data: 
        tx+= list(pal.keys())[0]+'  :'
        tx+= list(pal.values())[0]+' \n \n'
    #sg.PopupScrolled(tx)
    if(fuente2=="MAYUSCULAS"):
        tx=tx.upper()
    else:
        tx=tx.lower()
    sg.Popup(tx,font=fuente,title='Reporte',)

#----------------------------CONFIGURACION---------------------------

config =  [ [sg.T(" "),sg.Image(LOGO)],
            [sg.T(" "  * 45),sg.Text(" OPCIONES DE PALABRAS ",font="Bahnschrift",background_color="#C6C6C6")],
            [sg.T(" "  * 30),sg.InputText("",size=(40, 12),key="palabra_agregar"),sg.Button("Agregar",font="Bahnschrift 10",size=(10,1))],
            [sg.T(" "  * 30)],
            [sg.T(" " ),sg.Listbox(values=[], size=(45, 5),key="lbox",font="Bahnschrift"),sg.Button("Eliminar",font="Bahnschrift 12",size=(10,5)),sg.T(" "  * 2)],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 35),sg.Text("SUSTANTIVOS    -",font="Bahnschrift"),sg.Text("CANT:",font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_sustantivos",font="Bahnschrift 11"),sg.ColorChooserButton("COLOR",key="color_sustantivos")],
            [sg.T(" "  * 35),sg.Text("VERBO    -",font="Bahnschrift"),sg.Text("CANT:",font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_verbos",font="Bahnschrift 11"),sg.ColorChooserButton("COLOR",key="color_verbos")],
            [sg.T(" "  * 35),sg.Text("ADJETIVOS    -",font="Bahnschrift"),sg.Text("CANT:",font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_adjetivos",font="Bahnschrift 11"),sg.ColorChooserButton("COLOR",key="color_adjetivos")],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 25),sg.Text("ORIENTACION DE LAS PALABRAS:",font="Bahnschrift"), sg.InputCombo(["HORIZONTAL","VERTICAL"],key="orientacion",font="Bahnschrift 10",size=(17,5))],
            [sg.T(" "  * 25),sg.Text("¿QUE TIPO DE AYUDA DESEA DAR?:",font="Bahnschrift"), sg.InputCombo(["DEFINICIONES","LISTA DE PALABRAS"],key="ayuda",font="Bahnschrift 10",size=(17,5))],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 50),sg.Text(" FORMA DE LETRAS ",font="Bahnschrift",background_color="#C6C6C6")], 
            [sg.T(" "  * 30),sg.Text("FUENTE: ",font="Bahnschrift"),sg.InputCombo(["Bahnschrift","Trebuchet","Impact","Arial","Georgia",'ComicSansMS'],font="Bahnschrift 10",size=(12,5),key="fuente") ,sg.InputCombo(["MAYUSCULAS","MINUSCULAS"],font="Bahnschrift 10",size=(12,5),key= "may_o_min")],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 55),sg.Button("VER REPORTE",font="Bahnschrift 10")],
            [sg.T(" "  * 30)],
            [sg.T(" "  * 2),sg.RButton("",button_color=sg.TRANSPARENT_BUTTON,image_filename=JUGAR, image_subsample=2, border_width=0,key="jugar"),sg.T(" "  * 2),sg.RButton("",image_filename=CANCELAR,button_color=sg.TRANSPARENT_BUTTON, image_subsample=2, border_width=0,key="Cancelar")],
            [sg.T(" "  * 30)],
            ]

palabras={"sustantivos":[],"verbos":[],"adjetivos":[]}

windowC = sg.Window("SOPA DE LETRAS", config,disable_close=True).Finalize() 
lista_palabras=[]
lbox=windowC.Element("lbox")
while True:
    try:
        eventC, configuracion = windowC.Read()
        if(eventC=="Agregar"):
            palabra=configuracion["palabra_agregar"]
            resul=Validador_palabra.validar_palabra(palabra)
            print(resul)
            input()
            ''' if( es palabra valida):
                    agregar al diccionario la palabra 
                else:
                    sg.PopError('La palabra no es valida')'''
            lista_palabras.append(palabra)
            aux=lbox.GetListValues()
            if (not palabra in aux):#SI YA EXISTE LA PALABRA NO LA AGREGO
                aux.append(palabra)
                lbox.Update(aux)
        if(eventC=="Eliminar"):
            a_eliminar=configuracion["lbox"][0]
            aux=lbox.GetListValues()
            aux.remove(a_eliminar)
            lbox.Update(aux)
        if(eventC=='VER REPORTE'):
            interpretar_reporte(configuracion['fuente'],configuracion['may_o_min'])
        if(eventC=="Cancelar"):
            sys.exit()
        if (eventC=="jugar"):
            windowC.Close()
            break
    except(IndexError):
        continue


# -------------------------------------------------------------------  

# ------------------------ VAR --------------------------------------  

cant_palabras={"Sustantivos":0,"Verbos":0 ,"Adjetivos":0}#DESPUES DE FILTRAR SE CUANTOS HAY REALMENTE
for i in range(6):
    palabras["sustantivos"].append(["hola"])
print(palabras)

tamaño_max=mayor_palabra(list(palabras.values()))
print(tamaño_max)
nume_palabras=0

for lis in list(palabras.values()): nume_palabras+=len(lis)

print(nume_palabras)
input()
cant_ubicaciones=int(tamaño_max)+nume_palabras#tiene que ser el canta de las palabras

print(cant_ubicaciones)

if(nume_palabras>12):
    BOX_SIZE=(BOX_SIZE * 25)//30
    cant_ubicaciones=(cant_ubicaciones * 25)//30

# ------------------------ VAR -------------------------------------- 

#------------------------------PREPARACION PARTE GRAFICA------------------------

sin_ayuda = [
            [sg.Image(DECORACION,size=(100,100))],
			[sg.Text("Sustantivos:",text_color=configuracion["color_sustantivos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(cant_palabras["Sustantivos"],font="Bahnschrift 10")],
            [sg.Text("Verbos:",text_color=configuracion["color_verbos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(cant_palabras["Verbos"],font="Bahnschrift 10")],
			[sg.Text("Adjetivos:",text_color=configuracion["color_adjetivos"],font=configuracion["fuente"],background_color="#E6E6E6"),sg.Text(cant_palabras["Adjetivos"],font="Bahnschrift 10")],
			
			]


sopa = [
        [sg.Graph(canvas_size=(cant_ubicaciones*38, cant_ubicaciones*38), graph_bottom_left=(0,cant_ubicaciones*26), graph_top_right=(cant_ubicaciones*26,0), change_submits=True, drag_submits=False,background_color="white", key="graph", tooltip="SELECCIONE LAS LETRAS QUE CONFORMAN LAS PALABRAS!!")],
        [sg.T(" "  * 30)],
        [sg.Button("Controlar",font="Bahnschrift 10",size=(20,3))],
        ]

if (sg.PopupYesNo("QUIERE LAS AYUDAS?")=="Yes"):
    sopa.append([sg.Text("INFORMACION DE AYUDA:",font="Bahnschrift 10")],)
    texto=""
    for t in palabras.keys():
            for info in palabras[t]:
                if(configuracion["ayuda"] == "DEFINICIONES"):
                    texto+= info[1]+" \n"
                else:
                    texto+=info[0]+" \n"
    sopa.append([sg.Multiline(texto, size=(80,10),key="info_ayuda",font=configuracion["fuente"])],)   
    sopa.append([sg.T(" "  * 30)])    

layout = [ 
			[sg.Column(sopa), sg.Column(sin_ayuda,)],		
         ]   



window = sg.Window("SOPA DE LETRAS", layout, grab_anywhere=True).Finalize()    




g = window.Element("graph")
#graph.DrawRectangle(top_left=[tamaño_max*-17,tamaño_max*30], bottom_right=[10,50], fill_color="white", line_color="black")

#-----------------------------------------------------------------------

#------------INICIALIZACION DE MATRICES--------------------

for i in range(cant_ubicaciones):
    matriz.append([0]*cant_ubicaciones)
    matriz2.append([False]*cant_ubicaciones) 
    matriz3.append(["white"]*cant_ubicaciones)

#-----------------------------------------------------------

#-------------------------MATRIZ DIBUJO-----------------------------------------------

for row in range(cant_ubicaciones):
    print("VALOR DEL ROW " +str(row))
    for col in range(cant_ubicaciones):
            print("#############")	
            print("columna "+str(col),"ROW "+str(row))
            print(col * BOX_SIZE + 5,row * BOX_SIZE + 3)
            print("-------")
            print(col * BOX_SIZE + BOX_SIZE + 5,row * BOX_SIZE + BOX_SIZE + 3)
            print("#############")
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
            print("LA RAW: "+str(X)+" LA COL: "+str (Y))
            if(configuracion["orientacion"]== "HORIZONTAL"):
                print('CANTIDA DE ESPACIOS'+str(cant_ubicaciones - Y))
                while(cant_ubicaciones - Y < len(palabra[0])):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ 
                    print(""+str(cant_ubicaciones-Y))
                    print(Y- cant_ubicaciones < len(palabra[0]))
                    Y-=1
            else:
                while(cant_ubicaciones - X < len(palabra[0])):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ 
                    print(""+str(cant_ubicaciones-X))
                    print(X- cant_ubicaciones < len(palabra[0]))
                    X-=1
                    #input()
            if(configuracion["orientacion"]== "HORIZONTAL"):
                            coor=(X,range(Y,Y+len(palabra[0])))
            else:
                            coor=(Y,range(X,X+len(palabra[0])))
                            
            if(configuracion["orientacion"]== "HORIZONTAL"):
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,X)
                            print( palabras_en_la_linea(lista_coor_palabras,X))

            else:
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,Y)
                            print("HAY LINEA DIO:"+str(palabras_en_la_linea(lista_coor_palabras,Y)))
            if(not hay_palabra):
                    yI=Y
                    xI=X
                    for letra in palabra[0]:
                        if(configuracion["may_o_min"]== "MAYUSCULAS"):
                            letra=letra.upper()
                        else:
                            letra=letra.lower()
                        print("LUGAR DE IMPRESION = COL" +str(yI)+ "  ROW "+str(xI) )
                        g.DrawText(letra , (yI * BOX_SIZE + 18, xI * BOX_SIZE + 17),font=Fuente)
                        matriz3[yI][xI]=configuracion["color_"+ tipo]
                        if(configuracion["orientacion"]== "HORIZONTAL"):
                            yI+=1
                        else:
                            xI+=1
                    lista_coor_palabras.append(coor)
                    insertada=True
            else:
                    print("ENTRE AL ELSE")
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

#-------------------------ECRIBIR PALABRA-----------------------------------------------

#g.DrawText(random.choice(string.ascii_uppercase) , (col * BOX_SIZE + 18, row * BOX_SIZE + 17),font='Bahnschrift 20')

print(matriz)
print(matriz2)

while True:             # Event Loop
    try:
        event, values = window.Read()
        print(event, values)
        if event is None or event == "Exit":
            break
        mouse = values["graph"]

        if event == "graph":
            if mouse == (None, None):
                continue
            box_x = mouse[0]//BOX_SIZE
            box_y = mouse[1]//BOX_SIZE
            '''	print(box_x, box_y)
            print(letter_location)
            print('----------')
            print(box_x)
            print(box_y)'''
            if(matriz2[box_x][box_y] == False):
                if (matriz3[box_x][box_y]!="white"):
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill=matriz3[box_x][box_y])
                else:
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill="#CFF5E3")
                matriz2[box_x][box_y] = True
                print(matriz2[box_x][box_y])
            else :
                g.TKCanvas.itemconfig(matriz[box_x][box_y], fill="white")
                matriz2[box_x][box_y] = False
                #print(g.TKFrame(matriz[box_x][box_y], fill_color))
        elif (event=="Controlar"):
             sg.Popup("TUS PALABRAS/LETRAS FALTANTES VAN A SER MARCADAS EN GRIS!")
             print(lista_coor_palabras)
             for cor in lista_coor_palabras:
                y=cor[0]
                for x in cor[1]:
                    if  not(matriz2[x][y]):
                        print("NO ESTA MARCADO")
                        if(configuracion["orientacion"]== "HORIZONTAL"):
                            g.TKCanvas.itemconfig(matriz[x][y], fill="#C5C6C5")
                        else:
                            g.TKCanvas.itemconfig(matriz[y][x], fill="#C5C6C5")
                    else:
                        print("Esta marcado")
                
            #g.DrawRectangle((box_x * BOX_SIZE + 5, box_y * BOX_SIZE + 3),(box_x * BOX_SIZE + BOX_SIZE + 5, box_y * BOX_SIZE + BOX_SIZE + 3) ,fill_color='#CFF5E3', line_color='black')
    except(IndexError):
        continue
window.Close()
