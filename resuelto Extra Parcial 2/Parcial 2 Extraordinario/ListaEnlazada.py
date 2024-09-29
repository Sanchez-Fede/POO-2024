
import csv
import rich
from claseAnuncio import anuncio
from claseAudio import audio
from claseAudioVisual import audioVisual
from claseNodo import Nodo

class listaEnlazada:

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
        if self.__inice == self.__tope:
            self.__actual = self.__comienzo
            self.__inice = 0
            raise StopIteration
        else:
            self.__inice += 1
            dato = self.__actual.getAnuncio()
            self.__actual = self.__actual.getNodoSiguiente()
            return dato

    #def agregarNodo(self, unaPublicacion: publicacion):
    #      unNodo = Nodo(objeto)
    #      unNodo.setNodoSiguiente(self.__comienzo)
    #      self.__comienzo = unNodo
    #      self.__actual = unNodo
    #      self.__tope += 1

# Procesamiento:

    def insertarFinal(self, unAnuncio : anuncio):
        nuevoNodo = Nodo(unAnuncio)
        if self.__comienzo == None:
            self.__comienzo = Nodo(unAnuncio)
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
            dato = nodoAux.getAnuncio()    
            rich.print(dato)    
            nodoAux = nodoAux.getNodoSiguiente()

    def cargarPlanesCSV(self):
        with open("anuncios.csv", 'r', newline='') as archivoAnuncios:
            contenido = csv.reader(archivoAnuncios, delimiter = ';')
            archivoAnuncios.__next__()
            for fila in contenido:
                if fila[0] == 'AA':
                    unAudio = audio(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], fila[6])
                    self.insertarFinal(unAudio)
                elif fila[0] == 'AV':
                    unAudioVisual = audioVisual(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6]))
                    self.insertarFinal(unAudioVisual)
            print("Carga Completa....")

    def mostrarTipoPlan(self, unTitulo : str):
        i = 0
        nodoAux = self.__comienzo
        while nodoAux != None and i < self.__tope:
            dato = nodoAux.getAnuncio()
            if dato.getTitulo() == unTitulo:
                if isinstance(dato, audio):
                    print(f'''\n Anuncio de Audio: \n Titulo: {dato.getTitulo()} Formato {dato.getFormato()} Tipo de Canal {dato.getCanalAudio()}''')
                elif isinstance(dato, audioVisual):
                    print(f'''\n Anuncio AudioVisual: \n Titulo: {dato.getTitulo()} Formato {dato.getFormato()} Resolucion {dato.getResolucionVideo()}''')
            nodoAux = nodoAux.getNodoSiguiente()

    def mostrarTitulo_conResolucionX(self, unaCantidad : int):
        nodoAux = self.__comienzo
        i = 0
        while nodoAux != None and i < self.__tope:
            unAnuncio = nodoAux.getAnuncio()
            if isinstance(unAnuncio, audioVisual):
                if unAnuncio.getResolucionVideo() == unaCantidad:
                    print(f''' Titulo: {unAnuncio.getTitulo()} tiene la misma Resolucion.''')
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1

    def mostrarAnunciosConImporte(self):
        i = 0
        nodoAux = self.__comienzo
        while nodoAux != None and i < self.__tope:
            unAnuncio = nodoAux.getAnuncio()
            nombre = unAnuncio.getTitulo()
            duracion = unAnuncio.getDuracion()
            importe = unAnuncio.calcularImporteTotal()
            print(f'''Nombre Compañia: {nombre}\n Duracion Plan: {duracion} \n Importe Total: {importe}''')
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1