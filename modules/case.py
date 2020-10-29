class Case:
    def __init__(self, x, y, relief):
        self.__coord = {'x': x, 'y': y}
        self.__relief = relief
        self.__nb_treasure = 0

    def set_relief(self, new_relief):
        self.__relief = new_relief

    def set_nb_treasure(self, nb_treasure):
        self.__nb_treasure = nb_treasure

    def get_coord(self):
        return self.__coord

    def get_relief(self):
        return self.__relief

    def get_nb_treasure(self):
        return self.__nb_treasure

    def remove_one_treasure(self):
        if self.__nb_treasure > 0:
            self.__nb_treasure -= 1
            return True

        return False
