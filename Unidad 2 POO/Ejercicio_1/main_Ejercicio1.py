
from claseCajaAhorro import cajaAhorro
from test_CajaAhorro import Test

if __name__ == '__main__':

    caja1 = Test().crear_CajaAhorro()

    Test().mostrar_CajaAhorro(caja1)

    Test().extraccion(caja1)
    Test().mostrar_CajaAhorro(caja1)

    Test().deposito(caja1)
    Test().mostrar_CajaAhorro(caja1)

    pass

