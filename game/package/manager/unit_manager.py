from game.package.basic_module import unit_map
from ..object.unit_warrior import *
from ..object.unit_castle import *
from ..object.unit_frogman import *
from ..object.unit_goblin import *
from ..object.unit_goblinwarrior import *
from ..object.unit_goblingeneral import *
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
                                                  UNIT_MAP_START_Y, UNIT_TEAM_ENEMY)]
        self.activated_units += [
            Unit_PlayerCastle(WINDOW_WIDTH // 2, 2 * UNIT_TILE_HEIGHT + UNIT_MAP_START_Y,
                              UNIT_TEAM_PLAYER)]
        for unit in self.activated_units:
            unit.unit_map = self.unit_map.map
            unit.units = self.activated_units

        self.enemy_barracks = EnemyBarracks()

        self.winner = None

    def draw(self):
        for unit in self.activated_units:
            unit.draw()

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
                if unit.team == UNIT_TEAM_PLAYER and unit.status.current_hp <= 0:
                    is_player_living = False
                elif unit.team == UNIT_TEAM_PLAYER:
                    is_player_living = True
                if unit.team == UNIT_TEAM_ENEMY and unit.status.current_hp <=0:
                    is_enemy_living = False
                elif unit.team == UNIT_TEAM_ENEMY:
                    is_enemy_living = True

        # ----------
        if is_player_living and is_enemy_living:
            self.winner = None
        elif is_player_living and not is_enemy_living:
            self.winner = 'player'
        elif is_enemy_living and not is_player_living:
            self.winner = 'enemy'
        else:
            self.winner = 'draw'
        pass

    def create_unit(self):
        self.activated_units += self.prepared_units
        for unit in self.activated_units:
            unit.units = self.activated_units
            unit.unit_map = self.unit_map.map
        self.enemy_barracks.next_round()

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

        # create enemy unit
        enemy_units = []
        enemy_index = self.enemy_barracks.get_enemy_unit_index()
        count = 0
        x, y = 0, UNIT_MAP_SIZE_Y - 1
        while count < len(enemy_index):
            if self.unit_map.map[y][x]:
                enemy_units.append(create_enemy_unit(enemy_index.pop(), x, y))
                count += 1
            x += 1
            if x >= UNIT_MAP_SIZE_X:
                y -= 1
                x = 0

        self.prepared_units = player_units + enemy_units

    pass


def create_enemy_unit(index, x, y):
    if index == DIFFICULTY_FROG:
        return Unit_Frogman(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                            UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                            UNIT_TEAM_ENEMY)
    elif index == DIFFICULTY_GOBLIN:
        return Unit_Goblin(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                           UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                           UNIT_TEAM_ENEMY)
    elif index == DIFFICULTY_WARRIOR:
        return Unit_GoblinWarrior(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                  UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                  UNIT_TEAM_ENEMY)
    elif index == DIFFICULTY_GENERAL:
        return Unit_GoblinGeneral(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2,
                                  UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2,
                                  UNIT_TEAM_ENEMY)


DIFFICULTY_FROG = 1
DIFFICULTY_GOBLIN = 2
DIFFICULTY_WARRIOR = 3
DIFFICULTY_GENERAL = 4


class EnemyBarracks:

    def __init__(self):
        self.current_resource = 1
        self.additional_resource = 4

        self.difficulty = DIFFICULTY_FROG
        self.current_round = 0

    def next_round(self):
        self.current_resource += self.additional_resource
        self.current_round += 1
        self.additional_resource = 4 + int(self.current_round * 1.5)
        if self.current_round > 3:
            self.difficulty = DIFFICULTY_GENERAL
        elif self.current_round > 2:
            self.difficulty = DIFFICULTY_WARRIOR
        elif self.current_round > 1:
            self.difficulty = DIFFICULTY_GOBLIN
        else:
            self.difficulty = DIFFICULTY_FROG

    def get_enemy_unit_index(self):
        enemy_index_list = []
        count = random.randint(self.current_round * 2, max(1, int(self.current_round * 3)))
        for i in range(count):
            enemy_type = random.randint(DIFFICULTY_FROG, self.difficulty)
            if self.current_resource >= enemy_type:
                self.current_resource -= enemy_type
                enemy_index_list.append(enemy_type)

        return enemy_index_list
