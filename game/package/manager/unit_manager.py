from game.package.basic_module import unit_map
from ..object.unit_warrior import *
from ..object.unit_castle import *
from ..object.unit_frogman import *
from ..object.unit_goblin import *
from ..object.unit_militia import *

from game.package.object.unit import *
from game.package.framework import states


class UnitManager:
    def __init__(self):
        self.activated_units = []
        self.prepared_units = []
        self.unit_map = unit_map.Unit_Map()

        self.is_created_unit = False
        self.activated_units += [Unit_EnemyCastle(WINDOW_WIDTH // 2,
                                                  (get_unit_tile_position_y(WINDOW_HEIGHT) - 2) * UNIT_TILE_HEIGHT +
                                                  UNIT_MAP_START_Y,UNIT_TEAM_ENEMY)]
        self.activated_units += [
            Unit_PlayerCastle(WINDOW_WIDTH // 2, 2 * UNIT_TILE_HEIGHT + UNIT_MAP_START_Y,
                             UNIT_TEAM_PLAYER)]
        for unit in self.activated_units:
            unit.unit_map = self.unit_map.map
            unit.units = self.activated_units

        self.winner = None

    def draw(self):
        for unit in self.activated_units:
            unit.draw()
        self.unit_map.tmp_draw()

    def update(self):
        for unit in self.activated_units:
            self.unit_map.update_unit_map(self.activated_units)
            unit.update()

        for unit in self.activated_units:
            if not unit.is_living:
                self.activated_units.remove(unit)
                del unit

        for unit in self.activated_units:
            unit.units = self.activated_units
            unit.unit_map = self.unit_map.map

        if stopwatch.get_timer() % TIMER_UNIT_CREATION == 0:
            if not self.is_created_unit:
                self.prepare_unit()
                self.create_unit()
                self.is_created_unit = True
        else:
            self.is_created_unit = False

        # judge win or lose
        is_player_living = False
        is_enemy_living = False
        for unit in self.activated_units:
            if unit.is_castle:
                if unit.team == UNIT_TEAM_PLAYER:
                    is_player_living = True
                elif unit.team == UNIT_TEAM_ENEMY:
                    is_enemy_living = True

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
        for unit in self.activated_units:
            unit.units = self.activated_units
            unit.unit_map = self.unit_map.map

    def prepare_unit(self):
        build_manager = states.GameState.build_state.building_manager
        basic_warrior_counter = 0
        basic_tent_counter = 0
        for building in build_manager.buildings:
            if building.type == BUILDING_TYPE_BASIC_WARRIOR:
                basic_warrior_counter += 1
            elif building.type == BUILDING_TYPE_BASIC_TENT:
                basic_tent_counter += 1

        player_units = []
        count = 0
        x, y = 0, 0
        while count < basic_warrior_counter:
            if self.unit_map.map[y][x]:
                player_units += [Unit_Warrior(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                              UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                              UNIT_TEAM_PLAYER)]
                count += 1
            x += 1
            if x >= UNIT_MAP_SIZE_X:
                y += 1
                x = 0

        count = 0
        while count < basic_tent_counter:
            if self.unit_map.map[y][x]:
                player_units += [Unit_Militia(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                              UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                              UNIT_TEAM_PLAYER)]
                count += 1
            x += 1
            if x >= UNIT_MAP_SIZE_X:
                y += 1
                x = 0

        enemy_units = []
        count = 0
        x, y = 0, UNIT_MAP_SIZE_Y - 1
        while count < 1:
            if self.unit_map.map[y][x]:
                enemy_units += [Unit_Frogman(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                             UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                             UNIT_TEAM_ENEMY)]
                enemy_units += [Unit_Goblin(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                             UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                             UNIT_TEAM_ENEMY)]
                count += 1
            x += 1
            if x >= UNIT_MAP_SIZE_X:
                y -= 1
                x = 0

        self.prepared_units = player_units + enemy_units

    pass
