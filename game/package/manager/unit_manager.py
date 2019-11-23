import game.package.basic_module.unit_map
from game.package.basic_module.basic_define import draw_unit_map
from game.package.object.unit import *
from game.package.framework import states


class UnitManager:
    def __init__(self):
        self.activated_units = []  # object list
        self.prepared_units = []  #
        self.unit_map = game.package.basic_module.unit_map.Unit_Map()
        # self.unit_for_test = Unit_Warrior(100, 100)
        self.create_timer = 1000
        self.current_timer = 0

    def draw(self):
        draw_unit_map()
        for unit in self.activated_units:
            unit.draw()
        # self.unit_for_test.draw()

    def update(self):
        # self.unit_for_test.update()
        for unit in self.activated_units:
            unit.update()
        self.current_timer += 1
        if self.current_timer >= self.create_timer:
            self.prepare_unit()
            self.create_unit()
            self.current_timer = 0
        pass

    def create_unit(self):
        self.activated_units += self.prepared_units

    def prepare_unit(self):
        build_manager = states.GameState.build_state.building_manager
        basic_warrior_counter = 0
        basic_tent_counter = 0
        for building in build_manager.buildings:
            if building.type == BUILDING_TYPE_BASIC_WARRIOR:
                basic_warrior_counter += 1
            elif building.type == BUILDING_TYPE_BASIC_TENT:
                basic_tent_counter += 1
        self.prepared_units = [Unit_Warrior(random.randint(200, 600), random.randint(200, 400)) for i in
                               range(basic_warrior_counter)]

    pass
