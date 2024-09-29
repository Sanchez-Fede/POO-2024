
import rich
import csv
from claseNodo import Nodo
from clasePlanes import planes
from clasePlanTelefonia import planTelefonia
from clasePlanTelevision import planTelevision

class ListaEnlazada:

    __comienzo : Nodo
    __actual : Nodo
    __indice : int
    __tope : int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getPublicacion()
            self.__actual = self.__actual.getNodoSiguiente()
            return dato

    def getTope(self):
        return self.__tope

    def insertarFinal(self, unPlan : planes):
        nuevoNodo = Nodo(unPlan)
        if self.__comienzo == None:
            self.__comienzo = Nodo(unPlan)
            self.__tope += 1
        else:
            nodoAux = self.__comienzo
            while nodoAux.getNodoSiguiente() != None:
                nodoAux = nodoAux.getNodoSiguiente()
            nodoAux.setNodoSiguiente(nuevoNodo)
            self.__tope += 1


    def mostrarLista(self):
        nodoAux = self.__comienzo
        while nodoAux != None:
            dato = nodoAux.getPlan()    
            rich.print(dato)    
            nodoAux = nodoAux.getNodoSiguiente()

# ==== Procedimientos ===

    def cargarPlanesCSV(self):
        with open("planes.csv", 'r', newline='') as archivoPlanes:
            contenido = csv.reader(archivoPlanes, delimiter = ';')
            archivoPlanes.__next__()
            for fila in contenido:
                if fila[0] == 'T':
                    unaTelevision = planTelevision(fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]), int(fila[6]))
                    self.insertarFinal(unaTelevision)
                elif fila[0] == 'M':
                    unaTelefonia = planTelefonia(fila[1], fila[2], fila[3], float(fila[4]), fila[5], int(fila[6]))
                self.insertarFinal(unaTelefonia)
            print("Carga Completa....")

    def mostrarCantidadCobertura(self, coberturaUsuario : str):
        nodoAux = self.__comienzo
        i = 0
        contCoberturaTelefonia = 0
        contCoberturaTelevision = 0
        while nodoAux != None and i < self.__tope:
            unPlan = nodoAux.getPlan()
            unaCobertura = unPlan.getCoberturaGeografica()
            if isinstance(unPlan, planTelefonia) and unaCobertura == coberturaUsuario:
                contCoberturaTelefonia += 1
            elif isinstance(unPlan, planTelevision) and unaCobertura == coberturaUsuario:
                contCoberturaTelevision += 1
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1
        if i == self.__tope:
            print("Cantidad de planes de telefonia con cobertura {}: {}".format(coberturaUsuario, contCoberturaTelefonia))
            print("Cantidad de planes de television con cobertura {}: {}".format(coberturaUsuario, contCoberturaTelevision))
        else:
            print(" No hay planes para esa cobertura")

    def mostrarTipoPlan(self, posicionNodo : int)->None:
        try:
            posicionNodo = posicionNodo - 1
            if posicionNodo < 0 or posicionNodo > self.__tope:
                raise IndexError
        except IndexError:
            print("Posicion incorecta")
        else:
            i = 0
            nodoAux = self.__comienzo
            while nodoAux != None and i != posicionNodo:
                nodoAux = nodoAux.getNodoSiguiente()
                planEncontrado = nodoAux.getPlan()
                i += 1
            if nodoAux != None:
                if isinstance(planEncontrado, planTelefonia):
                    print("\n En la posicion {} se encuentra un Plan Telefonia".format(posicionNodo + 1))
                elif isinstance(planEncontrado, planTelevision):
                    print("\n En la posicion {} se encuentra un Plan Television".format(posicionNodo + 1))
        finally:
            print("Proceso Terminado")

    def buscarPlanesInternacionales(self, unaCantidad : int):
        nodoAux = self.__comienzo
        i = 0
        while nodoAux != None and i < self.__tope:
            unPlan = nodoAux.getPlan()
            if isinstance(unPlan, planTelevision):
                if unPlan.getCantCanalesInternacionales() == unaCantidad:
                    print(f'''La compañia : {unPlan.getNombreCompañia()} tiene la misma cantidad de canales internacionales.''')
                elif unPlan.getCantCanalesNacionales() > unaCantidad:
                    print(f'''La compañia : {unPlan.getNombreCompañia()} tiene mas canales internacionales''')
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1

    def calcularPorcentaje(self, unPrecio : float, unPorcentaje ):
        float(unPorcentaje)
        porcentaje = (unPrecio * unPorcentaje) / 100
        return porcentaje

    def mostrarPlanesConImporte(self):
        i = 0
        nodoAux = self.__comienzo
        while nodoAux != None and i < self.__tope:
            unPlan = nodoAux.getPlan()
            nombre = unPlan.getNombreCompañia()
            duracion = unPlan.getDuracionPlan()
            cobertura = unPlan.getCoberturaGeografica()
            importe = unPlan.calcularImporteTotal()
            print(f'''Nombre Compañia: {nombre}\n Duracion Plan: {duracion} \n Cobertura Geografica: {cobertura} \n Importe Total: {importe}''')
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1