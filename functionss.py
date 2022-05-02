
import numpy as np
import random as rd

board = np.full((10,10),' ')

inventario = []

def first_coordinate(eslora):
    coordenada = (np.random.randint(0,10-eslora), np.random.randint(0,10-eslora))
    return coordenada


def orientation():
    orientation_list = ['h', 'v']
    orientations = np.random.choice(orientation_list)
    return orientations

def distancia(a, b):
    return (np.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2))

def check_position (inventario, barco):
    for i in inventario:
        for j in barco:
            if distancia(i,j) < 2:
                return True
    return False    

def ship (eslora, inventario):
    while True:
        barco = []
        s = first_coordinate(eslora)
        o = orientation()
        for i in range(eslora):
            if o == 'v':
                sx = s[0] + i
                sy = s[1]
                tupla_s = (sx, sy)
                barco.append(tupla_s)
            else:
                sx = s[0] 
                sy = s[1] + i
                tupla_s = (sx, sy)
                barco.append(tupla_s)
        if check_position(inventario, barco) == False:
            break
    
    return barco

def posicionar_barco (eslora, inventario,board):
    barco = ship(eslora, inventario)
    for i in barco:
        inventario.append(i)
        board[i] = 'O'
    return board

def posicionar_todos (numero_barcos, eslora, inventario, board):
    for i in range(numero_barcos):
        board = posicionar_barco(eslora, inventario, board)
    return board

posicionar_todos(4, 1, inventario, board)
posicionar_todos(3, 2, inventario, board)
print(posicionar_todos(2, 3, inventario, board))
print(posicionar_todos(1, 4, inventario, board))
