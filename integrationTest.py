import filecmp
import unittest

from main import launch_game


class MainTest(unittest.TestCase):
    def test_launch_game(self):
        input_file = 'modules/tests/test_files/test_input'
        output_file = 'modules/tests/test_files/output'
        expected_output = 'modules/tests/test_files/expected_output'

        launch_game(input_file, output_file)

        self.assertTrue(filecmp.cmp(output_file, expected_output))


if __name__ == '__main__':
    unittest.main()
