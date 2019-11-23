from game.package.basic_module.basic_define import *
from game.package.basic_module import basic_struct


class Unit_Map:

    def __init__(self):
        self.unit_map = [[0 for x in range(UNIT_MAP_SIZE_X)] for y in range(UNIT_MAP_SIZE_Y)]
        self.init_unit_map()

    def init_unit_map(self):
        for y in range(UNIT_MAP_SIZE_Y):
            for x in range(UNIT_MAP_SIZE_X):
                self.unit_map[y][x] = True

    def update_unit_map(self, units):
        self.init_unit_map()
        for unit in units:
            self.unit_map[unit.position_on_tile.y][unit.position_on_tile.x] = False
            # self.unit_map[get_unit_tile_position_y(unit.position.y)][get_unit_tile_position_x(unit.position.x)] =
            # False

    def tmp_draw(self):
        for y in range(0, UNIT_MAP_SIZE_Y, 1):
            for x in range(0, UNIT_MAP_SIZE_X, 1):
                if not self.unit_map[y][x]:
                    pico2d.draw_rectangle(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH,
                                          UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT,
                                          UNIT_MAP_START_X + (x + 1) * UNIT_TILE_WIDTH,
                                          UNIT_MAP_START_Y + (y + 1) * UNIT_TILE_HEIGHT)

    def is_movable(self, unit):
        moved_position = basic_struct.Position(unit.position_on_window.x, unit.position_on_window.y)
        moved_position.move_position(unit.direction.x, unit.direction.y)
        if get_unit_tile_position_x(moved_position.x) == unit.position_on_tile.x and get_unit_tile_position_y(
                moved_position.y) == unit.position_on_tile.y:
            return True
        else:
            return self.unit_map[get_unit_tile_position_y(moved_position.y)][get_unit_tile_position_x(moved_position.x)]
        # if self.unit_map[get_unit_tile_position_y(moved_position.y)][get_unit_tile_position_x(moved_position.x)]:
        #     return True
        # else:
        #     direction = unit.direction
        #     direction.x *= -1
        #     direction.y *= -1
        #     unit.position.move_position(direction)
        #     return False