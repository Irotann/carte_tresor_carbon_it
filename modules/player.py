CARDINAL_DIRECTIONS = ['N', 'E', 'S', 'O']


class Player:
    def __init__(self, name, coord, orientation, action_sequence):
        self.__name = name
        self.__coord = coord
        self.__orientation = orientation
        self.__nb_treasures = 0
        self.__action_sequence = action_sequence

    def change_orientation(self, direction):
        current_direction = CARDINAL_DIRECTIONS.index(self.__orientation)

        if direction == 'D':
            self.__orientation = CARDINAL_DIRECTIONS[(current_direction + 1) % 4]
        elif direction == 'G':
            self.__orientation = CARDINAL_DIRECTIONS[(current_direction - 1) % 4]
        else:
            raise AttributeError('Wrong direction was passed: ', direction)

    def get_name(self):
        return self.__name

    def get_coord(self):
        return self.__coord

    def get_orientation(self):
        return self.__orientation

    def get_nb_treasure(self):
        return self.__nb_treasures

    def get_action_sequence(self):
        return self.__action_sequence

    def set_coord(self, coord):
        self.__coord = coord

    def add_one_treasure(self):
        self.__nb_treasures += 1

    def to_string(self):
        return 'A - ' + \
               self.__name + ' - ' + \
               str(self.__coord['x']) + ' - ' + \
               str(self.__coord['y']) + ' - ' + \
               self.__orientation + ' - ' + \
               str(self.__nb_treasures) + '\n'
