
# importo lo que necesito
import rich
from Menu import menuTerminal
from ListaEnlazada import listaEnlazada

if __name__=='__main__':
    menuApp = menuTerminal()
    menuApp.msjInicio()
    #Gestores
    listaAnuncio = listaEnlazada()
    listaAnuncio.cargarPlanesCSV()
    #Test
    #listaAnuncio.mostrarLista()

    menuApp.mostrarOpciones()
    rtaUsuario = menuApp.selecionarOpcion()

    while rtaUsuario != '0':
        if rtaUsuario == '1':
            tituloBuscar = menuApp.ingresarValor('Titulo del Anuncio')
            listaAnuncio.mostrarTipoPlan(tituloBuscar)
        elif rtaUsuario == '2':
            unaResolucionVideo= int(menuApp.ingresarValor('Resolucion Video'))
            listaAnuncio.mostrarTitulo_conResolucionX(unaResolucionVideo)
        elif rtaUsuario == '3':
            listaAnuncio.mostrarAnunciosConImporte()
        menuApp.mostrarOpciones()
        rtaUsuario = menuApp.selecionarOpcion()
    
    menuApp.msjFin()
    pass