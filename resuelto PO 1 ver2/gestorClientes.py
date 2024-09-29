
import csv
from typing import List
from claseCliente import cliente
from gestorMovimiento import gestorMovimiento

class gestorCliente:
    __listaClientes : List[cliente]
    def __init__(self):
        self.__listaClientes = list()

    def insertarCliente(self, unCliente):
        self.__listaClientes.append(unCliente)

# Funciones =================================
    def extraerClientesCSV(self):
        NOMBRE, APELLIDO, DNI, NUMCUENTA, SALDOANTERIOR = 0,1,2,3,4
        with open("ClientesFarmaCiudad.csv", 'r', newline='') as archivoClientes:
            contenido = csv.reader(archivoClientes, delimiter = ';')
            archivoClientes.__next__()

            for fila in contenido:
                nombre = fila[NOMBRE]
                apellido = fila[APELLIDO]
                dni = int(fila[DNI])
                numCuenta = int(fila[NUMCUENTA])
                saldo = float(fila[SALDOANTERIOR])
                unCliente = cliente(nombre, apellido, dni, numCuenta, saldo)
                self.insertarCliente(unCliente)
        print("Carga completa de Clientes....")

    def mostrarClientes(self):
        for unCliente in self.__listaClientes:
            print(unCliente)

# inciso A
    def informarCliente(self, unApellido, unNombre, unNumCuenta, unSaldo):
        print(f''' Cliente: {unApellido} , {unNombre} \t Numero de cuenta: {unNumCuenta}''')
        print(f''' Saldo anterior: {unSaldo}''')

    def modificarImporteCliente(self, unDNI, gestorMovimiento : gestorMovimiento):
        i = 0
        tam = len(self.__listaClientes)
        while i < tam and self.__listaClientes[i].getDNI() != unDNI:
            i += 1
        
        if i < tam:
            print("Datos del cliente:")
            apellido = self.__listaClientes[i].getApellido()
            nombre = self.__listaClientes[i].getNombre()
            numCuenta = self.__listaClientes[i].getNumCuenta()
            saldo = self.__listaClientes[i].getSaldoAnterior()
            self.informarCliente(apellido, nombre, numCuenta, saldo)
            print("Movimientos:")
            gestorMovimiento.mostrarMovimientos(numCuenta)
            nuevoSaldo = gestorMovimiento.actualizarSaldo(numCuenta)
            self.__listaClientes[i].setSaldoAnterior(nuevoSaldo)
            print(f'''Nuevo saldo: {nuevoSaldo}''')
        else:
            print("Cliente no encontrado")

# inciso B
    def buscarClientePorDNI(self, unDNI : int, gestorMovimiento : gestorMovimiento):
        i = 0
        tam = len(self.__listaClientes)
        while i < tam and self.__listaClientes[i].getDNI() != unDNI:
            i += 1
        
        if i < tam:
            numCuenta = self.__listaClientes[i].getNumCuenta()
            gestorMovimiento.informarMovimientoCliente(numCuenta)
        else:
            print("DNI del cliente no encontrado")

