from random import randint

class Monty:
    def __init__(self, change):
        # Jugador cambia o no
        self.change = change
        # Puertas, con cabras (0 = cabra)
        self.doors = [0,0,0]
        # Posiciono el auto (1) en una posición al azar
        car_position = randint(0,2)
        self.doors[car_position] = 1
        self.player_choice =  randint(0,2)
        self.win_result = 'Not played'

    def play(self):
        # Si elige cabra y cambia -> Gana
        # Si elige auto y cambia -> Pierde
        # Si elige cabra y no cambia -> Pierde
        # Si elige auto y no cambia -> Gana
        self.win_result = (self.doors[self.player_choice] == 0 and self.change) or (self.doors[self.player_choice] == 1 and not self.change) 
    
