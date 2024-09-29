class Pedido:
    def __init__(self, PatenteMoto, IDPedido, ComidaPedida, TiempoEstimado, TiempoReal, PrecioPedido):
        self.__PatenteMoto = PatenteMoto
        self.__IDPedido = IDPedido
        self.__ComidaPedida = ComidaPedida
        self.__TiempoEstimado = TiempoEstimado
        self.__TiempoReal = 0
        self.__PrecioPedido = float(PrecioPedido)
    
    def getPatenteMoto(self):
        return self.__PatenteMoto
    
    def getIDPedido(self):
        return self.__IDPedido
    
    def getComidaPedida(self):
        return self.__ComidaPedida
    
    def getTiempoEstimado(self):
        return self.__TiempoEstimado
    
    def getTiempoReal(self):
        return self.__TiempoReal
    
    def getPrecioPedido(self):
        return self.__PrecioPedido

