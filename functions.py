import numpy as np #importamos las librerias de numpy y random
import random as rd
import variables as v

board = np.full((11,11),' ') #Creamos un tablero generico con espacios vacios

inventario = [] #Creamos un inventario que será una lista vacia en la que incluiremos las posiciones de nuestros barcos


def first_coordinate(naves, tipo_nave): 
    """
    la funcion first_coordinate es una generadora aleatoria de coordenadas X e Y de los barcos,
     toma como variable "eslora" que es el tamaño de los barcos. Devuelve una coordenada aleatoria
    """
    coordenada = (np.random.randint(1,11 - naves[tipo_nave][1]), np.random.randint(1,11-naves[tipo_nave][1])) #El tamaño de los barcos se resta al valor máximo que puede tomar el valor aleatorio de X e Y esto es para evitar que las coordenadas se salgan del tablero
    return coordenada


def orientation():
    """
     La funcion orientation genera un valor aleatorio de la lista orientation_list la cual contiene v o h que es la orientación vertical u horizontal de las naves

    """
    orientation_list = ['h', 'v']
    orientations = np.random.choice(orientation_list)
    return orientations


def distancia(a, b):
    """
    La funcion distancia es la distancia que hay entre dos coordenadas generadas aleatoriamente 
    """
    return (np.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2))



def check_position (inventario, barco):
    """
    La funcion check position toma las variables inventario definida anteriormente y la variable
    barco que se apendizará a la lista posteriormente. Esta funcion devuelve True si la distancia entre la coordenada generada aletoriamente y
    las que estan en la lista inventario son validas, si no es así devuelve True
    """
    for i in inventario:
        for j in barco:
            if distancia(i,j) < 2:
                return True
    return False    

def ship (naves, tipo_nave, inventario):
    """
    La funcion ship genera las coordenadas de una nave de una eslora determinada con una orientacion y coordenadas iniciales aleatorias.
    Además, comprueba mediante la función check_position si cada una de las coordenadas de la nave es valida de tal forma que si lo es apendiza esa coordenada a la lista barco y
    si no el bucle while genera otra coordenada consecutiva horizontal o verticalmente con la anterior.
    La funcion devuelve la lista barco con el numero de coordenadas igual a la eslora correspondiente.
    """
    while True:
        barco = []
        s = first_coordinate(naves, tipo_nave)
        o = orientation()
        for i in range(naves[tipo_nave][1]):
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

def posicionar_barco (naves, tipo_nave, inventario,board):
    """
    La funcion posicionar barco genera un barco a partir de la funcion ship definida anteriormente. Luego itera a través de cada una de las coordenadas del barco y
    las apendiza al invetario, para que pueda ser utilizada en la funcion check position. Finalmente posiciona un string 'O' en el tablero definida al principio del script.
    La funcion devuelve el tablero con la nave posicionada
    """
    barco = ship(naves, tipo_nave, inventario)
    for i in barco:
        inventario.append(i)
        board[i] = 'O'
    return board

def posicionar_todos (naves,tipo_nave, inventario, board):
    """
    La funcion posicionar_todos escribe en el tablero 'board' la cantidad de barcos de un determinado tamaño a través de la funcion posicionar_barco anteriormente definida
    """
    for i in range(naves[tipo_nave][0]):
        board = posicionar_barco(naves, tipo_nave, inventario, board)
    return board

# Para finalizar la posición de todas las naves tenemos que llamar a la funcion posicionar todos para comprobar
#posicionar_todos(v.naves,'Portaviones', inventario, board)
#posicionar_todos(v.naves,'Buque', inventario, board)
#posicionar_todos(v.naves,'Crucero', inventario, board)
#posicionar_todos(v.naves,'lancha', inventario, board))