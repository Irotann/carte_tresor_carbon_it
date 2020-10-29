import unittest

from modules.case import Case


class CaseTest(unittest.TestCase):
    def test_case_init(self):
        case = Case(1, 1, 'M')

        self.assertEqual({'x': 1, 'y': 1}, case.get_coord())
        self.assertEqual('M', case.get_relief())
        self.assertEqual(0, case.get_nb_treasure())

    def test_remove_one_treasure(self):
        case = Case(1, 1, 'M')
        case.set_nb_treasure(10)

        flag = case.remove_one_treasure()

        self.assertTrue(flag)
        self.assertEqual(9, case.get_nb_treasure())

    def test_remove_one_treasure_when_there_is_no_treasure_left(self):
        case = Case(1, 1, 'M')
        case.set_nb_treasure(0)

        flag = case.remove_one_treasure()

        self.assertFalse(flag)
        self.assertEqual(0, case.get_nb_treasure())


if __name__ == '__main__':
    unittest.main()
