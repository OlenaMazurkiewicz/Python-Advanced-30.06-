"Написать консольную игру Морской бой"
from random import randint


class Battleship:
    """
    Base class for battleship game
    """


    def __init__(self, size):
        """
         :param size: playboard size
        """
        self.size = size

    def field_ships_gen(self):
        field_ships = [['~'] * self.size for _ in range(self.size)]
        for n in range(8):
            ship_row = randint(0, self.size - 1)
            ship_col = randint(0, self.size - 1)
            field_ships[ship_col][ship_row] = 'o'
        print('Ships field')
        for i in range(self.size):
            for j in range(self.size):
                print(field_ships[i][j], end='  ')
            print()

        return field_ships
    
    def field_shots_gen(self):
        field_shots = [['~'] * self.size for _ in range(self.size)]
        print('Shots field')
        for i in range(self.size):
            for j in range(self.size):
                print(field_shots[i][j], end='  ')
            print()

        return field_shots

    def check_coord(self, x, y):
        if field_ships[x][y] == 'o':
            shots_ships[x][y] = 'x'
        else:
            print('make another shot')

    def run(self):
        player_ship_1 = Battleship.field_ships_gen(self)
        player_shot_1 = Battleship.field_shots_gen(self)
        print('Make one perfect shot, please!')
        x, y = input("x,y:").split(',')
        player_check_1 = Battleship.check_coord(self, x, y)


size = 10
battle = Battleship(size)

battle.run()









