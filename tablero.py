class Tablero:

    def __init__(self):
        self.__matrix = list()
        for i in [0, 1, 2]:
            row = list()
            for j in [0, 1, 2]:
                row.append("-")
            self.__matrix.append(row)

    @property
    def tablero(self):
        return self.__matrix.copy()

    def Print(self):
        for row in self.__matrix:
            for i in range(3):
                print("{}".format(row[i]), end=" ")
            print("\n")

    def Marcar(self, player, x, y):
        # buscar posicion
        if(self.__matrix[x][y] == '-'):
            self.__matrix[x][y] = player.marcador
        else:
            raise BusyPosition

class BusyPosition(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# class posicion:

#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#         self.__marca = "-"

#     def __str__(self):
#         return self.__marca