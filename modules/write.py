import os

from modules.read import extract_lines_by_indicator
from modules.treasure_map import TreasureMap


def write_output_file(treasure_map: TreasureMap, file_path: str, input_lines: []):
    mode = 'a' if not os.path.exists(file_path) else 'w'
    with open(file_path, mode) as f:
        map_line = extract_lines_by_indicator(input_lines, 'C')[0]
        mountain_lines = extract_lines_by_indicator(input_lines, 'M')
        treasure_lines = extract_lines_by_indicator(input_lines, 'T')

        f.write(map_line)

        for line in mountain_lines:
            f.write(line)

        for line in treasure_lines:
            list_coord = line.split('-')

            coord = {'x': int(list_coord[1]), 'y': int(list_coord[2])}

            case = treasure_map.get_case_by_coord(coord)
            if case.get_nb_treasure() > 0:
                f.write('T - ' + str(coord['x']) + ' - ' + str(coord['y']) + ' - ' + str(case.get_nb_treasure()) + '\n')

        for player in treasure_map.get_players():
            f.write(player.to_string())
