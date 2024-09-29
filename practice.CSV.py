
import csv
from claseCliente import Cliente

# Esta funcion tiene error en los indices de Fila
def cargar(listaCliente: list):
    with open("ClientesFarmaCiudad.csv", 'r', newline='') as archivoCliente:
            contenido = csv.reader(archivoCliente, delimiter = ';')
            archivoCliente.__next__()
            for fila in contenido:
                unCliente = Cliente(fila[0], fila[1], fila[2], fila[3], fila[4])
                listaCliente.append(unCliente)

# Si utilizo contenidoNuevo.writerow(NuevoCliente) se guardan asi:
#Cliente: Nombre: Federico Apellido: Sanchez DNI: 40779987 Numero de Cuenta: 2345 Saldo Anterior: 500
# Si lo utilizo: contenidoNuevo.writerow([nuevoCliente.getNombre(), nuevoCliente.getApellido(), nuevoCliente.getDNI(), nuevoCliente.getNumCuenta(), nuevoCliente.getSaldoAnterior()])
# Se guardan asi:
#Federico;Sanchez;40779987;2345;500

def ingresarValor():
    with open("ClientesFarmaCiudad.csv", 'a', newline='') as archivoCliente:
        contenidoNuevo = csv.writer(archivoCliente, delimiter = ';')
        nuevoCliente = Cliente("Federico","Sanchez", "40779987", 2345, 500)
        contenidoNuevo.writerow(
            [nuevoCliente.getNombre(), nuevoCliente.getApellido(), nuevoCliente.getDNI(), nuevoCliente.getNumCuenta(), nuevoCliente.getSaldoAnterior()]
        )

if __name__ == '__main__':
    listaCliente = []
    #cargar(listaCliente)
    ingresarValor()
    print("Fin del programa")