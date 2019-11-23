from game.package.basic_module import unit_map
from game.package.object.unit import *
from game.package.framework import states


class UnitManager:
    def __init__(self):
        self.activated_units = []
        self.prepared_units = []
        self.unit_map = unit_map.Unit_Map()
        self.create_timer = 1000
        self.current_timer = 0

    def draw(self):
        # draw_unit_map()
        for unit in self.activated_units:
            unit.draw()
        self.unit_map.tmp_draw()

    def update(self):
        for unit in self.activated_units:
            unit.set_target(self.activated_units)
            unit.update()
        self.current_timer += 1
        if self.current_timer >= self.create_timer:
            self.prepare_unit()
            self.create_unit()
            self.current_timer = 0
        self.unit_map.update_unit_map(self.activated_units)
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
        self.prepared_units = [Unit_Warrior(random.randint(200, 600), random.randint(200, 400), UNIT_TEAM_PLAYER) for i
                               in range(basic_warrior_counter)] + [Unit_Enemy(random.randint(200, 600), random.randint(400, 600), UNIT_TEAM_ENEMY)]

    pass
