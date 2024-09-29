class Moto:
    def __init__(self, patente, marca, nombreConductor, apellidoConductor,kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombreConductor = nombreConductor
        self.__apellidoConductor = apellidoConductor
        self.__kilometraje = int(kilometraje)


    def getPantente(self):
        return self.__patente
    
    def getMarca(self):
        return self.__marca
    
    def getNombreConductor(self):
        return self.__nombreConductor
    
    def getApellidoConductor(self):
        return self.__apellidoConductor
    
    def getKilometraje(self):
        return self.__kilometraje
    
    def setTiempoReal(self, unTiempoReal):
        if unTiempoReal > 0:
            self.__tiempoReal = unTiempoReal