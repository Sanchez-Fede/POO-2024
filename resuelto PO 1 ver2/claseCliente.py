
class cliente:
    __nombre : str
    __apellido : str
    __DNI : int
    __numCuenta : int
    __saldoAnterior : float

    def __init__(self, nombre, apellido, DNI, numCuenta, saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__DNI = DNI
        self.__numCuenta = numCuenta
        self.__saldoAnterior = saldoAnterior

    def __str__(self):
        return f'''Nombre: {self.__nombre} Apellido: {self.__apellido} DNI: {self.__DNI} Numero de Cuenta: {self.__numCuenta} Saldo Anterior: {self.__saldoAnterior}'''

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getDNI(self):
        return self.__DNI

    def getNumCuenta(self):
        return self.__numCuenta

    def getSaldoAnterior(self):
        return self.__saldoAnterior
    
    def setSaldoAnterior(self, nuevoSaldo):
        self.__saldoAnterior = nuevoSaldo




