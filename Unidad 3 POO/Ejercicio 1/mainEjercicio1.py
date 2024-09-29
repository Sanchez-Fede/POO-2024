
# Ejercicio 1 - Unidad 3 - POO
from claseMenu import menuTerminal
from gestorEdificio import gestorEdificio

if __name__=='__main__':
    MenuApp = menuTerminal()
    MenuApp.msjInicio()

    listaEdifcio = gestorEdificio()
    listaEdifcio.extraerEdificioCSV()
    #Test 1: Funciona correctamente la carga de datos
    #listaEdifcio.mostrarListaEdificios()

    MenuApp.mostrarOpciones()
    rtaUsuario = MenuApp.selecionarOpcion()

    while rtaUsuario != '0':
        if rtaUsuario == '1':
            edificioUsuario = MenuApp.ingresar("Nombre del Edificio")
            listaEdifcio.buscarPropietario(edificioUsuario)
        
        elif rtaUsuario == '2':
            print("Opcion B")
        MenuApp.mostrarOpciones()
        rtaUsuario = MenuApp.selecionarOpcion()

    pass