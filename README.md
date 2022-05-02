
# Battleship

This is the game of battleship developed using python and numpy library.
## Authors

@ismael.pbla(https://github.com/Ismaelpbla)


[![Python](https://img.shields.io/badge/python-v3.7-blue)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


## Problem

1. Two players You and the IA
2. A **10 x 10 board** with positions
3. First put the boats in the board randomly
    * 4 boats of 1 position
    * 3 boats de 2 of 2 positions
    * 2 boats of 3 positions 
    * 1 barco de 4 positions 

4. Both you and the machine have a board with ships, and you have to "shoot" and sink your opponent's ships until one player runs out of ships, and therefore loses.
5. It works in turns and you start.
6. Each turn you shoot at a coordinate (X, Y) on the opponent's board. **If you hit it, it's your turn again**. If you don't, it's the machine's turn.
7. On the machine's turns, if you hit, it's your turn again. Where does the machine shoot? At a random point on your board.
8. If all of a player's ships are sunk, the game ends and the other player wins.
9. As a rule of the game there can be no ships stuck to each other without spaces between them.

## What we need?

We need to define three main variables:

- BOARDS We have to define three boards one with the player's ships and other with the IA's ships. Also we have to define a board to check if the shots impact or not.

- A dictionary that have the the size and number of each ship.

- A LIST wich is called inventory. In this list we storage all the boats with correct coordinates


## How to put the ships randomly?

To put the ships randomly in both boards (player's board and IA's board) we use a total of 7 functions:

- **First_coordinate**. The first_coordinate function is a random generator of X and Y coordinates of the ships, it takes as variable "length" which is the size of the ships. It returns a random coordinate
- **orientation**. The orientation function generates a random value from the orientation_list which contains v or h which is the vertical or horizontal orientation of the ships.
- **distancia**. The distance function is the distance between two randomly generated coordinates.
- **check_position** The function check position takes the inventory variables defined above and the variable ship that will be appended to the list later. This function returns True if the *distance* between the randomly generated coordinate and the ones in the inventory list are valid, otherwise it returns True.
- **ship** . The ship function generates the coordinates of a ship of a given length with a random initial orientation and coordinates. In addition, it checks through the function *check_position* if each of the coordinates of the ship is valid so that if it is valid, it appends that coordinate to the ship list and if not, the while loop generates another coordinate horizontally or vertically consecutive to the previous one. The function returns the ship list with the number of coordinates equal to the corresponding length.
- **posicionar_barco** . The position ship function generates a ship from the *ship* function defined above. It then iterates through each of the ship's coordinates and appends them to the inventory, so that it can be used in the *check position* function. Finally it puts a string 'O' on the board defined at the beginning of the script. The function returns the board with the positioned ship.
- **posicionar_todos** . The function position_all writes to the board the number of ships of a given size through the previously defined function *posicionar_barco*.

### How it works?
## The Game

To make the game works we need to create a class. This class consist of:

- A constructor. When the board will be defined and the ships will be positionated on the board
- A shot_order method that requires input from the player to describe the square on the board where he wants to shoot.
- A check_shot method which checks whether the shot_order coordinates have hit a ship or not.
- a shot_order_machine method in which the machine randomly decides two coordinates X and Y
- A check_shot_machine method that checks if the machine coordinates hit the player's ships or not.

Once the class were made, we have to make a main script where the game will works. To make this we:
- First, create the variables *vida_jugador* and *vida_maquina* which are the variables who start the "while" loop and break it when the variables reach the value of 0.
- After the "while" loop we call the shot_order method to claim a coordenate and the check_shot method to check if the coordinate hit or not.
- Now, could happend two situations: That the coordinate hits a ship, or not. In both situations we enter or exit to the if loop thorugh a control variable called *tocado*. So if tocado is True the player continue playing and if not the IA starts its turn.
- In the IA turn occurs the same with only one difference: The coordinates will be generated randomly.
- When the IA or the player hits a ship, we removed a value of 1 to the variables vida_jugador or vida_maquina. So when one of this variables reach 0, the while loop breaks and the game end.
