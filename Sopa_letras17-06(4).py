import PySimpleGUI as sg
import random
import string
import numpy as np

BOX_SIZE=25
matriz=[]#Matriz de nombres de las figuras
matriz2=[]#Matriz de si esta pintado o no
matriz3=[]#Matriz del color al cual tiene q cambiar esa cordenada al ser seleccionada

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
    for a in palabras:
        if len(a)>max:
            max=len(a)
    return max

def palabras_en_la_linea(coordenadas,x_o_y):
    for c in coordenadas:
        if c[0]== x_o_y:
            return True
    return False
#----------------------------CONFIGURACION---------------------------
config =  [ 
            [sg.Text('CONFIGURACION')],
			[sg.Text('QUE CONFIGURACION DE PALABRAS DESEA?')],
            [sg.InputCombo(['4 sustantivos, 3 verbos y 3 adjetivos','6 verbos, 3 sustantivos y 0 adjetivos'],key="con_palabras")],
            [sg.Text('ORIENTACION DE LAS PALABRAS:'), sg.InputCombo(['HORIZONTAL','VERTICAL'],key="orientacion")],
            [sg.Text('FORMA DE LETRAS'), sg.InputCombo(['MAYUSCULAS','MINUSCULAS'],key= "may_o_min")],
            [ sg.Submit(), sg.Cancel()]	,
			]
window2 = sg.Window('SOPA DE LETRAS').Layout(config)
event, configuracion = window2.Read()

# -------------------------------------------------------------------  


colores={'Sustantivos':"red",'Verbo':"green" ,'Adjetivos':"purple"}
cant_palabras={'Sustantivos':0,'Verbo':0 ,'Adjetivos':0}
palabras={'Sustantivos':["TOMATE","MINERVA","MANZANA"],'Verbo':["LAPUTAQLOPARIO"]}
tamaño_max=mayor_palabra(palabras)
print(tamaño_max)
cant_ubicaciones=int(tamaño_max)+4#tiene q serel canta de las palabras
print(cant_ubicaciones)
layout = [[sg.Graph(canvas_size=(cant_ubicaciones*38, cant_ubicaciones*38), graph_bottom_left=(0,cant_ubicaciones*26), graph_top_right=(cant_ubicaciones*26,0), change_submits=True, drag_submits=False,background_color='white', key='graph', tooltip='SELECCIONE LAS LETRAS QUE CONFORMAN LAS PALABRAS!!')],
        [sg.Button('Controlar')]]    

window = sg.Window('Graph of Sine Function', layout, grab_anywhere=True).Finalize()    
g = window.Element('graph')
#graph.DrawRectangle(top_left=[tamaño_max*-17,tamaño_max*30], bottom_right=[10,50], fill_color="white", line_color="black")

'''matriz=[[[0]] * tamaño_max for i in range(cant_ubicaciones)]
matriz2=[[[0]] * tamaño_max for i in range(cant_ubicaciones)]'''
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
            #g.DrawRectangle((box_x * BOX_SIZE + 5, box_y * BOX_SIZE + 3),(box_x * BOX_SIZE + BOX_SIZE + 5, box_y * BOX_SIZE + BOX_SIZE + 3) ,fill_color='#CFF5E3', line_color='black')
    except(IndexError):
        continue
window.Close()
