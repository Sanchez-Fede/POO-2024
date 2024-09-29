
import rich
from claseNodo import Nodo
from clasePublicacion import publicacion
from claseLibroImpreso import libroImpreso
from claseCD import cd

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

    def agregarPublicacion(self, unaPublicacion: publicacion):
        unNodo = Nodo(unaPublicacion)
        unNodo.setNodoSiguiente(self.__comienzo)

        self.__comienzo = unNodo
        self.__actual = unNodo
        self.__indice += 1
        self.__tope += 1


    def insertarFinal(self, unaPublicacion : publicacion):
        nuevoNodo = Nodo(unaPublicacion)
        if self.__comienzo == None:
            self.__comienzo = Nodo(unaPublicacion)
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
            dato = nodoAux.getPublicacion()
            rich.print(dato)          
            nodoAux = nodoAux.getNodoSiguiente()

# ==== Procedimientos ===

    def crearLibroImpreso(self):
        titulo = input('   Titulo de la publicacion: ')
        categoria = input('   Categoria de la Publicacion: ')
        precioBase = float(input('   Precio Base de la publicacion: '))
        nombreAutor = input('   Nombre del Autor: ')
        fechaEdicion = input('   Fecha de Edicion: ')
        cantPagina = int(input('   Cantidad de Pagina: '))
        return libroImpreso(titulo, categoria, precioBase, nombreAutor, fechaEdicion, cantPagina)

    def crearCD(self):
        titulo = input('   Titulo de la publicacion: ')
        categoria = input('   Categoria de la Publicacion: ')
        precioBase = float(input('   Precio Base de la publicacion: '))
        duracion = int(input('   Duracion del CD: '))
        nombreNarrador = input('   Nombre del Narrador: ')
        return cd(titulo, categoria, precioBase, duracion, nombreNarrador)

# Punto 1
    def cargarPublicacion(self)->None:
        print("Carga de Publicaciones")
        print("----------------------")
        print(" [ 0 ] para terminar \n [ 1 ] para cargar Libro Impreso \n [ 2 ] para cargar CD")
        rtaUsuario = int(input("Ingrese una opcion: "))
        while rtaUsuario != 0:
            if rtaUsuario == 1:
                unLibroImpreso = self.crearLibroImpreso()
                # Con agregarPublicacion agrego por Cabeza los nodos.
                #self.agregarPublicacion(unCD)
                # Con insertarFinal agrego por la Cola los nodos.
                self.insertarFinal(unLibroImpreso)
            elif rtaUsuario == 2:
                unCD = self.crearCD()
                # Con agregarPublicacion agrego por Cabeza los nodos.
                #self.agregarPublicacion(unCD)
                # Con insertarFinal agrego por la Cola los nodos.
                self.insertarFinal(unCD)
            print(" [ 0 ] para terminar \n [ 1 ] para cargar Libro Impreso \n [ 2 ] para cargar CD")
            rtaUsuario = int(input("Ingrese una opcion: "))

# Punto 2
    def mostrarTipoPublicacion(self, posicionNodo : int)->None:
        i = 0
        nodoAux = self.__comienzo
        while nodoAux != None and i != posicionNodo:
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1

        if nodoAux != None:
            dato = nodoAux.getPublicacion()
            if isinstance(dato, libroImpreso):
                print("\n En la posicion {} se encuentra un Libro Impreso".format(posicionNodo))
            elif isinstance(dato, cd):
                print("\n En la posicion {} se encuentra un CD".format(posicionNodo))
        else:
            print("No se encontro la posicion solicitada")

# Punto 3
    def contarTipoPublicacion(self):
        contLibroImpreso = 0
        contCD = 0
        indice = 0
        nodoAux = self.__comienzo

        while nodoAux != None and indice < self.__tope:
            unaPublicacion = nodoAux.getPublicacion()
            if isinstance(unaPublicacion , libroImpreso):
                contLibroImpreso += 1
            elif isinstance(unaPublicacion , cd):
                contCD += 1
            nodoAux = nodoAux.getNodoSiguiente()
            indice += 1
        
        if indice == self.__tope:
            print("Cantidad de Libros Impresos: ", contLibroImpreso)
            print("Cantidad de CD: ", contCD)
        else:
            print("Error al contar las publicaciones")

#Punto 4
    def mostrarStock(self):
        nodoAux = self.__comienzo
        i = 0
        while nodoAux != None and i < self.__tope:
            unaPublicacion = nodoAux.getPublicacion()
            if isinstance(unaPublicacion, libroImpreso):
                importeLibro = unaPublicacion.importeLibroImpreso()
                #importeLibro = self.importeLibroImpreso(unaPublicacion.getPrecioBase(), unaPublicacion.getFechaEdicion())
                # Error float no es un objeto llamable.
                print(f'''Titulo: {unaPublicacion.getTitulo()} \n Categoria: {unaPublicacion.getCategoria()}''')
                print(f'''Importe: {importeLibro}''')
            elif isinstance(unaPublicacion, cd):
                importeCD = unaPublicacion.importeCD()
                #importeCD = self.importeCD(unaPublicacion.getPrecioBase())
                print(f'''Titulo: {unaPublicacion.getTitulo()} \n Categoria: {unaPublicacion.getCategoria()}''')
                print(f'''Importe: {importeCD}''')
            nodoAux = nodoAux.getNodoSiguiente()
            i += 1