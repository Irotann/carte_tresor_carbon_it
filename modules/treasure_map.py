from modules.read import extract_lines_by_indicator
from modules.case import Case
from modules.player import Player


def get_move(direction):
    if direction == 'N':
        return {'x': 0, 'y': -1}
    elif direction == 'E':
        return {'x': 1, 'y': 0}
    elif direction == 'S':
        return {'x': 0, 'y': 1}
    elif direction == 'O':
        return {'x': -1, 'y': 0}


def add_dict_values_by_key(dict1, dict2):
    result = dict1.copy()
    for key, value in dict1.items():
        result[key] = value + dict2.get(key, 0)
    return result


class TreasureMap:
    def __init__(self, input_lines):
        map_line = extract_lines_by_indicator(input_lines, 'C')[0]
        mountain_lines = extract_lines_by_indicator(input_lines, 'M')
        treasure_lines = extract_lines_by_indicator(input_lines, 'T')
        player_lines = extract_lines_by_indicator(input_lines, 'A')

        list_coord = map_line.split('-')

        nb_case_x = int(list_coord[1])
        nb_case_y = int(list_coord[2])

        self.__cases = []
        for y in range(nb_case_y):
            for x in range(nb_case_x):
                self.__cases.append(Case(x, y, '.'))

        self.__players = []

        for mountain in mountain_lines:
            self.add_mountain(mountain)

        for treasure in treasure_lines:
            self.add_treasure(treasure)

        for player in player_lines:
            self.add_player(player)

    def get_cases(self):
        return self.__cases

    def get_players(self):
        return self.__players

    def add_mountain(self, mountain_line):
        list_coord = mountain_line.split('-')

        coord = {'x': int(list_coord[1]), 'y': int(list_coord[2])}

        self.get_case_by_coord(coord).set_relief('M')

    def add_treasure(self, treasure_line):
        list_coord = treasure_line.split('-')

        coord = {'x': int(list_coord[1]), 'y': int(list_coord[2])}
        nb_treasure = int(list_coord[3])

        self.get_case_by_coord(coord).set_nb_treasure(nb_treasure)

    def add_player(self, player_line):
        list_coord = player_line.split('-')

        name = list_coord[1].strip()
        coord = {'x': int(list_coord[2]), 'y': int(list_coord[3])}
        orientation = list_coord[4].strip()
        displacement_sequence = list_coord[5].strip()

        if self.get_case_by_coord(coord) is not None:
            new_player = Player(name, coord, orientation, displacement_sequence)

            self.__players.append(new_player)
        else:
            raise AttributeError('Coordinates are out of limits')

    def play_game(self):
        turn_count = 0
        end_game = False
        while not end_game:
            end_game = True
            for player in self.__players:
                end_game = end_game and not self.take_turn(turn_count, player)
            turn_count += 1

    def take_turn(self, turn_number, player):
        if len(player.get_action_sequence()) <= turn_number:
            return False

        current_action = player.get_action_sequence()[turn_number]

        if current_action == 'A':
            self.go_forward(player)
        elif current_action == 'D' or current_action == 'G':
            player.change_orientation(current_action)
        else:
            raise AttributeError('Wrong action was passed: ', current_action)

        return len(player.get_action_sequence()) > turn_number + 1

    def go_forward(self, player):
        gain_per_axis = get_move(player.get_orientation())
        destination_coord = add_dict_values_by_key(gain_per_axis, player.get_coord())
        destination_case = self.get_case_by_coord(destination_coord)

        if destination_case.get_relief() != 'M' and self.get_player_by_coord(destination_coord) is None:
            player.set_coord(destination_coord)
            if destination_case.remove_one_treasure():
                player.add_one_treasure()

    def get_case_by_coord(self, coord):
        for case in self.__cases:
            if case.get_coord() == coord:
                return case

    def get_player_by_coord(self, coord):
        for player in self.__players:
            if player.get_coord() == coord:
                return player

        return None


if __name__ == '__main__':
    pass
