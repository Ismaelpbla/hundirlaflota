import variables as v # importa el archivo variables.py
import functions as fnc # importa el archivo functionss.py
import classes as hf # importa el archivo class1.py
import numpy as np # importa la libreria numpy

partida = hf.hundir_flota() # Crea un objeto mediante la clase hundir la flota del archivo class1.py

vidas_jugador = np.sum(partida.board_jugador == 'O') # definimos las vidas del jugador a través de la suma del numero de veces que aparece el string 'O'
vidas_maquina = np.sum(partida.board_maquina == 'O')
print(f'Bienvenido capitán, tenemos que hundir un total de {vidas_maquina} barcos, necesitamos toda su pericia')

id = 'player' # Asignamos 'player' a id

while vidas_maquina > 0 and vidas_jugador > 0: # iniciamos un bucle while que sea valido siempre que las vidas sean mayores a 0
    if id == 'player':
        print(partida.board_jugador)
        print(partida.board_check_jugador)
        partida.shot_order() # Pedimos unas coordenadas al jugador para realizar un tiro
        partida.check_shot() # Comprobamos que el tiro acierte o no
        if partida.tocado == True: # Si el tiro acierta la variable de control es True con lo cual podriamos entrar en este bucle
            vidas_maquina = vidas_maquina -1 # La vida de la maquina al acertar disminuiría en uno
            print(partida.shot_coordenate_X, partida.shot_coordenate_Y)
            print('Tocado!!')
            print(f'A la maquina le quedan {vidas_maquina} posiciones con barcos')
        else: # En caso de no acertar la variable de control es False con lo cual entrariamos en este else
            id = 'IA' # La id cambiaría a 'IA' de tal forma que pasariamos al elif de mas abajo
            print(partida.shot_coordenate_X, partida.shot_coordenate_Y)
            print('Agua!')
            print(f'A la maquina le quedan {vidas_maquina} posiciones con barcos')
            

    elif id == 'IA':
            partida.shot_order_maquina() # La maquina generaría aleatoriamente unas coordenadas donde lanzar el tiro
            partida.check_shot_machine() # Y comprobaria que el tiro es acertado o no
            if partida.tocado_m == True:
                vidas_jugador = vidas_jugador - 1
                print('La maquina ha acertado!')
            else:
                id = 'player'
                print('la maquina ha fallado!')
                     
else: # Cuando las vidas del jugador o de la maquina llegan a 0 el bucle se rompe y termina el juego
    if vidas_maquina == 0:
        print('Has ganado')
    else:
        print('Has perdido')
