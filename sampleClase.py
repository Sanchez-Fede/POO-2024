
class x:

    __x : int
    __y : float
    __z : str
    __k : object

    def __init__(self, xx, yy,  zz, kk):
        self.__x = xx
        self.__y = yy
        self.__z = zz
        self.__k = kk

    def __repr__(self):
        return f'''x: {self.__x} y: {self.__y} z: {self.__z} k: {self.__k}'''

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def k(self):
        return self.__k