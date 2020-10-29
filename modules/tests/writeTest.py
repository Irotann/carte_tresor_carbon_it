import unittest

from modules.read import read_file
from modules.treasure_map import TreasureMap
from modules.write import write_output_file


class WriteTest(unittest.TestCase):
    def test_write_output_file(self):
        output_file = 'test_files/output'
        input_lines = ['C - 3 - 4\n', 'M - 1 - 0\n', 'T - 0 - 3 - 2\n',
                       'T - 1 - 3 - 1\n', 'A - Lara - 0 - 3 - S - AAAA']
        treasure_map = TreasureMap(input_lines)
        treasure_map.get_players()[0].add_one_treasure()
        treasure_map.get_case_by_coord({'x': 1, 'y': 3}).remove_one_treasure()

        write_output_file(treasure_map, output_file, input_lines)
        result_lines = read_file(output_file)

        self.assertEqual(input_lines[0], result_lines[0])
        self.assertEqual(input_lines[1], result_lines[1])
        self.assertEqual(input_lines[2], result_lines[2])
        self.assertEqual('A - Lara - 0 - 3 - S - 1\n', result_lines[3])


if __name__ == '__main__':
    unittest.main()
