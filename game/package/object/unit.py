from game.package.object.object import *
from game.package.basic_module.basic_struct import *
import pico2d
import random
import math

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
        self.is_in_attack_range = False
        self.is_able_to_attack = True
        self.is_attacking = False
        self.is_living = True
        self.attack_delay_counter = 0
        pass

    def draw(self):
        self.image_class[self.frame_mode].draw_image(self.position_on_window.x, self.position_on_window.y)
        image = pico2d.load_image('resource/UI/hp_bar.png')
        image.clip_draw(0, 0, 64, 64, self.position_on_window.x, self.position_on_window.y + 32,
                        self.status.current_hp / self.status.max_hp * 32, 10)

    def change_frame_mode(self):
        distance = None
        if self.target_x is None or self.target_y is None:
            distance = -1
        else:
            distance = math.sqrt((get_unit_tile_position_y(self.target_y) - self.position_on_tile.y) ** 2 + \
                       (get_unit_tile_position_x(self.target_x) - self.position_on_tile.x) ** 2)
        if 0 < distance <= self.status.attack_range:
            self.is_in_attack_range = True
            self.frame_mode = UNIT_FRAME_ATTACK_TOP
        elif abs(self.direction.x) >= abs(self.direction.y):
            if self.direction.x >= 0:
                self.frame_mode = UNIT_FRAME_MOVE_RIGHT
            else:
                self.frame_mode = UNIT_FRAME_MOVE_LEFT
        else:
            if self.direction.y >= 0:
                self.frame_mode = UNIT_FRAME_MOVE_TOP
            else:
                self.frame_mode = UNIT_FRAME_MOVE_DOWN

    def set_target(self, units):
        enemy_units = []
        is_empty = True
        for unit in units:
            if self.team != unit.team:
                enemy_units += [unit]
                is_empty = False

        min_distance_index = 0
        if is_empty:
            self.target_x = None
            self.target_y = None
            pass
        else:
            min_distance = 0
            index_counter = 0
            for enemy in enemy_units:
                distance = (self.position_on_window.x - enemy.position_on_window.x) ** 2 + (
                        self.position_on_window.y - enemy.position_on_window.y) ** 2
                if index_counter == 0:
                    min_distance = distance
                    min_distance_index = index_counter
                else:
                    if min_distance > distance:
                        min_distance_index = index_counter
                index_counter += 1
            self.target_x = enemy_units[min_distance_index].position_on_window.x
            self.target_y = enemy_units[min_distance_index].position_on_window.y

    def set_normalized_direction(self):
        degree = None
        if self.target_x is None or self.target_y is None:
            degree = -1
        else:
            degree = math.atan2(self.target_y - self.position_on_window.y, self.target_x - self.position_on_window.x)

        if degree == -1:
            self.direction.x = 0
            self.direction.y = 0
        else:
            self.direction.x = math.cos(degree) * self.status.move_speed
            self.direction.y = math.sin(degree) * self.status.move_speed

    def attack_target_position_on_tile(self):
        return get_unit_tile_position_x(self.target_x), get_unit_tile_position_y(self.target_y)

    def attack(self, units):
        for unit in units:
            if not unit.team == self.team:
                if unit.position_on_tile.x == get_unit_tile_position_x(
                        self.target_x) and unit.position_on_tile.y == get_unit_tile_position_y(self.target_y):
                    unit.status.current_hp -= self.status.attack_power
                    if unit.status.current_hp <= 0:
                        unit.is_alive = False
        self.is_in_attack_range = False
        self.is_able_to_attack = False
        self.is_attacking = False

    def update(self, is_movable):
        self.change_frame_mode()
        self.set_normalized_direction()

        if self.is_in_attack_range:
            if not self.is_able_to_attack:
                self.image_class[self.frame_mode].current_frame = self.image_class[
                                                                      self.frame_mode].max_frame * SUB_FRAME - 1
                self.attack_delay_counter += 1
                if 100 / self.status.attack_speed <= self.attack_delay_counter:
                    self.attack_delay_counter = 0
                    self.is_able_to_attack = True
            else:
                if self.image_class[self.frame_mode].current_frame == self.image_class[
                    self.frame_mode].max_frame * SUB_FRAME - 1:
                    self.is_able_to_attack = False
                    self.is_attacking = True
                else:
                    self.is_attacking = False

        elif is_movable:
            self.position_on_window.move_position(self.direction.x, self.direction.y)

        self.position_on_tile.set_position(get_unit_tile_position_x(self.position_on_window.x),
                                           get_unit_tile_position_y(self.position_on_window.y))

        if self.position_on_window.x > UNIT_MAP_END_X:
            self.position_on_window.x -= self.direction.x * 2
        if self.position_on_window.x < UNIT_MAP_START_X:
            self.position_on_window.x -= self.direction.x * 2
        if self.position_on_window.y > UNIT_MAP_END_Y:
            self.position_on_window.y -= self.direction.y * 2
        if self.position_on_window.y < UNIT_MAP_START_Y:
            self.position_on_window.y -= self.direction.y * 2


# tmp unit (for test)
class Unit_Warrior(Unit):
    MAX_HP = 100
    MOVE_SPEED = 0.5
    ATTACK_POWER = 10
    ATTACK_RANGE = math.sqrt(1 + 1)
    ATTACK_SPEED = 1

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, 1)
        self.frame_mode = UNIT_FRAME_MOVE_TOP
        self.team = team
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

        self.status = basic_struct.Status(Unit_EnemyCastle.MAX_HP, Unit_EnemyCastle.MOVE_SPEED, Unit_EnemyCastle.ATTACK_POWER,
                                          Unit_EnemyCastle.ATTACK_SPEED, Unit_EnemyCastle.ATTACK_RANGE)
        pass
