
from gestorMadre import gestorMadre
from gestorNacimineto import gestorNacimiento
from Menu import menuTerminal

# Codigo fundionando 3/7/24

if __name__=='__main__':
    menuApp = menuTerminal()
    menuApp.msjInicio()
    #Gestores
    arregloMadre = gestorMadre()
    arregloMadre.extraerDatosCSV()
    #tet Carga
    #arregloMadre.mostrarDatosCSV()
    listaBebes = gestorNacimiento()
    listaBebes.extraerDatosCSV()
    #test Carga
    #listaBebes.mostrarDatosBebes()

    menuApp.mostrarOpciones()
    rtaUsuario = menuApp.selecionarOpcion()

    while rtaUsuario != '0':
        if rtaUsuario == '1':
            dniIngresado = int(menuApp.ingresarValor("DNI"))
            arregloMadre.mostrarMadreyBebe(dniIngresado, listaBebes)
        elif rtaUsuario == '2':
            listaBebes.ordenarPorDNI()
            arregloMadre.mostrarMadresVariosBebes(listaBebes)
        menuApp.mostrarOpciones()
        rtaUsuario = menuApp.selecionarOpcion()

    menuApp.msjFin()

# Nota: EL CSV de Mamas tiene los DNI sin repetir, en el CSV de Nacimientos estan los repetidos
# La funcion de la opcion 2, solo muestra dos madres por que solo hay dos madres tienen dos bebes. las otras tienen uno solo.