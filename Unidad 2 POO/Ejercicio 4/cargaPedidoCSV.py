import csv

if __name__ == '__main__':
    # Carga informacion de Pedidos en datosPedidos.csv
    print("Carga de Informacion de Pedidos")
    print("-------------------------------")
    print("Teclee lo siguiente:")

    with open('datosPedidos.csv', 'a', newline='') as pedidosCSV:
        datosPedidos = csv.writer(pedidosCSV, delimiter=';')
        rta = 's'
        while rta != 'n':
            patenteMoto = input("Patente Moto: ")
            IDPedido = input("ID Pedido: ")
            comidaPedida = input("Comida Pedida: ")
            tiempoEstimado = input("Tiempo Estimado: ")
            tiempoReal = input("Tiempo Real: ")
            precioPedido = input("Precio Pedido: ")
            datosPedidos.writerow([patenteMoto, IDPedido, comidaPedida, tiempoEstimado, tiempoReal, precioPedido])
            print("-------------------------------")
            rta = input("Desea agregar otra moto? (s/n): ")

    print("Finalizo con exito la carga de motos")
    print("-----------------------------------")

    pedidosCSV.close()
    print("Se almacenaron los datos de las motos en datosMotos.csv")
    print("Fin del programa")
