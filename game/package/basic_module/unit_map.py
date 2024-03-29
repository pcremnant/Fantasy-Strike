from game.package.basic_module.basic_define import *


class Unit_Map:

    def __init__(self):
        self.map = [[0 for x in range(UNIT_MAP_SIZE_X)] for y in range(UNIT_MAP_SIZE_Y)]
        self.init_unit_map()

    def init_unit_map(self):
        for y in range(UNIT_MAP_SIZE_Y):
            for x in range(UNIT_MAP_SIZE_X):
                self.map[y][x] = True

    def update_unit_map(self, units):
        self.init_unit_map()
        for unit in units:
            self.map[unit.position_on_tile.y][unit.position_on_tile.x] = False

    def tmp_draw(self):
        for y in range(0, UNIT_MAP_SIZE_Y, 1):
            for x in range(0, UNIT_MAP_SIZE_X, 1):
                if not self.map[y][x]:
                    pico2d.draw_rectangle(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH,
                                          UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT,
                                          UNIT_MAP_START_X + (x + 1) * UNIT_TILE_WIDTH,
                                          UNIT_MAP_START_Y + (y + 1) * UNIT_TILE_HEIGHT)


