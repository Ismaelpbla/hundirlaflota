import variables as v # importamos el archivo varibles.py
import functions as fnc # importamos el archvio functionss.py
import numpy as np # importamos numpy
import random as rd # importamos la libreria random

class hundir_flota():
    """
    La clase hundir la flota consta de:
    - Un constructor. Donde se posicionan inicialmente los barcos tanto de la maquina como del jugador
    - Un metodo shot_order que requiere de un input del jugador para describir la casilla del tablero en la que quiere disparar
    - Un metodo check_shot en el que se comprueba si las coordenadas de shot_order ha impactado con un barco o no
    - Un metodo shot_order_maquina en el que la maquina decide aleatoriamente dos coordenadas X e Y
    - Un metodo check_shot_machine que comprueba si las coordenadas de la maquina impactan o no con las naves del jugador.
    """

    def __init__(self):
        self.board_jugador = v.tablero_jugador # Tablero del jugador donde se posicionar sus naves
        self.board_check_jugador = v.board_check_jugador # Tablero del jugador donde se registrara si los tiros impactan o no sobre la nave enemiga
        inventario_jugador = [] # inventario del jugador donde se guardan los barcos generados mediante la funcion posicionar barco
        self.board_maquina = v.board_maquina # Tablero de la maquina donde posiciona sus naves
        inventario_maquina = [] # inventario de la maquina donde se guardan los barcos generados por la funcion posicionar barco
        self.board_check_maquina = v.board_check_maquina # tablero donde se registran los impactos de la maquina

        fnc.posicionar_todos(v.naves, 'portaviones', inventario_jugador, self.board_jugador) # Posicionando 1 barco de 4 coordenadas de tamaño
        fnc.posicionar_todos(v.naves, 'buque', inventario_jugador, self.board_jugador) # Posicionando 2 barcos de 3 coordenadas de tamaño
        fnc.posicionar_todos(v.naves, 'crucero', inventario_jugador, self.board_jugador) # Posicionando 3 barcos de 2 coordenadas de tamaño
        fnc.posicionar_todos(v.naves, 'lancha', inventario_jugador, self.board_jugador) # Posicionando 4 barcos de 1 coordenada de tamaño

        fnc.posicionar_todos(v.naves, 'portaviones', inventario_maquina, self.board_maquina)
        fnc.posicionar_todos(v.naves, 'buque', inventario_maquina, self.board_maquina)
        fnc.posicionar_todos(v.naves, 'crucero', inventario_maquina, self.board_maquina)
        fnc.posicionar_todos(v.naves, 'lancha', inventario_maquina, self.board_maquina)
        #print(self.board_maquina)
        #print(self.board_check_maquina)
    
    def shot_order(self):
       self.shot_coordenate_X = input('Dame una coordenada X del A al J-->') # Requiere al usuario un valor para las filas
       self.shot_coordenate_Y = input('Dame una coordenada Y del 0 al 9-->') # Requiere al usuario un valor para las columnas
       dict_a = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
       dict_b = {'0':1, '1':2, '2':3, '3':4, '4':5, '5':6, '6':7, '7':8, '9':10}
       self.shot_coordenate = ((dict_a[self.shot_coordenate_X])), (dict_b[self.shot_coordenate_Y]) # Genera una tupla con las coordenadas X e Y
       return self.shot_coordenate # devuelve la tupla con la coordenada que se quiere disparar
    
    def check_shot(self):
        if self.board_maquina[self.shot_coordenate] == 'O': # Si la coordenada obtenida en shot_order coincide en el tablero de la maquina con un string 'O' 
            self.tocado = True # variable de control para generar el bucle en el script main.py
            self.board_check_jugador[self.shot_coordenate] = 'T' # Escribe en el tablero de comprobación del jugador un string 'T' para recordar que en esa coordenada ha habido un impacto
            return self.board_check_jugador # Devuelve el tablero de comprobacion del jugador con los cambios realizados
    
        else:
            self.tocado = False
            self.board_check_jugador[self.shot_coordenate] = 'A' # Escribe en el tablero de comprobación del jugador un string 'A' para recordar que en esa coordenada NO ha habido un impacto
            return self.board_check_jugador # Devuelve el tablero de comprobacion del jugador con los cambios realizados

    def shot_order_maquina(self):
        self.X_maquina = rd.randint(1,10) # Genera aleatoriamente un numero del 0 al 9
        self.Y_maquina = rd.randint(1,10)
        self.shot_maquina = (self.X_maquina, self.Y_maquina) # Crea la tupla con los valores aleatorios X e Y
        return self.shot_maquina

    def check_shot_machine (self):
         if self.board_jugador[self.shot_maquina] == 'O':
            self.tocado_m = True
            self.board_jugador[self.shot_maquina] = 'X' # Si la maquina acierta marca una X en el tablero del jugador
            return self.board_jugador
         else:
            self.tocado_m = False
            self.board_check_maquina[self.shot_maquina] = 'A'
            return self.board_check_maquina