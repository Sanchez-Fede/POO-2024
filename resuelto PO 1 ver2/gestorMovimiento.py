
import rich
import csv
import numpy as np
from claseMovimiento import movimiento

class gestorMovimiento:
    __ArregloMovimientos : np.ndarray
    __dimension : int
    __cantidad : int
    __incremento : int

    def __init__(self):
        self.__ArregloMovimientos = np.empty([0], dtype = movimiento)
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1

    def insertarDato(self, unMovimiento):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__ArregloMovimientos.resize(self.__dimension)
        
        self.__ArregloMovimientos[self.__cantidad] = unMovimiento
        self.__cantidad += 1

# Funciones ================================= 
    def extraerMovimientoCSV(self):
        NUMCUENTA, FECHA, DESCRIPCION, TIPOMOVIMIENTO, IMPORTE = 0,1,2,3,4
        with open("MovimientosAbril2024.csv", 'r', newline='') as archivoMovimientos:
            contenido = csv.reader(archivoMovimientos, delimiter = ';')
            archivoMovimientos.__next__()
        
            for fila in contenido:
                numCuenta = int(fila[NUMCUENTA])
                fecha = fila[FECHA]
                descripcion = fila[DESCRIPCION]
                tipoMovimiento = fila[TIPOMOVIMIENTO]
                importe = float(fila[IMPORTE])
                unMovimiento = movimiento(numCuenta, fecha, descripcion, tipoMovimiento, importe)  
                self.insertarDato(unMovimiento)
        print("Carga completa de Movimientos....")

    def mostrarMovimiento(self):
        for i in range(len(self.__ArregloMovimientos)):
            rich.print(self.__ArregloMovimientos[i])

# inciso A
    def contadorMovimiento(self, unNumCuenta : int, unTipo : str)->int:
        cont = 0
        for i in range(len(self.__ArregloMovimientos)):
            if self.__ArregloMovimientos[i].getTipoMovimiento() == unTipo and self.__ArregloMovimientos[i].getNumCuenta() == unNumCuenta:
                cont += self.__ArregloMovimientos[i].getImporte()
        return cont

    def mostrarMovimientos(self, unNumCuenta):
        for i in range(len(self.__ArregloMovimientos)):
            if self.__ArregloMovimientos[i].getNumCuenta() == unNumCuenta:
                fecha = self.__ArregloMovimientos[i].getFecha()
                descripcion = self.__ArregloMovimientos[i].getDescripcion()
                importe = self.__ArregloMovimientos[i].getImporte()
                print(f''' Fecha: {fecha} \t Descripcion: {descripcion} \t Importe: {importe}''')

    def actualizarSaldo(self, unNumCuenta):
        creditoTotal = self.contadorMovimiento(unNumCuenta, 'C')
        debitoTotal = self.contadorMovimiento(unNumCuenta, 'P')
        return (creditoTotal - debitoTotal)

# inciso B
    def buscarMovimiento(self, unNumCuenta, unTipo : str)->bool:
        i = 0
        tam = self.__cantidad
        bandEncontrado = False
        while i < tam and not bandEncontrado:
            if self.__ArregloMovimientos[i].getTipoMovimiento() == unTipo and self.__ArregloMovimientos[i].getNumCuenta() == unNumCuenta:
                bandEncontrado = True
            else:
                i += 1
        
        if i < tam:
            return bandEncontrado
        else:
            return False

    def informarMovimientoCliente(self, unNumCuenta):
        if self.buscarMovimiento(unNumCuenta, 'C') or self.buscarMovimiento(unNumCuenta, 'P'):
            print("El cliente posee movimientos")
        else:
            print("El cliente no posee movimientos")

# inciso C
    def ordenarPorNumCuenta(self):
        self.__ArregloMovimientos.sort()
        print("Movimientos ordenados por numero de cuenta") #menor a mayor

# incisos optimizados para el Arreglo Ordenado:
    def buscarMovimientoOptimizado(self, unNumCuenta, unTipo : str)->bool:
        #Busqueda Binaria
        minimo = 0
        maximo = self.__cantidad - 1
        bandEncontrado = False
        centro = (minimo + maximo) // 2
        while minimo <= maximo and not bandEncontrado:
            if self.__ArregloMovimientos[centro].getNumCuenta() == unNumCuenta and self.__ArregloMovimientos[centro].getTipoMovimiento() == unTipo:
                bandEncontrado = True
            else:
                if self.__ArregloMovimientos[centro].getNumCuenta() > unNumCuenta:
                    maximo = centro - 1
                else:
                    minimo = centro + 1
                centro = (minimo + maximo) // 2
        
        if bandEncontrado != False:
            return bandEncontrado
        else:
            return False

    def informarMovimientoClienteOptimizado(self, unNumCuenta):
        if self.buscarMovimientoOptimizado(unNumCuenta, 'C') or self.buscarMovimientoOptimizado(unNumCuenta, 'P'):
            print("El cliente posee movimientos")
        else:
            print("El cliente no posee movimientos")
