from game.package.object.object import *
from game.package.basic_module.basic_struct import *
import random
import math

# tmp code : unit define module will be added ----------------------------------------------
UNIT_FRAME_MOVE_UP = 0
UNIT_FRAME_MOVE_DOWN = 1
UNIT_FRAME_MOVE_RIGHT = 2
UNIT_FRAME_MOVE_LEFT = 3

UNIT_FRAME_SIZE = 4


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
        pass

    def draw(self):
        self.image_class[self.frame_mode].draw_image(self.position_on_window.x, self.position_on_window.y)

    def change_frame_mode(self):
        if abs(self.direction.x) >= abs(self.direction.y):
            if self.direction.x >= 0:
                self.frame_mode = UNIT_FRAME_MOVE_RIGHT
            else:
                self.frame_mode = UNIT_FRAME_MOVE_LEFT
        else:
            if self.direction.y >= 0:
                self.frame_mode = UNIT_FRAME_MOVE_UP
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
        direction_x = self.target_x - self.position_on_window.x
        direction_y = self.target_y - self.position_on_window.y
        direction_size = math.sqrt(
            (self.position_on_window.x - self.target_x) ** 2 + (self.position_on_window.y - self.target_y) ** 2)
        self.direction.x = direction_x / direction_size
        self.direction.y = direction_y / direction_size

    def update(self):
        self.change_frame_mode()
        self.set_normalized_direction()

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
    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, 1)
        self.frame_mode = UNIT_FRAME_MOVE_UP
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

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_UP, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 4, 64, 64)

        self.status = basic_struct.Status(100, 1, 3, 1, 1)
        pass


class Unit_Enemy(Unit):
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

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_UP, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 1, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 1, 64, 64)

        self.status = basic_struct.Status(100, 1, 3, 1, 1)
        pass
