from claseCuentaBancaria import CuentaBancaria

class ManejadorCuentaBancaria:
    def __init__(self):
        self.__listaCuantaBancaria = []
    
    def crearCuentaBancaria(self):
        numCuenta = input(" Numero de Cuenta: ")
        cuil = input(" CUIL : ")
        apellido = input (" Apellido: ")
        nombre = input(" Nombre: ")
        saldo = float( input(" Saldo Total: "))
        
        cuentaBancaria = CuentaBancaria(numCuenta, cuil, apellido, nombre, saldo)
        return cuentaBancaria
    
    def cargaCuentasBancarias(self):
        cantObjetos = int( input("  Ingrese la cantidad de Cuenntas Bancarias a cargar: ") )
        
        for i in range (cantObjetos):
            nuevaCuentaBancaria = self.crearCuentaBancaria()
            self.__listaCuantaBancaria.append(nuevaCuentaBancaria)

    def obtenerDatos(self, unCUIL):
        banderaEncontrado = 0
        cantObjetos = len(self.__listaCuantaBancaria)
        
        while(( i <= cantObjetos) or (banderaEncontrado != 0)):
            
        pass