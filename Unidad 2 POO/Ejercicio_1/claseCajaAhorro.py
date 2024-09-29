class cajaAhorro:
    def __init__(self, NumCuenta, cuil, apellido, nombre, saldo) -> None:
        self.__nroCuenta = NumCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = float(saldo)
    
    def getNumCuenta(self):
        return self.__nroCuenta
    
    def getCUIL(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSaldo(self):
        return self.__saldo
    
    # Esta funcion tambien esta funcionando bastante bien.
    # def mostrarDatos(self):
    #     print(" Numero Cuenta = ", self.__nroCuenta)
    #     print(" C.U.I.L = ", self.__cuil)
    #     print(" Apellido = ", self.__apellido)
    #     print(" Nombre = ", self.__nombre)
    #     print(" Saldo = ", self.__saldo)

    def mostrarDatos(self):
        print(" Numero Cuenta = ", self.getNumCuenta())
        print(" C.U.I.L = ", self.getCUIL())
        print(" Apellido = ", self.getApellido())
        print(" Nombre = ", self.getNombre())
        print(" Saldo = ", self.getSaldo())
    
    def extraer(self, importe):
        if (self.__saldo > importe):
            self.__saldo = self.__saldo - importe
            print("Extraccion realizada con exito")
            print("Saldo actualizado = ", self.__saldo)
        else:
            print("No hay saldo suficiente")
    
    def depositar(self, cant):
        if cant > 0:
            self.__saldo = self.__saldo + cant
        else:
            print(" Deposito Negativo. No se pudo depositar")
    
    def validarCUIL(self, unCUIL):
        pass