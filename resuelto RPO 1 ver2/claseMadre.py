
class madre:

    __DNI : int
    __edad : int
    __apellido : str
    __nombre : str

    def __init__(self, DNI, edad,  apellido, nombre):
        self.__DNI = DNI
        self.__edad = edad
        self.__apellido = apellido
        self.__nombre = nombre

    def __str__(self):
        return f'''DNI: {self.__DNI} Edad: {self.__edad} Apellido: {self.__apellido} Nombre: {self.__nombre}'''

    def getDNI(self):
        return self.__DNI

    def getEdad(self):
        return self.__edad

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre
