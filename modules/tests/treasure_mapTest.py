import unittest

from modules.case import Case
from modules.treasure_map import TreasureMap, add_dict_values_by_key


class TreasureMapTest(unittest.TestCase):
    def test_treasure_map(self):
        input_lines = ['C - 3 - 4']
        treasure_map = TreasureMap(input_lines)

        cases = treasure_map.get_cases()
        self.assertEqual(3 * 4, len(cases))

    def test_get_case_by_coord(self):
        input_lines = ['C - 1 - 1']
        treasure_map = TreasureMap(input_lines)
        treasure_map.get_cases().append(Case(2, 1, 'M'))
        treasure_map.get_cases().append(Case(3, 2, '.'))

        mountain_case = treasure_map.get_case_by_coord({'x': 2, 'y': 1})

        self.assertEqual(3, len(treasure_map.get_cases()))
        self.assertEqual('M', mountain_case.get_relief())

    def test_add_mountain(self):
        input_lines = ['C - 1 - 2']
        treasure_map = TreasureMap(input_lines)

        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 0}).get_relief())
        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 1}).get_relief())

        treasure_map.add_mountain('M - 0 - 0')

        self.assertEqual('M', treasure_map.get_case_by_coord({'x': 0, 'y': 0}).get_relief())
        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 1}).get_relief())

    def test_add_mountain_on_non_existing_case(self):
        try:
            input_lines = ['C - 1 - 2']
            treasure_map = TreasureMap(input_lines)

            treasure_map.add_mountain('M - 0 - 2')

            self.fail()
        except AttributeError:
            pass

    def test_add_treasure(self):
        input_lines = ['C - 1 - 2']
        treasure_map = TreasureMap(input_lines)

        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 0}).get_relief())
        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 1}).get_relief())

        treasure_map.add_treasure('T - 0 - 0 - 3')

        self.assertEqual(3, treasure_map.get_case_by_coord({'x': 0, 'y': 0}).get_nb_treasure())
        self.assertEqual('.', treasure_map.get_case_by_coord({'x': 0, 'y': 1}).get_relief())

    def test_add_treasure_on_non_existing_case(self):
        try:
            input_lines = ['C - 1 - 2']
            treasure_map = TreasureMap(input_lines)

            treasure_map.add_treasure('T - 0 - 2 - 3')

            self.fail()
        except AttributeError:
            pass

    def test_add_player(self):
        input_lines = ['C - 1 - 2']
        treasure_map = TreasureMap(input_lines)

        self.assertEqual(0, len(treasure_map.get_players()))

        treasure_map.add_player('A - Lara - 0 - 0 - S - AADADAGGA')

        self.assertEqual(1, len(treasure_map.get_players()))
        self.assertEqual('Lara', treasure_map.get_players()[0].get_name())

    def test_add_player_on_non_existing_case(self):
        try:
            input_lines = ['C - 1 - 2']
            treasure_map = TreasureMap(input_lines)

            treasure_map.add_player('A - Lara - 1 - 1 - S - AADADAGGA')

            self.fail()
        except AttributeError:
            pass

    def test_add_dict_values_by_key(self):
        dict1 = {'x': 42, 'y': 24}
        dict2 = {'x': 7, 'y': 21}

        result = add_dict_values_by_key(dict1, dict2)

        self.assertEqual(49, result['x'])
        self.assertEqual(45, result['y'])

    def test_take_turn(self):
        input_lines = ['C - 1 - 2', 'A - Lara - 0 - 0 - S - AA']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]

        end_game = treasure_map.take_turn(0, player)

        self.assertTrue(end_game)

    def test_take_turn_when_it_s_last_player_action(self):
        input_lines = ['C - 1 - 2', 'A - Lara - 0 - 0 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]

        end_game = treasure_map.take_turn(0, player)

        self.assertFalse(end_game)

    def test_take_turn_when_no_player_action_left(self):
        input_lines = ['C - 1 - 2', 'A - Lara - 0 - 0 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]

        end_game = treasure_map.take_turn(5, player)

        self.assertFalse(end_game)

    def test_go_forward(self):
        input_lines = ['C - 1 - 2', 'A - Lara - 0 - 0 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]
        player_coord = player.get_coord()
        player_new_coord = {'x': 0, 'y': 1}

        treasure_map.go_forward(player)

        self.assertIsNone(treasure_map.get_player_by_coord(player_coord))
        self.assertIsNotNone(treasure_map.get_player_by_coord(player_new_coord))
        self.assertEqual('Lara', treasure_map.get_player_by_coord(player_new_coord).get_name())

    def test_go_forward_with_treasure_on_destination(self):
        input_lines = ['C - 1 - 2', 'T - 0 - 1 - 3', 'A - Lara - 0 - 0 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]
        player_new_coord = {'x': 0, 'y': 1}

        treasure_map.go_forward(player)

        self.assertIsNotNone(treasure_map.get_player_by_coord(player_new_coord))
        self.assertEqual('Lara', treasure_map.get_player_by_coord(player_new_coord).get_name())
        self.assertEqual(1, treasure_map.get_player_by_coord(player_new_coord).get_nb_treasure())
        self.assertEqual(2, treasure_map.get_case_by_coord(player_new_coord).get_nb_treasure())

    def test_go_forward_with_mountain_on_destination(self):
        input_lines = ['C - 1 - 2', 'M - 0 - 1', 'A - Lara - 0 - 0 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]
        player_coord = player.get_coord()

        treasure_map.go_forward(player)

        self.assertIsNotNone(treasure_map.get_player_by_coord(player_coord))
        self.assertEqual('Lara', treasure_map.get_player_by_coord(player_coord).get_name())

    def test_go_forward_with_other_player_on_destination(self):
        input_lines = ['C - 1 - 2', 'A - Lara - 0 - 0 - S - A', 'A - Test - 0 - 1 - S - A']
        treasure_map = TreasureMap(input_lines)
        player = treasure_map.get_players()[0]
        other_player = treasure_map.get_players()[1]
        player_coord = player.get_coord()
        other_player_coord = other_player.get_coord()

        treasure_map.go_forward(player)

        self.assertIsNotNone(treasure_map.get_player_by_coord(player_coord))
        self.assertEqual('Lara', treasure_map.get_player_by_coord(player_coord).get_name())
        self.assertIsNotNone(treasure_map.get_player_by_coord(other_player_coord))
        self.assertEqual('Test', treasure_map.get_player_by_coord(other_player_coord).get_name())


if __name__ == '__main__':
    unittest.main()
