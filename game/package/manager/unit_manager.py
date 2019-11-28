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
        self.activated_units += [Unit_EnemyCastle(WINDOW_WIDTH // 2, get_unit_tile_position_y(WINDOW_HEIGHT) * UNIT_TILE_HEIGHT, UNIT_TEAM_ENEMY)]
        self.winner = None

    def draw(self):
        for unit in self.activated_units:
            unit.draw()
        self.unit_map.tmp_draw()

    def update(self):
        for unit in self.activated_units:
            unit.set_target(self.activated_units)
            self.unit_map.update_unit_map(self.activated_units)
            unit.update(self.unit_map.is_movable(unit))
            if unit.is_attacking:
                unit.attack(self.activated_units)

        for unit in self.activated_units:
            if not unit.is_living:
                self.activated_units.remove(unit)
                del unit

        self.current_timer += 1
        if self.current_timer >= self.create_timer:
            self.prepare_unit()
            self.create_unit()
            self.current_timer = 0

        self.activated_units.sort(key=lambda x: x.position_on_tile.y, reverse=True)

        is_player_living = False
        is_enemy_living = False
        for unit in self.activated_units:
            if unit.is_castle:
                if unit.team == UNIT_TEAM_PLAYER:
                    is_player_living = True
                elif unit.team == UNIT_TEAM_ENEMY:
                    is_enemy_living = True

        # test code ---
        is_player_living = True
        # ----------
        if is_player_living and is_enemy_living:
            self.winner = None
        elif is_player_living:
            self.winner = 'player'
        elif is_enemy_living:
            self.winner = 'enemy'
        else:
            self.winner = 'draw'
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
        self.prepared_units = [Unit_Warrior(random.randint(200, 600), random.randint(100, 300), UNIT_TEAM_PLAYER)
                               for i in range(basic_warrior_counter)] + \
                              [Unit_Enemy(random.randint(200, 600), random.randint(400, 600), UNIT_TEAM_ENEMY)]

    pass
