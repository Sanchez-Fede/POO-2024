
class Departamento:

    __id: int
    __numPiso: int
    __propietario: str
    __numDepartamento: int
    __cantHabitaciones: int
    __cantBaños: int
    __superficieCubierta: float


    def __init__(
        self,
        id : int, propietario : str, numPiso : int,
        numDepartamento : int, cantHabitaciones : int,
        cantBaños : int, superficieCubierta: float
    ):
        self.__id = id
        self.__numPiso = numPiso
        self.__propietario = propietario
        self.__numDepartamento = numDepartamento
        self.__cantHabitaciones = cantHabitaciones
        self.__cantBaños = cantBaños
        self.__superficieCubierta = superficieCubierta

    def __del__(self):
        print("Borrando datos del Edificio:")
        del self.__suEdificio   

    def setEdificio(self, unEdificio : object):
        self.__suEdificio = unEdificio


    def getID(self):
        return self.__id


    def getPropietario(self):
        return self.__propietario


    def getNumPiso(self):
        return self.__numPiso


    def getNumDepartamento(self):
        return self.__numDepartamento

    
    def getCantHabitaciones(self):
        return self.__cantHabitaciones

    
    def getCantBaños(self):
        return self.__cantBaños

    
    def getSuperficieCubierta(self):
        return self.__superficieCubierta
