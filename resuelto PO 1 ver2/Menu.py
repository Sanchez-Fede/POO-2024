
from typing import List

class menuTerminal:
    __listaOpciones : list
    def __init__(self):
        self.__listaOpciones = list(
            [
                "Terminar Programa",
                "Actualizar saldo de un cliente",
                "Mostrar movimientos de un cliente",
                "Test de Ordenamiento del Arreglo de Movimientos"
            ]
        )

    def msjInicio(self, tema:str):
        print("\t Bienvenido a {}".format(tema))
        print("Espere que se cargue los datos y muestre el menu...")

    def msjFin(self):
        print("\tFin del Programa... ")
        print(" Desarrollado por Federico Sanchez \n Gracias por utilizarlo! :)")

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