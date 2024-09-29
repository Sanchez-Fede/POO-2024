
class nacimiento:

    __dniMadre : int
    __tipoParto : str
    __fecha : str
    __hora : str
    __peso : float
    __altura : float

    def __init__(self, dniMadre, tipoParto,  fecha, hora, peso, altura):
        self.__dniMadre = dniMadre
        self.__tipoParto = tipoParto
        self.__fecha = fecha
        self.__hora = hora
        self.__peso = peso
        self.__altura = altura

    def __str__(self):
        return f'''DNI Madre: {self.__dniMadre} Tipo de parto: {self.__tipoParto} Fecha: {self.__fecha} Hora: {self.__hora} Peso: {self.__peso} Altura: {self.__altura}'''

    def getDniMadre(self):
        return self.__dniMadre

    def getTipoParto(self):
        return self.__tipoParto

    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def __eq__(self, otroNacimiento) -> bool:
        return ((self.getDniMadre() == otroNacimiento.getDniMadre() ) and (self.getFecha() == otroNacimiento.getFecha()))

    def __lt__(self, otroNacimiento):
        if self.getDniMadre() == otroNacimiento.getDniMadre():
            return self.getFecha() < otroNacimiento.getFecha()
        else:
            return self.getDniMadre() > otroNacimiento.getDniMadre()
