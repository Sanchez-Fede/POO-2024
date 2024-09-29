import csv
from claseMoto import Moto

class manejadorMotos:
    def __init__(self):
        self.__listaMotos = []
    
    def agregarMoto(self, moto):
        self.__listaMotos.append(moto)

    def getListaMotos(self):
        return self.__listaMotos

    def mostrarListaMotos(self):
        for unaMoto in self.__listaMotos:
            print(unaMoto)

# Punto 1: Cargar la lista de motos    
    def cargarListaMotos(self):
        with open('datosMotos.csv', 'r', newline='') as motosCSV:
            datosMotos = csv.reader(motosCSV, delimiter=';')
            for fila in datosMotos:
                patente = fila[0]
                marca = fila[1]
                nombreConductor = fila[2]
                apellidoConductor = fila[3]
                kilometraje = (fila[4])
                unaMoto = Moto(patente, marca, nombreConductor, apellidoConductor, kilometraje)
                self.__listaMotos.append(unaMoto)
        motosCSV.close()

# Parte del Punto 3: Ordenar lalista de pedidos y motos
    def ordenarPatente(self):
        self.__listaMotos.sort(key=lambda moto: moto.getPatente())

# Parte del Punto 3 y 4: Buscar una patente
    def buscarPatente(self, unaPatente):
        encontrado = False
        min = 0
        max = len(self.__listaMotos) - 1
        centro = (min + max) // 2

        while min <= max and not encontrado:
            if unaPatente == self.__listaMotos[centro].getPatente():
                encontrado = True
            else:
                if unaPatente < self.__listaMotos[centro].getPatente():
                    max = centro - 1
                else:
                    min = centro + 1
            centro = (min + max) // 2
        return encontrado

# Parte del Punto 4: modificar el Tiempo Real de una patente y con ID pedido
    def modificarTiempoReal(self, unaPatente, IDPedido, nuevotiempoReal):
        for unaMoto in self.__listaMotos:
            if unaMoto.getPatente() == IDPedido and unaMoto.getPatente() == unaPatente:
                unaMoto.setTiempoReal(nuevotiempoReal)

# Parte del Punto 5: Listar las motos
    def listadoMoto(self):
        pass