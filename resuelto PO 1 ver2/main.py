
from Menu import menuTerminal
from gestorClientes import gestorCliente
from gestorMovimiento import gestorMovimiento

#codigo funcionando sin problemas.
#Dudas con la opcion 1 del menu, el enunciado no dice nada que hacer con el anterior saldo.

if __name__=='__main__':
    menuApp = menuTerminal()
    menuApp.msjInicio('FarmaCuidad')
    #Gestores
    listaClientes = gestorCliente()
    listaClientes.extraerClientesCSV()
    #listaClientes.mostrarClientes()

    arregloMovimiento = gestorMovimiento()
    arregloMovimiento.extraerMovimientoCSV()
    arregloMovimiento.ordenarPorNumCuenta()
    #arregloMovimiento.mostrarMovimiento()

    menuApp.mostrarOpciones()
    rtaUsuario = menuApp.selecionarOpcion()

    while rtaUsuario != '0':
        if rtaUsuario == '1':
            dniCliente = int(menuApp.ingresarValor("DNI"))
            listaClientes.modificarImporteCliente(dniCliente, arregloMovimiento)
        elif rtaUsuario == '2':
            dniCliente = int(menuApp.ingresarValor("DNI"))
            # Sin tener arregloMovimiento ordenado.
            #listaClientes.buscarClientePorDNI(dniCliente, arregloMovimiento)

            # Con arregloMovimiento ordenado.
            listaClientes.buscarClientePorDNI(dniCliente, arregloMovimiento)
        elif rtaUsuario == '3':
            arregloMovimiento.ordenarPorNumCuenta()
            #Test ordenamiento
            arregloMovimiento.mostrarMovimiento()
        menuApp.mostrarOpciones()
        rtaUsuario = menuApp.selecionarOpcion()

    menuApp.msjFin()
