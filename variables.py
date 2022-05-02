import numpy as np
import random as rd

tablero_jugador = np.full((11,11), ' ') #genera el tablero del jugador 
columnas_ref = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
filas_ref = [' ',0,1,2,3,4,5,6,7,8,9]

for i in range(len(columnas_ref)):
    tablero_jugador[i,0] = columnas_ref[i] #incorpora las referencias de columnas


for i in range(len(filas_ref)): #incorpora las referencias de filas
    tablero_jugador[10,i] = filas_ref[i]


board_check_jugador = np.full((11,11), ' ') # genera el tablero de comprobación del jugador

for i in range(len(columnas_ref)):
    board_check_jugador[i,0] = columnas_ref[i]


for i in range(len(filas_ref)):
    board_check_jugador[10,i] = filas_ref[i]


board_maquina = np.full((11,11), 'W') # genera el tablero de la maquina

for i in range(len(columnas_ref)):
    board_maquina[i,0] = columnas_ref[i]


for i in range(len(filas_ref)):
    board_maquina[10,i] = filas_ref[i]


board_check_maquina = np.full((11,11), ' ') # gnera el tablero de comprobación de la maquina

for i in range(len(columnas_ref)):
    board_check_maquina[i,0] = columnas_ref[i]


for i in range(len(filas_ref)):
    board_check_maquina[10,i] = filas_ref[i]




naves = {'lancha':[4,1], 'crucero':[3,2], 'buque':[2,3], 'portaviones':[1,4]} # diccionario con las características de las naves (numero de naves y eslora)

naves_test = {'lancha':[1,1]}