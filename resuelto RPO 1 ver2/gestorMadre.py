
import csv
import rich
import numpy as np
from claseMadre import madre
from gestorNacimineto import gestorNacimiento

class gestorMadre:
    __ArregloMadre : np.ndarray
    __dimension : int
    __cantidad : int
    __incremento : int

    def __init__(self):
        self.__ArregloMadre = np.empty([0], dtype = madre)
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1

    def insertarDato(self, unaMadre):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__ArregloMadre.resize(self.__dimension)
        
        self.__ArregloMadre[self.__cantidad] = unaMadre
        self.__cantidad += 1

# Funciones =================================

    def extraerDatosCSV(self):
        DNI, EDAD, APELLIDOyNOMBRE = 0,1,2
        with open("mamas.csv", 'r', newline='') as archivoMadres:
            contenido = csv.reader(archivoMadres, delimiter = ';')
            archivoMadres.__next__()
    
            for fila in contenido:
                dni = int(fila[DNI])
                edad = fila[EDAD]
                apellidoynombre = fila[APELLIDOyNOMBRE]
                apellido, nombre = apellidoynombre.split(', ')
                unaMadre = madre(dni, edad, apellido, nombre)  
                self.insertarDato(unaMadre)
        print("Carga completa de Madres....")

    def mostrarDatosCSV(self):
        for i in range(len(self.__ArregloMadre)):
            rich.print(self.__ArregloMadre[i])

#Item a

    def datoPartoMadre(self, unApellido, unNombre, unaEdad, unParto):
        print("Datos de la madre: ")
        print(f'''Apellido , Nombre: {unApellido} , {unNombre}''')
        print(f'''Edad: {unaEdad}''')
        print(f'''Tipo de parto: {unParto}''')
        pass

    def mostrarMadreyBebe(self, unDNI, getorNacimiento : gestorNacimiento):
        i = 0
        cant = self.__cantidad
        bandEncontrado = False
        while i < cant and bandEncontrado != True:
            if unDNI == self.__ArregloMadre[i].getDNI():
                bandEncontrado = True
            else:
                i += 1
        
        if i < cant:
            #Cargando Datos Madre
            apellidoMadre = self.__ArregloMadre[i].getApellido()
            nombreMadre = self.__ArregloMadre[i].getNombre()
            edadMadre = self.__ArregloMadre[i].getEdad()
            suTipoParto = getorNacimiento.buscarPartoBebe(unDNI)
            #Cargando Datos Bebe
            self.datoPartoMadre(apellidoMadre, nombreMadre, edadMadre, suTipoParto)
            print("Bebe/s: ")
            getorNacimiento.mostrarHijos(unDNI)
        else:
            print("No se encontro el DNI ingresado")

#item b
    def mostrarMadresVariosBebes(self, gestorNacimiento : gestorNacimiento):
        for i in range(len(self.__ArregloMadre)):
            cantBebes = gestorNacimiento.contadorNacimientos(self.__ArregloMadre[i].getDNI())
            if cantBebes > 1:
                print(f'''Apellido: {self.__ArregloMadre[i].getApellido()} Nombre: {self.__ArregloMadre[i].getNombre()}''')
                print(f'''Tiene {cantBebes} hijos ''')



