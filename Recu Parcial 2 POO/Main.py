
from Menu import menuTerminal
from gestorListaEnlazada import ListaEnlazada

# Tema 2
# Alumno Federico Gabriel Sanchez
# TPW = E014-53
# LCC = E010-192
# LSI = E009-100

if __name__=='__main__':

    MenuApp = menuTerminal()
    MenuApp.msjInicio()

    listaNodo = ListaEnlazada()
    listaNodo.cargarPlanesCSV()
    #listaNodo.mostrarLista()

    MenuApp.mostrarOpciones()
    rtaUsuario = MenuApp.selecionarOpcion()

    while rtaUsuario != "0":
        if rtaUsuario == "1":
            posicion = int(MenuApp.ingresarValor("posicionNodo"))
            listaNodo.mostrarTipoPlan(posicion)
        elif rtaUsuario == "2":
            cobertura = MenuApp.ingresarValor("Cobertura")
            listaNodo.mostrarCantidadCobertura(cobertura)
        elif rtaUsuario == "3":
            cantidad = int(MenuApp.ingresarValor("Cantidad de Canales"))
            listaNodo.buscarPlanesInternacionales(cantidad)
        elif rtaUsuario == "4":
            listaNodo.mostrarPlanesConImporte()
        
        MenuApp.mostrarOpciones()
        rtaUsuario = MenuApp.selecionarOpcion()
    MenuApp.msjFin()
    pass