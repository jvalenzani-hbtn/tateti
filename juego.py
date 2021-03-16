from tablero import Tablero, BusyPosition
from player import Player

t = Tablero()
p1 = Player("Betty", "RED", "B")
p2 = Player("Julien", "BLUE", "F")

def main():

    win = False
    while(not win):
        # p1.Juega(tablero, x, y)
        jugadaX = input("Ingrese X: ")
        jugadaY = input("Ingrese Y: ")
        try:
            t.Marcar(p1, int(jugadaX), int(jugadaY))
        except BusyPosition:
            print("Ya jugaste ahi pibe")
        t.Print()
        win = CheckWin(t)

def CheckWin(t):
    win = False
    # Check Filas
    for fila in t.tablero:
        marca = fila[0]
        checks = 1
        if (marca != "-"):
            for i in range(1, 3):
                if(fila[i] == marca):
                    print(fila[i])
                    checks += 1
                    print(checks)
                else:
                    break
        if(checks >= 3):
            print("WIN!!")
            win = True
    # Check Columnas
    for columna in range(3):
        checks = 1
        marca = t.tablero[0][columna]
        if (marca != "-"):
            for fila in range(1,3):
                if(t.tablero[fila][columna] == marca):
                    print(t.tablero[fila][columna])
                    checks += 1
                    print(checks)
                else:
                    break
            if(checks >= 3):
                print("WIN!!")
                win = True            
    # Check Diagonales
    # Diagonal izq-arriba
    marca = t.tablero[1][1]
    checks = 1 
    for x,y in [(0,0), (2,2)]:     
        if (marca != "-"):
            if(t.tablero[x][y] == marca):
                print(t.tablero[x][y])
                checks += 1
                print(checks)
            else:
                break
            if(checks >= 3):
                print("WIN!!")
                win = True
    checks = 1            
    for x,y in [(0,2), (2,0)]:      
        if (marca != "-"):
            if(t.tablero[x][y] == marca):
                print(t.tablero[x][y])
                checks += 1
                print(checks)
            else:
                break
            if(checks >= 3):
                print("WIN!!")
                win = True                 
    return win

main()