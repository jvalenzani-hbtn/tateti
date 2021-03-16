class Player:

    def __init__(self, nombre, color, marcador):
        self.__nombre = nombre
        self.__color = color
        self.__marcador = marcador
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def color(self):
        return self.__color

    @property
    def marcador(self):
        return self.__marcador
