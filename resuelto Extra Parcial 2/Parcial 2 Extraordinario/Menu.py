from typing import List

class menuTerminal:
    __listaOpciones : list
    def __init__(self):
        self.__listaOpciones = list(
            [
                "Terminar Programa",
                "Mostrar Formato, Tipo de Audio de un Titulo",
                "Mostrar Titulos con la misma Resolucion",
                "Mostrar todos los Planes, su Duracion y Costo Total"
            ]
        )

    def msjInicio(self):
        print("\t Bienvenido a Gestion De Anuncios")
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