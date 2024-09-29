from typing import List

class menuTerminal:
    __listaOpciones : list
    def __init__(self):
        self.__listaOpciones = list(
            [
                "Terminar Programa",
                "Mostrar el tipo Plan en una posicion",
                "Mostrar la Cantidad de Planes con la misma cobertura",
                "Ingresar una cantidad y mostrar las compañias con la misma o mas cantidad de canales internacionales",
                "Mostrar planes con importe total"
            ]
        )

    def msjInicio(self):
        print("\t Bienvenido a Servicio de Plaes de Telecomunicaciones")
        print("Espere que se cargue los datos y muestre el menu...")

    def msjFin(self):
        print("\nFin del Programa. Gracias por utilizarlo, Hasta luego! :) ")

    def mostrarOpciones(self):
        print("\nLista de Opciones:")
        print("-------------------------\n")
        for i in range (len(self.__listaOpciones)):
            print("  [ {} ]  -  {}".format(i, self.__listaOpciones[i]))
        print("-------------------------")

    def selecionarOpcion(self)->str:
        rtaUsuario = input("Ingrese el numero de la opcion deseada: ")
        return rtaUsuario

    def ingresarValor(self, unTema):
        print("Ingrese el valor de {}".format(unTema))
        valor = input()
        return valor

# Test 
# if __name__=='__main__':

#     MenuApp = menuTerminal()
#     MenuApp.msjInicio()
#     MenuApp.mostrarOpciones()
#     rtaUsuario = MenuApp.selecionarOpcion()

#     while rtaUsuario != "0":
#         if rtaUsuario == "1":
#             print("Opcion A")
#         elif rtaUsuario == "2":
#             print("Opcion B")
#         MenuApp.mostrarOpciones()
#         rtaUsuario = MenuApp.selecionarOpcion()

#     MenuApp.msjFin()
#     pass