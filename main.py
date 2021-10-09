#---------------------------------------Class-----------------------------------------
class Automata:
    #Variables locales
    nEstados=0
    estados = []
    nFinales = 0
    estadosFinales = []
    nCaracteres = 0
    caracteres = []
    tabla = []

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
#------------------------------------Fin Class-------------------------------------------



# Función encargada de leer el fichero y guardar las casteristicas del autómata
def read_file(Automata):
    fichero = open('definicionAutomata.txt',"r")    #Apertura del fichero con la descripción del autómata
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
    word = input("Palabra a procesar (o 'q' para salir): ")

    automata = Automata()  # Instacia de la clase autómata

    if word == "QUIT":
        break
    else:
        read_file(automata)
        automata.show_info()