from game.package.object.object import *
from game.package.basic_module.basic_struct import *
import pico2d
import random
import math
from game.package.basic_module.behavior_tree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

# tmp code : unit define module will be added ----------------------------------------------
UNIT_FRAME_MOVE_TOP = 0
UNIT_FRAME_MOVE_DOWN = 1
UNIT_FRAME_MOVE_RIGHT = 2
UNIT_FRAME_MOVE_LEFT = 3
UNIT_FRAME_ATTACK_TOP = 4

UNIT_FRAME_SIZE = 5


# ------------------------------------------------------------------------------------------

class Unit(Object):
    def __init__(self, x, y, size_x, size_y):
        super().__init__(size_x, size_y)
        self.image_class = []  # image list [frame_mode]
        self.frame_mode = None
        self.position_on_window = basic_struct.Position(x, y)
        self.position_on_tile = basic_struct.Position(get_unit_tile_position_x(x), get_unit_tile_position_y(y))
        self.status = None
        self.direction = None
        self.team = None
        self.target_x = None
        self.target_y = None
        # self.is_in_attack_range = False
        # self.is_able_to_attack = True
        # self.is_attacking = False
        self.is_living = True
        self.is_castle = None
        self.attack_delay_counter = 0

        # tmp code : for behavior tree
        self.units = None
        self.unit_map = None
        self.next_tile = None

        self.build_behavior_tree()
        pass

    def draw(self):
        self.image_class[self.frame_mode].draw_image(self.position_on_window.x, self.position_on_window.y)
        image = pico2d.load_image('resource/UI/hp_bar.png')
        image.clip_draw(0, 0, 64, 64, self.position_on_window.x, self.position_on_window.y + 32,
                        self.status.current_hp / self.status.max_hp * 32, 10)

    # def change_frame_mode(self):
    #     distance = None
    #     if self.target_x is None or self.target_y is None:
    #         distance = -1
    #     else:
    #         distance = math.sqrt((get_unit_tile_position_y(self.target_y) - self.position_on_tile.y) ** 2 + \
    #                              (get_unit_tile_position_x(self.target_x) - self.position_on_tile.x) ** 2)
    #     if 0 < distance <= self.status.attack_range:
    #         self.is_in_attack_range = True
    #         self.frame_mode = UNIT_FRAME_ATTACK_TOP
    #     elif abs(self.direction.x) >= abs(self.direction.y):
    #         if self.direction.x >= 0:
    #             self.frame_mode = UNIT_FRAME_MOVE_RIGHT
    #         else:
    #             self.frame_mode = UNIT_FRAME_MOVE_LEFT
    #     else:
    #         if self.direction.y >= 0:
    #             self.frame_mode = UNIT_FRAME_MOVE_TOP
    #         else:
    #             self.frame_mode = UNIT_FRAME_MOVE_DOWN

    # def set_target(self, units):
    #    enemy_units = []
    #    is_empty = True
    #    for unit in units:
    #        if self.team != unit.team:
    #            enemy_units += [unit]
    #            is_empty = False

    #    min_distance_index = 0
    #    if is_empty:
    #        self.target_x = None
    #        self.target_y = None
    #        pass
    #    else:
    #        min_distance = 0
    #        index_counter = 0
    #        for enemy in enemy_units:
    #            distance = (self.position_on_window.x - enemy.position_on_window.x) ** 2 + (
    #                    self.position_on_window.y - enemy.position_on_window.y) ** 2
    #            if index_counter == 0:
    #                min_distance = distance
    #                min_distance_index = index_counter
    #            else:
    #                if min_distance > distance:
    #                    min_distance_index = index_counter
    #                    min_distance = distance
    #            index_counter += 1
    #        self.target_x = enemy_units[min_distance_index].position_on_window.x
    #        self.target_y = enemy_units[min_distance_index].position_on_window.y

    # def set_normalized_direction(self):
    #     degree = None
    #     if self.target_x is None or self.target_y is None:
    #         degree = -1
    #     else:
    #         degree = math.atan2(self.target_y - self.position_on_window.y, self.target_x - self.position_on_window.x)
    #
    #     if degree == -1:
    #         self.direction.x = 0
    #         self.direction.y = 0
    #     else:
    #         self.direction.x = math.cos(degree) * self.status.move_speed
    #         self.direction.y = math.sin(degree) * self.status.move_speed

    # def attack_target_position_on_tile(self):
    #     return get_unit_tile_position_x(self.target_x), get_unit_tile_position_y(self.target_y)
    #
    # def attack(self, units):
    #     for unit in units:
    #         if not unit.team == self.team:
    #             if unit.position_on_tile.x == get_unit_tile_position_x(
    #                     self.target_x) and unit.position_on_tile.y == get_unit_tile_position_y(self.target_y):
    #                 unit.status.current_hp -= self.status.attack_power
    #                 if unit.status.current_hp < 1:
    #                     unit.is_living = False
    #     self.is_in_attack_range = False
    #     self.is_able_to_attack = False
    #     self.is_attacking = False

    # def update(self, unit_map):
    #     self.bt.run()
    # self.change_frame_mode()
    # self.set_normalized_direction()
    #
    # if self.is_in_attack_range:
    #     if not self.is_able_to_attack:
    #         self.image_class[self.frame_mode].current_frame = self.image_class[
    #                                                               self.frame_mode].max_frame * SUB_FRAME - 1
    #         self.attack_delay_counter += 1
    #         if 100 / self.status.attack_speed <= self.attack_delay_counter:
    #             self.attack_delay_counter = 0
    #             self.is_able_to_attack = True
    #     else:
    #         if self.image_class[self.frame_mode].current_frame == \
    #                 self.image_class[self.frame_mode].max_frame * SUB_FRAME - 1:
    #             self.is_able_to_attack = False
    #             self.is_attacking = True
    #         else:
    #             self.is_attacking = False
    # else:
    #     moved_position = basic_struct.Position(self.position_on_window.x, self.position_on_window.y)
    #     moved_position.move_position(self.direction.x, self.direction.y)
    #     if get_unit_tile_position_x(moved_position.x) == self.position_on_tile.x and \
    #             get_unit_tile_position_y(moved_position.y) == self.position_on_tile.y:
    #         self.position_on_window.move_position(self.direction.x, self.direction.y)
    #     elif unit_map[get_unit_tile_position_y(moved_position.y)][get_unit_tile_position_x(moved_position.x)]:
    #         self.position_on_window.move_position(self.direction.x, self.direction.y)
    #     else:
    #         if abs(self.direction.x) <= abs(self.direction.y):
    #             if self.target_x < self.position_on_window.x:
    #                 if unit_map[self.position_on_tile.y][max(0, self.position_on_tile.x - 1)]:
    #                     self.position_on_window.move_position(-1 * self.status.move_speed, 0)
    #                 else:
    #                     self.position_on_window.move_position(1 * self.status.move_speed, 0)
    #             else:
    #                 if unit_map[self.position_on_tile.y][min(UNIT_MAP_SIZE_X - 1, self.position_on_tile.x + 1)]:
    #                     self.position_on_window.move_position(1 * self.status.move_speed, 0)
    #                 else:
    #                     self.position_on_window.move_position(-1 * self.status.move_speed, 0)
    #         elif abs(self.direction.x) > abs(self.direction.y):
    #             if self.target_y < self.position_on_window.y:
    #                 if unit_map[max(0, self.position_on_tile.y - 1)][self.position_on_tile.x]:
    #                     self.position_on_window.move_position(0, -1 * self.status.move_speed)
    #                 else:
    #                     self.position_on_window.move_position(0, 1 * self.status.move_speed)
    #             else:
    #                 if unit_map[min(UNIT_MAP_SIZE_Y - 1, self.position_on_tile.y + 1)][self.position_on_tile.x]:
    #                     self.position_on_window.move_position(0, 1 * self.status.move_speed)
    #                 else:
    #                     self.position_on_window.move_position(0, -1 * self.status.move_speed)
    #
    # self.position_on_tile.set_position(get_unit_tile_position_x(self.position_on_window.x),
    #                                    get_unit_tile_position_y(self.position_on_window.y))
    #
    # if self.position_on_window.x > UNIT_MAP_END_X:
    #     self.position_on_window.x = UNIT_MAP_END_X - 1  # self.direction.x * 2
    # if self.position_on_window.x < UNIT_MAP_START_X:
    #     self.position_on_window.x = UNIT_MAP_START_X + 1  # self.direction.x * 2
    # if self.position_on_window.y > UNIT_MAP_END_Y:
    #     self.position_on_window.y = UNIT_MAP_END_Y - 1  # self.direction.y * 2
    # if self.position_on_window.y < UNIT_MAP_START_Y:
    #     self.position_on_window.y = UNIT_MAP_START_Y + 1  # self.direction.y * 2

    def update(self):
        self.bt.run()

    def solve_maze(self, maze, start, end):
        queue = []
        done = set()

        queue.append(start)
        done.add(start)

        while queue:
            p = queue.pop()
            v = (p[-2], p[-1])
            # v = (p[-1][0], p[-1][1])
            if v == end:
                return p
            else:
                for x in maze[v]:
                    if x not in done:
                        queue.append(p + x)
                        done.add(x)

        return '?'

    def is_in_attack_range(self):
        for unit in self.units:
            if unit.team != self.team:
                distance = (unit.position_on_tile.x - self.position_on_tile.x) ** 2 + (
                        unit.position_on_tile.y - self.position_on_tile.y) ** 2
                if self.status.attack_range ** 2 >= distance:
                    return BehaviorTree.SUCCESS
        #
        return BehaviorTree.FAIL

    def is_in_attack_delay(self):
        if self.is_castle:
            return BehaviorTree.FAIL
        elif self.attack_delay_counter < 100 / self.status.attack_speed:
            self.attack_delay_counter += 1
            return BehaviorTree.RUNNING
        elif self.attack_delay_counter >= 100 / self.status.attack_speed:
            self.attack_delay_counter = 0
            return BehaviorTree.SUCCESS

    def attack_enemy(self):
        min_distance = None
        min_index = None
        min_count = 0
        for unit in self.units:
            if unit.team != self.team:
                distance = (unit.position_on_tile.x - self.position_on_tile.x) ** 2 + (
                        unit.position_on_tile.y - self.position_on_tile.y) ** 2
                if min_distance > distance:
                    min_distance = distance
                    min_index = min_count
            min_count += 1

        if min_distance is None or min_index is None:
            return BehaviorTree.FAIL
        else:
            self.units[min_index].status.current_hp -= self.status.attack_power
            return BehaviorTree.SUCCESS

    def set_target_enemy(self):
        # 임시로 상수값 넣어보기
        TEMP_RANGE = 5
        min_distance = None
        min_index = None
        min_count = 0
        for unit in self.units:
            if unit.team != self.team:
                distance = (unit.position_on_tile.x - self.position_on_tile.x) ** 2 + (
                        unit.position_on_tile.y - self.position_on_tile.y) ** 2
                if min_distance is None:
                    min_distance = distance
                elif min_distance > distance:
                    min_distance = distance
                    min_index = min_count
            min_count += 1

        if min_distance is None or min_index is None:
            return BehaviorTree.FAIL
        elif min_distance < TEMP_RANGE ** 2:
            # set target!
            self.target_x = self.units[min_index].position_on_tile.x
            self.target_y = self.units[min_index].position_on_tile.y
            return BehaviorTree.SUCCESS

        return BehaviorTree.FAIL

    def set_target_castle(self):
        for unit in self.units:
            if unit.is_castle and unit.team != self.team:
                self.target_x = unit.position_on_tile.x
                self.target_y = unit.position_on_tile.y
                return BehaviorTree.SUCCESS

        return BehaviorTree.FAIL

    def find_path(self):
        # set maze
        #self.unit_map[self.position_on_tile.y][self.position_on_tile.x] = True
        self.unit_map[self.target_y][self.target_x] = True
        maze = {}
        for y in range(UNIT_MAP_SIZE_Y):
            for x in range(UNIT_MAP_SIZE_X):
                path = []
                # 상하좌우 체크
                # 상
                if y + 1 < UNIT_MAP_SIZE_Y and self.unit_map[y + 1][x]:
                    path += [(y + 1, x)]
                # 하
                if y - 1 >= 0 and self.unit_map[y - 1][x]:
                    path += [(y - 1, x)]
                # 좌
                if x - 1 >= 0 and self.unit_map[y][x - 1]:
                    path += [(y, x - 1)]
                # 우
                if x + 1 < UNIT_MAP_SIZE_X and self.unit_map[y][x + 1]:
                    path += [(y, x + 1)]

                maze[(y, x)] = path

        self.unit_map[self.target_y][self.target_x] = False
        # self.unit_map[self.position_on_tile.y][self.position_on_tile.x] = False
        # solve maze
        path = self.solve_maze(maze, (self.position_on_tile.y, self.position_on_tile.x), (self.target_y, self.target_x))

        # set next tile
        if path == '?':
            next_tile = None
            return BehaviorTree.FAIL
        else:
            self.next_tile = basic_struct.Position(path[2], path[3])
            return BehaviorTree.SUCCESS

    def move(self):
        if self.next_tile is None:
            return BehaviorTree.FAIL
        else:
            # set direction
            degree = math.atan2(UNIT_MAP_START_Y + self.next_tile.y * UNIT_TILE_HEIGHT + UNIT_TILE_HEIGHT // 2 - self.position_on_window.y,
                                UNIT_MAP_START_X + self.next_tile.x * UNIT_TILE_WIDTH + UNIT_TILE_WIDTH // 2 - self.position_on_window.x)
            self.direction.x = math.cos(degree) * self.status.move_speed
            self.direction.y = math.sin(degree) * self.status.move_speed

            # set animation frame
            if abs(self.direction.x) >= abs(self.direction.y):
                if self.direction.x >= 0:
                    self.frame_mode = UNIT_FRAME_MOVE_RIGHT
                else:
                    self.frame_mode = UNIT_FRAME_MOVE_LEFT
            else:
                if self.direction.y >= 0:
                    self.frame_mode = UNIT_FRAME_MOVE_TOP
                else:
                    self.frame_mode = UNIT_FRAME_MOVE_DOWN

            # move position
            self.position_on_window.move_position(self.direction.x, self.direction.y)
            self.position_on_tile.set_position(get_unit_tile_position_x(self.position_on_window.x),
                                               get_unit_tile_position_y(self.position_on_window.y))
            return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        is_in_attack_range_node = LeafNode("Is in attack range", self.is_in_attack_range)
        is_in_attack_delay_node = LeafNode("Is in attack delay", self.is_in_attack_delay)
        attack_enemy_node = LeafNode("Attack enemy", self.attack_enemy)

        attack_action_node = SequenceNode("Attack action")
        attack_action_node.add_children(is_in_attack_range_node, is_in_attack_delay_node, attack_enemy_node)

        set_target_enemy_node = LeafNode("Set target enemy", self.set_target_enemy)
        set_target_castle_node = LeafNode("Set target castle", self.set_target_castle)

        set_target_node = SelectorNode("Set target")
        set_target_node.add_children(set_target_enemy_node, set_target_castle_node)

        find_path_node = LeafNode("Find path", self.find_path)
        move_node = LeafNode("Move", self.move)

        move_action_node = SequenceNode("Move Action")
        move_action_node.add_children(set_target_node, find_path_node, move_node)

        action_node = SelectorNode("Action")
        action_node.add_children(attack_action_node, move_action_node)

        self.bt = BehaviorTree(action_node)
        pass


# tmp unit (for test)
class Unit_Warrior(Unit):
    MAX_HP = 100
    MOVE_SPEED = 0.5
    ATTACK_POWER = 10
    ATTACK_RANGE = 1.7
    ATTACK_SPEED = 1

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, 1)
        self.frame_mode = UNIT_FRAME_MOVE_TOP
        self.team = team
        self.is_castle = False
        image_path_list = []
        image_type_list = []

        image_path_list.append([
            'resource/object/unit/warrior/move_top_1.png',
            'resource/object/unit/warrior/move_top_2.png',
            'resource/object/unit/warrior/move_top_3.png',
            'resource/object/unit/warrior/move_top_4.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/move_bottom_1.png',
            'resource/object/unit/warrior/move_bottom_2.png',
            'resource/object/unit/warrior/move_bottom_3.png',
            'resource/object/unit/warrior/move_bottom_4.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/move_right_1.png',
            'resource/object/unit/warrior/move_right_2.png',
            'resource/object/unit/warrior/move_right_3.png',
            'resource/object/unit/warrior/move_right_4.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/move_left_1.png',
            'resource/object/unit/warrior/move_left_2.png',
            'resource/object/unit/warrior/move_left_3.png',
            'resource/object/unit/warrior/move_left_4.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/attack_top_1.png',
            'resource/object/unit/warrior/attack_top_2.png',
            'resource/object/unit/warrior/attack_top_3.png',
            'resource/object/unit/warrior/attack_top_4.png',
            'resource/object/unit/warrior/attack_top_5.png',
            'resource/object/unit/warrior/attack_top_6.png',
            'resource/object/unit/warrior/attack_top_7.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_TOP, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_ATTACK_TOP, 7, 86, 86)

        self.status = basic_struct.Status(Unit_Warrior.MAX_HP, Unit_Warrior.MOVE_SPEED, Unit_Warrior.ATTACK_POWER,
                                          Unit_Warrior.ATTACK_SPEED, Unit_Warrior.ATTACK_RANGE)
        pass


class Unit_Enemy(Unit):
    MAX_HP = 20
    MOVE_SPEED = 0.3
    ATTACK_POWER = 0
    ATTACK_RANGE = 1
    ATTACK_SPEED = 20

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, -1)
        self.frame_mode = UNIT_FRAME_MOVE_DOWN
        self.team = team
        self.is_castle = False
        image_path_list = []
        image_type_list = []

        image_path_list.append([
            'resource/object/unit/tmp_enemy/enemy_for_test.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy/enemy_for_test.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy/enemy_for_test.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy/enemy_for_test.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy/enemy_for_test.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_TOP, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_ATTACK_TOP, 1, 64, 64)

        self.status = basic_struct.Status(Unit_Enemy.MAX_HP, Unit_Enemy.MOVE_SPEED, Unit_Enemy.ATTACK_POWER,
                                          Unit_Enemy.ATTACK_SPEED, Unit_Enemy.ATTACK_RANGE)
        pass


class Unit_EnemyCastle(Unit):
    MAX_HP = 200
    MOVE_SPEED = 0
    ATTACK_POWER = 0
    ATTACK_RANGE = 0
    ATTACK_SPEED = 0

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, -1)
        self.frame_mode = UNIT_FRAME_MOVE_DOWN
        self.team = team
        self.is_castle = True
        image_path_list = []
        image_type_list = []

        image_path_list.append([
            'resource/object/unit/tmp_enemy_castle/tmp_enemy_castle.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy_castle/tmp_enemy_castle.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy_castle/tmp_enemy_castle.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy_castle/tmp_enemy_castle.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/tmp_enemy_castle/tmp_enemy_castle.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_TOP, 1, 256, 256)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 1, 256, 256)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 1, 256, 256)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 1, 256, 256)
        self.set_object_frame(UNIT_FRAME_ATTACK_TOP, 1, 256, 256)

        self.status = basic_struct.Status(Unit_EnemyCastle.MAX_HP, Unit_EnemyCastle.MOVE_SPEED,
                                          Unit_EnemyCastle.ATTACK_POWER,
                                          Unit_EnemyCastle.ATTACK_SPEED, Unit_EnemyCastle.ATTACK_RANGE)
        pass
