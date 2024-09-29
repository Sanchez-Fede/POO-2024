from clasePedido import Pedido
from gestorMotos import manejadorMotos
import csv

class manejadorPedido:
    def __init__(self):
        self.__listaPedidos = []
    
    def agregarPedido(self, pedido):
        self.__listaPedidos.append(pedido)
    
    def getListaPedidtos(self):
        return self.__listaPedidos

    def mostrarListaPedidos(self):
        for pedido in self.__listaPedidos:
            print(pedido)

# Punto 2: Cargar la lista de pedidos
    def cargarListaPedidos(self):
        with open('datosPedidos.csv', 'r', newline='') as pedidosCSV:
            datosPedidos = csv.reader(pedidosCSV, delimiter=';')
            for fila in datosPedidos:
                PatenteMoto = fila[0]
                IDPedido = fila[1]
                ComidaPedida = fila[2]
                TiempoEstimado = int(fila[3])
                TiempoReal = int(fila[4])
                PrecioPedido = (fila[5])
                unPedido = Pedido(PatenteMoto, IDPedido, ComidaPedida, TiempoEstimado, TiempoReal, PrecioPedido)
                self.__listaPedidos.append(unPedido)
        pedidosCSV.close()

# Parte del Punto 3: Ordenar la lista de pedidos y motos
    def ordenarPedidos(self):
        self.__listaPedidos.sort(key=lambda pedido: pedido.getPatente())

# Punto 3: Agrear pedidos y buscar si existe la patente
    def agregarPedido(self):
        rta = 's'
        print("Telcee lo siguiente: ")

        while rta != 'n':
            patenteMoto = input("Patente Moto: ")
            while manejadorMotos.buscarPatente(patenteMoto) != True:
                print("La patente ingresada no existe en la lista de motos")
                print("Por favor, ingrese una patente valida ")
                patenteMoto = input("Patente Moto: ")
            
            if manejadorMotos.buscarPatente(patenteMoto) == True:
                print("La patente ingresada existe en la lista de motos ")

                IDPedido = input("ID Pedido: ")
                comidaPedida = input("Comida Pedida: ")
                tiempoEstimado = input("Tiempo Estimado: ")
                tiempoReal = input("Tiempo Real: ")
                precioPedido = input("Precio Pedido: ")
                unPedido = Pedido(patenteMoto, IDPedido, comidaPedida, tiempoEstimado, tiempoReal, precioPedido)
                self.__listaPedidos.append(unPedido)

            print("-------------------------------")
            rta = input("Desea agregar otro pedido? (s/n): ")

# Parte del Punto 4: Ingresar Patente, ID pedido, Tiempo Real y modificar el Tiempo Real de esa patente con el ID pedido
    def modificarTiempoReal(self):
        patenteMoto = input("Ingrese la patente de la moto: ")
        
        while manejadorMotos.buscarPatente(patenteMoto) != True:
            print("La patente ingresada no existe en la lista de motos")
            print("Por favor, ingrese una patente valida ")
            patenteMoto = input("Patente Moto: ")

        if manejadorMotos.buscarPatente(patenteMoto) == True:
            print("La Patente de la Moto se encontro. ingrese lo siguiente: ")
            IDPedido = input("Ingrese el ID del pedido: ")
            tiempoReal = input("Ingrese el tiempo real: ")
            manejadorMotos.modificarTiempoReal(IDPedido, tiempoReal)
    
# Parte del Punto 5: Listar los pedidos
    # def mostrarDatos(self, unPedido, unaMoto):
    #     print("Patente de Moto: \n", unPedido.getPatente())
    #     print("Conductor: {} , {} \n", unaMoto.getNombreConductor(), unaMoto.getApellidoConductor())
    #     print("Identificador de Pedido: {}\t Tiempo Estimado: {}\t Tiempo Real: {}\t Precio: {}\n",
    #         unPedido.getIDPedido(), unPedido.getTiempoEstimado(), unPedido.getTiempoReal(), unPedido.getPrecioPedido())
    #     print("-------------------------------")
    #     print("Total: {}")
        
    # def generarListado(self):
    #     listaMotos = manejadorMotos.getListaMotos()
    #     for unaMoto in listaMotos:
    #         for unPedido in self.__listaPedidos:
    #             self.mostrarDatos(unPedido, unaMoto)
    #         print("-------------------------------")
    #         print("Total: {}")