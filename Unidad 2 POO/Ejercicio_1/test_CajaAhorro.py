from claseCajaAhorro import cajaAhorro

class Test:
    def __init__(self):
        pass

    def crear_CajaAhorro(self):
        numeroCuenta = input(" Numero de Cuenta:  ")
        numCUIL = input(" CUIL:  ")
        apellido = input(" Apellido: ")
        nombre = input(" Nombre: ")
        saldo = float(input(" Saldo: "))

        caja1 = cajaAhorro(numeroCuenta,numCUIL,apellido,nombre,saldo)
        return caja1
    
    # def mostrar_CajaAhorro(self, cajaAhorro):
    #     print(" Los datos de la Caja de Ahorro son = ")
    #     print("   Numero Cuenta = ", cajaAhorro.getNumCuenta())
    #     print("   C.U.I.L = ", cajaAhorro.getCUIL())
    #     print("   Apellido = ", cajaAhorro.getApellido())
    #     print("   Nombre = ", cajaAhorro.getNombre())
    #     print("   Saldo = ", cajaAhorro.getSaldo())

    def mostrar_CajaAhorro(self, caja1):
        caja1.mostrarDatos()

    def extraccion(self, caja1):
        saldoDeseado = float(input(" Ingrese el saldo a extraer =  "))
        caja1.extraer(saldoDeseado)
    
    def deposito(self, caja1):
        depositoDeseado = float(input(" Ingrese el saldo a depositar =  "))
        caja1.depositar(depositoDeseado)
    
