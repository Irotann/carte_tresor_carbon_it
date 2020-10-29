import unittest

from modules.player import Player


class PlayerTest(unittest.TestCase):
    def test_player_init(self):
        coord = {'x': 2, 'y': 4}
        player = Player('Test', coord, 'S', 'AAA')

        self.assertEqual('Test', player.get_name())
        self.assertEqual(coord, player.get_coord())
        self.assertEqual('S', player.get_orientation())
        self.assertEqual(0, player.get_nb_treasure())
        self.assertEqual('AAA', player.get_action_sequence())

    def test_change_orientation_turn_right(self):
        coord = {'x': 2, 'y': 4}
        new_player = Player('Test', coord, 'S', 'AAA')

        new_player.change_orientation('D')

        self.assertEqual('O', new_player.get_orientation())

    def test_change_orientation_turn_left(self):
        coord = {'x': 2, 'y': 4}
        new_player = Player('Test', coord, 'S', 'AAA')

        new_player.change_orientation('G')

        self.assertEqual('E', new_player.get_orientation())

    def test_change_orientation_turn_right_with_limit(self):
        coord = {'x': 2, 'y': 4}
        new_player = Player('Test', coord, 'O', 'AAA')

        new_player.change_orientation('D')

        self.assertEqual('N', new_player.get_orientation())

    def test_change_orientation_turn_left_with_limit(self):
        coord = {'x': 2, 'y': 4}
        new_player = Player('Test', coord, 'N', 'AAA')

        new_player.change_orientation('G')

        self.assertEqual('O', new_player.get_orientation())

    def test_change_orientation_with_wrong_orientation(self):
        coord = {'x': 2, 'y': 4}
        new_player = Player('Test', coord, 'N', 'AAA')

        try:
            new_player.change_orientation('A')

            self.fail('Function should raise an AttributeError')
        except AttributeError:
            pass


if __name__ == '__main__':
    unittest.main()
