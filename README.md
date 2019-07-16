 # Sopa de Letras en Python

_Este proyecto consiste en una simple aplicación destinada, principalmente, a niños que se encuentren cursando la etapa primaria del colegio. Ésta aplicación se trata de una sopa de letras en la que se pueden buscar palabras de acuerdo a su tipo gramatical (sustantivos,adjetivos,verbos) contando tambien con distintos tipos de ayudas que vayan ayudando a los participantes en el proceso del juego, como ser, las palabras mismas a buscar, o las definiciones de dichas palabras, en las que se profundizará mas adelante._ 

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Antes que nada, es ideal clonar el repositorio de este proyecto para poder ejectuar pruebas mas adelante:_
```
git clone https://github.com/augustodelg/TpFinalPython.git
```
_Para poder ejecutar dicha aplicación, es necesario contar con distintas herramientas que se irán explicando a continuación. Éstas herramientas son el intérprete de python3, junto con una librería y modulo externo (Pattern y PySimpleGUI),que nos ayudarán a obtener el tipo gramatical de una palabra, y por otro lado desarrollar la interfaz gràfica, respectivamente._

### Instalación 🔧

_En primera instancia, necesitamos contar con el intérprete de python3. Posiblemente nuestro equipo ya cuente con èl por defecto, pero de no ser así, podemos instalarlo con la siguiente instrucción en consola :_

```
sudo  apt install python3.7
```

_Ahora instalaremos el mòdulo PySimpleGUI. Antes, necesitaremos instalar la librería tkinter desde la pagina oficial: https://pypi.org/project/PySimpleGUI/ . Ahora si, instalamos el modulo deseado:_

```
sudo pip3 install PySimpleGUI
```
_Finalmente instalamos la librería Pattern:_
```
sudo pip3 install pattern
```
_Podríamos llegar a obtener un error asociado a mysql. Esto lo solucionaremos con dos lineas ejecutadas consecutivamente:_

```
sudo apt-get install mysql-server
```

```
sudo apt-get install libmysqlclient-dev
```

## Ejecutando las pruebas ⚙️

_Ejecutamos el archivo desde la consola, yendo a la carpeta donde se haya clonado el repositario. Cabe destacar que necesitaremos estar conectados a Internet, en el caso de que no juguemos con la opcion "Jugada Rapida"_

### Configuración  📌
_Una vez abierta la aplicaciòn, procederemos a realizar algunas pruebas sencillas. En primera instancia contamos con el boton "Jugada Rapida" que cuenta con una configuración por defecto para poder jugar(palabras,definiciones,colores de los tipos,etc).
Por otro lado, podemos jugar sin la necesidad de la opcion antes mencionada. Este proceso consiste en ir ingresando palabras que se iran chequendo vía online en "Wiktionary" y en "pattern.es", donde obtendremos su tipo gramatical junto con su definición del primero. Para hacer esto, basta con ingresar la palabra deseada debajo de "opciones de palabras" y pulsar "Agregar". A medida que se van validando las palabras, se van agregando en la seccion que se encuentra debajo.
Una vez que hayamos las palabras que deseamos, vamos hacia el lado derecho para configurar el color con el que se identificara posteriormente cada palabra (de acuerdo a su tipo). Ademas, podemos aclarar de antemano la cantidad de cada tipo con las que vamos a jugar. Finalmente, configuramos como deseamos que se encuentren orientadas las palabras (vertical u horizontal) y la fuente de la sopa.
Cabe destacar que hay dos botones mas, uno identificado con ("?") que nos da una pequeña guia para poder jugar, y otro llamado "Ver Reporte" que consiste en un archivo .json con las palabras con las que haya ocurrido algo en particular durante su validación web(ya sea que no se haya encontrado ni en wik ni en pattern, o que estos criterios hayan diferido en el tipo gramatical de la palabra. En este caso se reporta, y nos quedamos con lo dado por wik).
Ahora bien, con esto configurado, apretamos en el boton "JUGAR" donde tendremos una ventana nueva para jugar nuestra sopa de letras._

### Juego con la Sopa 🔩
_En este momento, es donde empieza el verdadero juego. El jugador debe ir clickeando en las letras que cree que van conformando alguna de las palabras buscadas. Estas se iran resaltando con el color elegido antes en configuración. 
En el lado derecho, vemos la cantidad de palabras que debemos buscar de cada tipo, y la cantidad de intentos que tenemos para verificar nuestro resultado. Es decir, cada vez que creemos haber terminado, apretamos en "Controlar", donde se verificará si lo que hicimos es correcto. Finalmente abajo a la derecha tenemos la ayuda quer hayamos elegido, o sea las definiciones de las palabras, o las mismas palabras a buscar._



## Construido con 🛠️

* Python 3.7- El lenguaje de programación utilizado.
* PySimpleGUI - Modulo para la interfaz grafica.
* Pattern - Libreria para la busqueda de tipos gramaticales y definiciones de las palabras.


## Autores ✒️


* **Del Grosso Augusto** - [augustodelg](https://github.com/augustodelg)
* **Velazquez Germán**  - [ger-velazquez](https://github.com/ger-velazquez)


