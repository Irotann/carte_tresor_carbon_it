import unittest

from modules import read


class ReadTest(unittest.TestCase):
    def test_read_input_file(self):
        path_file = 'test_files/test_input'

        lines_list = read.read_file(path_file)

        self.assertIsNotNone(lines_list)
        self.assertEqual(6, len(lines_list))

    def test_read_input_file_when_not_exist(self):
        try:
            read.read_file('')

            self.fail()
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
