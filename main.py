#---------------------------------------Class-----------------------------------------
class Automata:
    #Variables locales
    nEstados=0              #Número de estados que tiene el autómata
    estados = []            #Lista de estados del autómata
    nFinales = 0            #Número de estados finales
    estadosFinales = []     #Lista de estados finales
    nCaracteres = 0         #Número de caracateres contenidos en el alfabeto
    caracteres = []         #Lista correspondiente al alfabeto del automata
    tabla = []              #Tabla de transiciones

    estadoActual = []       #Estado o estados en los que se encuentra el autómata


    def show_info(self):                #Muestrar la información del automata leido
        print(self.nEstados)
        print(self.estados)
        print(self.nFinales)
        print(self.estadosFinales)
        print(self.nCaracteres)
        print(self.caracteres)
        print("Tabla de Transiciones:")
        for i in range(int(self.nEstados)):
            print(self.tabla[i])

    def next_state(self,char,mark):          #Función que dado un caractar nos devuelve el estado siguiente del automata
        if(self.estadoActual.__contains__(" ")):
            for i in self.estadoActual:                             #Hay que valorar todos los posibles estados actuales en los que nos encontramos

                indexState = self.estados.index(i)              #Obtención del valor del indice del estado actual
                indexChar = self.caracteres.index(char)         #Obtención del valor del indice del caracter que se esta procesando

                nE = self.tabla[indexState][indexChar]          #Obtengo el siguiente valor dado
                nE = nE.split(" ")
                aux = []
                for index in nE:
                    if index != '':
                        aux.append(index)

            self.estadoActual = aux
        else:
            if mark == 0:
                indexState = self.estados.index(self.estadoActual)  # Obtención del valor del indice del estado actual
            else:
                indexState = self.estados.index(self.estadoActual[0])  # Obtención del valor del indice del estado actual

            indexChar = self.caracteres.index(char)                # Obtención del valor del indice del caracter que se esta procesando

            nE = self.tabla[indexState][indexChar]              # Obtengo el siguiente valor dado
            nE = nE.split(" ")
            aux = []
            for index in nE:
                if index != '':
                    aux.append(index)

            self.estadoActual = aux

    def process_word(self, word):       #Funcón que procesa la palabra que entra en el autómata
        self.estadoActual = self.estados[0]
        print(self.estadoActual, end=", ")
        mark = 0
        for x in word:
            if not self.caracteres.__contains__(x):     #Si alguno de los caracteres no pertenece al alfabeto se lanza un mensaje de error
                print("Alguno de los caracteres no pertenece al Alfabeto")
                break
            else:
                self.next_state(x,mark)
                mark+=1
                print(self.estadoActual, end=", ")

    def reset(self):
        self.estadoActual = self.estados[0]

#------------------------------------Fin Class-------------------------------------------



# Función encargada de leer el fichero y guardar las casteristicas del autómata
def read_file(Automata):
    fichero = open('definicionAutomata2.txt',"r")    #Apertura del fichero con la descripción del autómata
    lines = fichero.readlines()                 #Guardo las líneas del fichero en la variables lines

    aux = 0                                     #Variable para saber en que linea estoy leyendo
    for line in lines:                          #Recorro las lineas con la variables line
        line = line.replace('\n',"")            #Elimino todos los \n de las líneas
        if line[0]=='#':                    #Si la linea empieza por #
            x=line.split(' ')                #Separo por espacios

            for i in x:
               if (i[0]=='#' and aux == 0):     #primera línea, primer elemento --> nº estados
                   a=i.replace("#","")
                   automata.nEstados = a
               elif aux == 0:                   #Resto de elementos de la primera línea -->Estados
                   automata.estados.append(i)
               if (i[0]=='#' and aux == 1):     #segunda línea, primer elemento --> nº estados Finales
                   b=i.replace("#","")
                   automata.nFinales = b
               elif aux == 1:                   #Resto de elementos de la segunda línea -->Estados Finales
                   automata.estadosFinales.append(i)
               if (i[0]=='#' and aux == 2):     #tercera línea, primer elemento --> nº caracteres
                   c=i.replace("#","")
                   automata.nCaracteres = c
               elif aux == 2:                   #Resto de elementos de la tercera línea -->Caracteres
                   automata.caracteres.append(i)

            aux = aux + 1 #Siguiente línea


        elif (line[0]!='#' and line[0]!='-'):       #Parte de la tabla de transiciones
            x=line.split('#')                       #Separo por #
            for i in (automata.nCaracteres):
                del x[-1]                           #elimino el ultimo caracter ""
                automata.tabla.append(x)            #añado el elemento a la tabla

#----------------------------------------------Fin read_file----------------------------------------------------

# -------------------------------------------------Main---------------------------------------------------------
while(True):
    print("")
    print("______________________________________")
    print("| IMPLEMENTADOR DE AUTOMATAS FINITOS |")
    print("______________________________________")
    word = input("Palabra a procesar (o 'q' para salir): ")     #Palabra de prueba: 152ac22bd1c2c

    automata = Automata()  # Instacia de la clase autómata

    if word == "q":
        break
    else:
        read_file(automata)
        automata.show_info()           #Descomentar si se quiere ver la información del automata definido en el fichero
        automata.process_word(word)
        automata.reset()