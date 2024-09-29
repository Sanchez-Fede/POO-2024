import csv

if __name__=='__main__':
    # Carga informacion de Motos en datosMotos.csv
    print("Carga de Informacion de Motos")
    print("-------------------------------")
    print("Teclee lo siguiente:")


    with open('datosMotos.csv', 'a', newline='') as motosCSV:
        datosMotos = csv.writer(motosCSV, delimiter=';')    
        rta = 's'
        while rta != 'n':
            patenteMoto = input("Patente: ")
            marcaMoto = input("Marca: ")
            nombreConductor = input("Nombre: ")
            apellidoConductor = input("Apellido: ")
            kilometraje = input("Kilometraje: ")
            datosMotos.writerow([patenteMoto, marcaMoto, nombreConductor, apellidoConductor, kilometraje])
            print("-------------------------------")
            rta = input("Desea agregar otra moto? (s/n): ")
    
    print("-------------------------------")
    print("Finalizo con exito la carga de motos")

    motosCSV.close()

print("Se almacenaron los datos de las motos en datosMotos.csv")
print("Fin del programa")