import json
from claseJugador import Jugador
class GestorJugadores:
    def __init__(self):
        self.__jugadores = []
    
    def agregarJugador(self, jugador):
        self.__jugadores.append(jugador)


    def cargarJugadores(self):
        with open("pysimonpuntajes.json", "r", encoding='utf-8-sig') as jsonJugadores:
            data = json.load(jsonJugadores)
            for unJugador in data['jugadores']:
                self.agregarJugador(Jugador(unJugador['jugador'],unJugador['fecha'], unJugador['hora'], unJugador['puntaje']))
        jsonJugadores.close()

    def __str__(self):
        s = ''
        for jug in self.__jugadores:
            s += str(jug) + '\n'
        return s
    
    def get_jugadores(self):
        return self.__jugadores
    
    def toJson(self):
        d = dict(
            __class__=self.__class__.__name__,
            jugadores = [jug.toJson() for jug in self.__jugadores]
        )
        return d

    def guardarJSONArchivo(self, dic):
        
        with open('pysimonpuntajes.json', 'w') as jsonJugador:
            json.dump(dic, jsonJugador, indent=4)
        jsonJugador.close()