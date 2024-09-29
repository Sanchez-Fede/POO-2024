
class movimiento:
    __numCuenta : int
    __fecha : str
    __descripcion : str
    __tipoMovimiento : str
    __importe : float

    def __init__(self, numCuenta, fecha, descripcion, tipoMovimiento, importe):
        self.__numCuenta = numCuenta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMovimiento = tipoMovimiento
        self.__importe = importe

    def __str__(self):
        return f'''Numero de Cuenta: {self.__numCuenta} Fecha: {self.__fecha} Descripcion: {self.__descripcion} Tipo de Movimiento: {self.__tipoMovimiento} Importe: {self.__importe}'''

    def getNumCuenta(self):
        return self.__numCuenta

    def getFecha(self):
        return self.__fecha

    def getDescripcion(self):
        return self.__descripcion

    def getTipoMovimiento(self):
        return self.__tipoMovimiento

    def getImporte(self):
        return self.__importe

    def __lt__(self, otroMovimiento):
        return self.__numCuenta < otroMovimiento.getNumCuenta()

    def __eq__(self, otroMovimiento):
        return self.__numCuenta == otroMovimiento.getNumCuenta()


