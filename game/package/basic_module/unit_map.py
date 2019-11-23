from game.package.basic_module.basic_define import UNIT_MAP_SIZE_X, UNIT_MAP_SIZE_Y


class Unit_Map:

    def __init__(self):
        self.unit_map = [[0 for x in range(UNIT_MAP_SIZE_X)] for y in range(UNIT_MAP_SIZE_Y)]
        self.init_unit_map()

    def init_unit_map(self):
        for y in range(UNIT_MAP_SIZE_Y):
            for x in range(UNIT_MAP_SIZE_X):
                self.unit_map[y][x] = True