from game.package.object.unit import *
from game.package.framework.states import *


class UnitManager:
    def __init__(self):
        self.activated_units = []  # object list
        self.prepared_units = []  #
        self.unit_map = basic_struct.Unit_Map()
        self.unit_for_test = Unit_Warrior(100, 100)

    def draw(self):
        self.unit_map.tmp_draw_table()
        self.unit_for_test.draw()

    def update(self):
        pass

    def create_unit(self):
        self.activated_units += self.prepared_units

    def prepare_unit(self):
        build_manager = get_building_manager()
        basic_warrior_counter = 0
        basic_tent_counter = 0
        for building in build_manager.buildings:
            if building.type == BUILDING_TYPE_BASIC_WARRIOR:
                basic_warrior_counter += 1
            elif building.type == BUILDING_TYPE_BASIC_TENT:
                basic_tent_counter += 1
        self.prepared_units = [Unit_Warrior() for i in range(basic_warrior_counter)]

    pass
