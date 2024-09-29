
# importo lo que necesito
from practicaListaEnlazada import listaEnlazada

#funciones test

def testInsertarAlFinal(listaEnlazada):
    rtaUsuario = input("Quieres agregar numeros: S/N: ")
    while rtaUsuario != 'N':
        unNumero = input("Numero: ")
        listaEnlazada.insertarFinal(unNumero)
        rtaUsuario = input("Quieres agregar numeros: S/N: ")

if __name__=='__main__':
    listaNodo = listaEnlazada()
    testInsertarAlFinal(listaNodo)
    listaNodo.mostrarLista()
    listaNodo.buscarNumero(5)
    print(list[3]) 
    pass