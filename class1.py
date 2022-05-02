import functionss as fnc
import numpy as np
import random as rd

class hundir_flota():

    def __init__(self):
        self.board_jugador = np.full((10,10), ' ')
        self.board_check_jugador = np.full((10,10), ' ')
        inventario_jugador = []
        self.board_maquina = np.full((10,10), 'W')
        inventario_maquina = []
        self.board_check_maquina = np.full((10,10), ' ')

        fnc.posicionar_todos(1, 4, inventario_jugador, self.board_jugador)
        fnc.posicionar_todos(2, 3, inventario_jugador, self.board_jugador)
        fnc.posicionar_todos(3, 2, inventario_jugador, self.board_jugador)
        fnc.posicionar_todos(4, 1, inventario_jugador, self.board_jugador)
        print(self.board_jugador)
        print(self.board_check_jugador)

        #fnc.posicionar_todos(1, 4, inventario_maquina, self.board_maquina)
        #fnc.posicionar_todos(2, 3, inventario_maquina, self.board_maquina)
        #fnc.posicionar_todos(3, 2, inventario_maquina, self.board_maquina)
        fnc.posicionar_todos(1, 1, inventario_maquina, self.board_maquina)
        print(self.board_maquina)
        print(self.board_check_maquina)
    
    def shot_order(self):
       self.shot_coordenate_X = input('Dame una coordenada X del 0 al 9')
       self.shot_coordenate_Y = input('Dame una coordenada Y del 0 al 9')
       self.shot_coordenate = ((int(self.shot_coordenate_X)), (int(self.shot_coordenate_Y)))
       return self.shot_coordenate
    
    def check_shot(self):
        if self.board_maquina[self.shot_coordenate] == 'O':
            self.tocado = True
            print('Tocado!!')
            self.board_check_jugador[self.shot_coordenate] = 'T'
            return self.board_check_jugador
    
        else:
            self.tocado = False
            print('Agua!')
            self.board_check_jugador[self.shot_coordenate] = 'A'
            return self.board_check_jugador

    def shot_order_maquina(self):
        self.X_maquina = rd.randint(0,9)
        self.Y_maquina = rd.randint(0,9)
        self.shot_maquina = (self.X_maquina, self.Y_maquina)
        return self.shot_maquina

    def check_shot_machine (self):
         if self.board_jugador[self.shot_maquina] == 'O':
            self.tocado_m = True
            self.board_check_maquina[self.shot_maquina] = 'T'
            return self.board_check_maquina
         else:
            self.tocado_m = False
            self.board_check_maquina[self.shot_maquina] = 'A'
            return self.board_check_maquina
