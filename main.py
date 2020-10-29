from modules import read
from modules.treasure_map import TreasureMap
from modules.write import write_output_file


def launch_game(input_file_path, output_file_path):
    input_lines = read.read_file(input_file_path)

    treasure_map = TreasureMap(input_lines)

    treasure_map.play_game()

    write_output_file(treasure_map, output_file_path, input_lines)

    return treasure_map


if __name__ == '__main__':
    launch_game('modules/tests/test_files/test_input',
                'modules/tests/test_files/expected_output')
