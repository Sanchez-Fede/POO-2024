
class materialReflectario:

    __material : int
    __caracteristica : any
    __cantUtilizada : float
    __costoAdicional : float

    def __init__(self, material : int, cantUtilizada : float, costoAdicional : float):
        self.__material = material
        self.__cantUtilizada = cantUtilizada
        self.__costoAdicional = costoAdicional

    def getMaterial(self):
        return self.__material

    def getCamtidadUtilizada(self):
        return self.__cantUtilizada

    def getCostoAdicional(self):
        return self.__costoAdicional

