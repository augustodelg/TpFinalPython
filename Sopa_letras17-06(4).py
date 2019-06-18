import PySimpleGUI as sg
import random
import string
import sys

BOX_SIZE=25
matriz=[]#Matriz de nombres de las figuras
matriz2=[]#Matriz de si esta pintado o no
matriz3=[]#Matriz del color al cual tiene q cambiar esa cordenada al ser seleccionada

LOGO="./IMAGENES/logosopa.png"
JUGAR="./IMAGENES/jugar.png"
CANCELAR="./IMAGENES/cancelar.png"
DECORACION="./IMAGENES/logo_decoracion.png"

def insertar_palabra(col,row,palabra,color):
    colI=col
    rowI=row
    for letra in palabra:
            print('LUGAR DE IMPRESION = COL' +str(colI)+ '  ROW '+str(rowI) )
            g.DrawText(letra , (colI * BOX_SIZE + 18, rowI * BOX_SIZE + 17),font='Bahnschrift 20')
            print(colores[color])
            matriz3[colI][rowI]=colores[color]
            colI+=1
    
def mayor_palabra(palabras):
    max=-1
    for lis in palabras:
        for a in lis:
            if len(a)>max:
                max=len(a)
    return max

def palabras_en_la_linea(coordenadas,x_o_y):
    for c in coordenadas:
        if c[0]== x_o_y:
            return True
    return False
#----------------------------CONFIGURACION---------------------------
config =  [ [sg.T(' '),sg.Image(LOGO)],
            [sg.T(' '  * 45),sg.Text('OPCIONES DE PALABRAS',font="Bahnschrift",background_color='#C6C6C6')],
            [sg.T(' '  * 28),sg.InputText('',size=(40, 12),key='palabra_agregar'),sg.Button('Agregar',font="Bahnschrift")],
            [sg.T(' '  * 30)],
            [sg.Listbox(values=[], size=(50, 10),key='lbox',font="Bahnschrift"),sg.Button('Eliminar',font="Bahnschrift",size=(10,5))],
            [sg.T(' '  * 30)],
            [sg.T(' '  * 35),sg.Text('SUSTANTIVOS    -',font="Bahnschrift"),sg.Text('CANT:',font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_sustantivos",font="Bahnschrift"),sg.ColorChooserButton('COLOR',key='color_sustantivos')],
            [sg.T(' '  * 35),sg.Text('VERBO    -',font="Bahnschrift"),sg.Text('CANT:',font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_verbos",font="Bahnschrift"),sg.ColorChooserButton('COLOR',key='color_verbos')],
            [sg.T(' '  * 35),sg.Text('ADJETIVOS    -',font="Bahnschrift"),sg.Text('CANT:',font="Bahnschrift"), sg.InputCombo([0,1,2,3,4,5,6],key="cant_adjetivos",font="Bahnschrift"),sg.ColorChooserButton('COLOR',key='color_adjetivos')],
            [sg.T(' '  * 30)],
            [sg.T(' '  * 25),sg.Text('ORIENTACION DE LAS PALABRAS:',font="Bahnschrift"), sg.InputCombo(['HORIZONTAL','VERTICAL'],key="orientacion",font="Bahnschrift")],
            [sg.T(' '  * 25),sg.Text('QUE TIPO DE AYUDA DESEA DAR?:',font="Bahnschrift"), sg.InputCombo(['DEFINICIONES','LISTA DE PALABRAS'],key="ayuda",font="Bahnschrift",size=(5,5))],
            [sg.T(' '  * 30)],
            [sg.T(' '  * 50),sg.Text('FORMA DE LETRAS ',font="Bahnschrift",background_color='#C6C6C6')], 
            [sg.T(' '  * 35),sg.Text('FUENTE: ',font="Bahnschrift"),sg.InputCombo(['Arial','Bahnschrift'],key="fuente") ,sg.InputCombo(['MAYUSCULAS','MINUSCULAS'],key= "may_o_min")],
            [sg.T(' '  * 30)],
            [sg.T(' '  * 2),sg.RButton('',button_color=sg.TRANSPARENT_BUTTON,image_filename=JUGAR, image_subsample=2, border_width=0,key='jugar'),sg.T(' '  * 3),sg.RButton('',image_filename=CANCELAR,button_color=sg.TRANSPARENT_BUTTON, image_subsample=2, border_width=0,key="cancelar")],
            [sg.T(' '  * 30)],
            ]
windowC = sg.Window('SOPA DE LETRAS', config, grab_anywhere=True).Finalize() 
lista_palabras=[]
lbox=windowC.Element('lbox')
while True:
    eventC, configuracion = windowC.Read()
    if(eventC=='Agregar'):
        palabra=configuracion['palabra_agregar']
        lista_palabras.append(palabra)
        print(palabra)
        print(lbox.GetListValues())
        #configuracion['listado_palabras'].Update(value=configuracion['listado_palabras'].append(palabra))
        aux=lbox.GetListValues()
        if (not palabra in aux):#SI YA EXISTE LA PALABRA NO LA AGREGO
            aux.append(palabra)
            lbox.Update(aux)
    if(eventC=='Eliminar'):
        a_eliminar=configuracion["lbox"][0]
        aux=lbox.GetListValues()
        aux.remove(a_eliminar)
        lbox.Update(aux)
    if(eventC=='cancelar'):
        sys.exit()
    if (eventC=='jugar'):
        break


# -------------------------------------------------------------------  

# ------------------------ VAR --------------------------------------  

colores={'Sustantivos':"red",'Verbo':"green" ,'Adjetivos':"purple"}
cant_palabras={'Sustantivos':0,'Verbos':0 ,'Adjetivos':0}#DESPUES DE FILTRAR SE CUANTOS HAY REALMENTE
palabras={'Sustantivos':["TOMATE","MINERVA","MANZANA"],'Verbo':["CORRER","SALTAR"]}
tamaño_max=mayor_palabra(list(palabras.values()))
nume_palabras=0
for lis in list(palabras.values()):
    for a in lis:
        nume_palabras+=1

cant_ubicaciones=int(tamaño_max)+nume_palabras#tiene q serel canta de las palabras
print(cant_ubicaciones)

# ------------------------ VAR -------------------------------------- 

#------------------------------SOPA DE LETRAS------------------------

sin_ayuda = [
            [sg.Image(DECORACION,size=(100,100))],
			[sg.Text("Sustantivos:",text_color=configuracion['color_sustantivos'],font='Bahnschrift 10',background_color='#E6E6E6'),sg.Text(cant_palabras["Sustantivos"],font='Bahnschrift 10')],
            [sg.Text("Verbos:",text_color=configuracion['color_verbos'],font='Bahnschrift 10',background_color='#E6E6E6'),sg.Text(cant_palabras["Verbos"],font='Bahnschrift 10')],
			[sg.Text("Adjetivos:",text_color=configuracion['color_adjetivos'],font='Bahnschrift 10',background_color='#E6E6E6'),sg.Text(cant_palabras["Adjetivos"],font='Bahnschrift 10')],
			
			]

'''ayuda1 = [[sg.Text('INFORMACION DE AYUDA:')]],
        [[sg.Multiline('', size=(45,10),key="info_ayuda")]],
        ]'''

sopa = [
        [sg.Graph(canvas_size=(cant_ubicaciones*38, cant_ubicaciones*38), graph_bottom_left=(0,cant_ubicaciones*26), graph_top_right=(cant_ubicaciones*26,0), change_submits=True, drag_submits=False,background_color='white', key='graph', tooltip='SELECCIONE LAS LETRAS QUE CONFORMAN LAS PALABRAS!!')],
        [sg.T(' '  * 30)],
        [sg.Button('Controlar',font='Bahnschrift 10',size=(20,3))],
        ]

if (sg.PopupYesNo('QUIERE LAS AYUDAS?')=='Yes'):
    sopa.append([sg.Text('INFORMACION DE AYUDA:',font='Bahnschrift 10')],)
    sopa.append([sg.Multiline('', size=(80,10),key="info_ayuda")],)   
    sopa.append([sg.T(' '  * 30)])    

layout = [ 
			[sg.Column(sopa), sg.Column(sin_ayuda)],		
         ]   



window = sg.Window('SOPA DE LETRAS', layout, grab_anywhere=True).Finalize()    




g = window.Element('graph')
#graph.DrawRectangle(top_left=[tamaño_max*-17,tamaño_max*30], bottom_right=[10,50], fill_color="white", line_color="black")

#------------------------------SOPA DE LETRAS------------------------

for i in range(cant_ubicaciones):
    matriz.append([0]*cant_ubicaciones)
    matriz2.append([False]*cant_ubicaciones) 
    matriz3.append(['white']*cant_ubicaciones)

print(matriz)
print('TAMAÑO MATRIZ COLORES  '+str(len(matriz3)))
print(matriz3)

#-------------------------MATRIZ DIBUJO-----------------------------------------------

for row in range(cant_ubicaciones):
    print('VALOR DEL ROW ' +str(row))
    for col in range(cant_ubicaciones):
            print('#############')	
            print('columna '+str(col),'ROW '+str(row))
            print(col * BOX_SIZE + 5,row * BOX_SIZE + 3)
            print('-------')
            print(col * BOX_SIZE + BOX_SIZE + 5,row * BOX_SIZE + BOX_SIZE + 3)
            print('#############')
            matriz[col][row]=g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')

#-------------------------MATRIZ DIBUJO-----------------------------------------------


#-------------------------ECRIBIR PALABRA-----------------------------------------------

lista_coor_palabras=[]
for tipo in palabras.keys():
    l_palabras=palabras[tipo]
    for palabra in l_palabras:
        #input()
        insertada=False
        X=random.randint(0,tamaño_max)
        Y=random.randint(0,tamaño_max)
        while not insertada:
            print('LA RAW: '+str(X)+' LA COL: '+str (Y))
            if(configuracion['orientacion']== "HORIZONTAL"):
                while(cant_ubicaciones - Y < len(palabra)):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ 
                    print(''+str(cant_ubicaciones-Y))
                    print(Y- cant_ubicaciones < len(palabra))
                    Y-=1
                    #input()
            else:
                while(cant_ubicaciones - X < len(palabra)):#PARA QUE LA PALABRA NO SE IMPRIMA FUERA DEL RANGO DE LA MATRIZ 
                    print(''+str(cant_ubicaciones-X))
                    print(X- cant_ubicaciones < len(palabra))
                    X-=1
                    #input()
            if(configuracion['orientacion']== "HORIZONTAL"):
                            coor=(X,range(Y,Y+len(palabra)))
            else:
                            coor=(Y,range(X,X+len(palabra)))
                            
            if(configuracion['orientacion']== "HORIZONTAL"):
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,X)
                            print( palabras_en_la_linea(lista_coor_palabras,X))

            else:
                            hay_palabra=palabras_en_la_linea(lista_coor_palabras,Y)
                            print('HAY LINEA DIO:'+str(palabras_en_la_linea(lista_coor_palabras,Y)))
            if(not hay_palabra):
                    yI=Y
                    xI=X
                    for letra in palabra:
                        print('LUGAR DE IMPRESION = COL' +str(yI)+ '  ROW '+str(xI) )
                        g.DrawText(letra , (yI * BOX_SIZE + 18, xI * BOX_SIZE + 17),font='Bahnschrift 20')
                        matriz3[yI][xI]=colores[tipo]
                        if(configuracion['orientacion']== "HORIZONTAL"):
                            yI+=1
                        else:
                            xI+=1
                    lista_coor_palabras.append(coor)
                    insertada=True
            else:
                    print('ENTRE AL ELSE')
                    X=random.randint(0,tamaño_max)
                    Y=random.randint(0,tamaño_max)

#-----------------------LETRAS ALEATOREAS--------------------------------------------------------------

for row in range(cant_ubicaciones):
    for col in range(cant_ubicaciones):
        if(configuracion['orientacion']== "HORIZONTAL"):
                if(matriz3[col][row] == "white"):
                    g.DrawText(random.choice(string.ascii_uppercase) , (col * BOX_SIZE + 18, row * BOX_SIZE + 17),font='Bahnschrift 20')
        else:
            if(matriz3[row][col] == "white"):
                    g.DrawText(random.choice(string.ascii_uppercase) , (row * BOX_SIZE + 18, col * BOX_SIZE + 17),font='Bahnschrift 20')

#-------------------------ECRIBIR PALABRA-----------------------------------------------

#g.DrawText(random.choice(string.ascii_uppercase) , (col * BOX_SIZE + 18, row * BOX_SIZE + 17),font='Bahnschrift 20')

print(matriz)
print(matriz2)

while True:             # Event Loop
    try:
        event, values = window.Read()
        print(event, values)
        if event is None or event == 'Exit':
            break
        mouse = values['graph']

        if event == 'graph':
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
                if (matriz3[box_x][box_y]!='white'):
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill=matriz3[box_x][box_y])
                else:
                    g.TKCanvas.itemconfig(matriz[box_x][box_y], fill='#CFF5E3')
                matriz2[box_x][box_y] = True
                print(matriz2[box_x][box_y])
            else :
                g.TKCanvas.itemconfig(matriz[box_x][box_y], fill='white')
                matriz2[box_x][box_y] = False
                #print(g.TKFrame(matriz[box_x][box_y], fill_color))
        elif (event=="Controlar"):
             sg.Popup('TUS PALABRAS/LETRAS FALTANTES VAN A SER MARCADAS EN GRIS!')
             print(lista_coor_palabras)
             for cor in lista_coor_palabras:
                y=cor[0]
                for x in cor[1]:
                    if  not(matriz2[x][y]):
                        print('NO ESTA MARCADO')
                        if(configuracion['orientacion']== "HORIZONTAL"):
                            g.TKCanvas.itemconfig(matriz[x][y], fill='#C5C6C5')
                        else:
                            g.TKCanvas.itemconfig(matriz[y][x], fill='#C5C6C5')
                    else:
                        print('Esta marcado')
                
            #g.DrawRectangle((box_x * BOX_SIZE + 5, box_y * BOX_SIZE + 3),(box_x * BOX_SIZE + BOX_SIZE + 5, box_y * BOX_SIZE + BOX_SIZE + 3) ,fill_color='#CFF5E3', line_color='black')
    except(IndexError):
        continue
window.Close()
