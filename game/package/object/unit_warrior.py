from .unit import *


class Unit_Warrior(Unit):
    MAX_HP = 100
    MOVE_SPEED = 0.5
    ATTACK_POWER = 10
    ATTACK_RANGE = 0.7
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

        image_path_list.append([
            'resource/object/unit/warrior/attack_bottom_1.png',
            'resource/object/unit/warrior/attack_bottom_2.png',
            'resource/object/unit/warrior/attack_bottom_3.png',
            'resource/object/unit/warrior/attack_bottom_4.png',
            'resource/object/unit/warrior/attack_bottom_5.png',
            'resource/object/unit/warrior/attack_bottom_6.png',
            'resource/object/unit/warrior/attack_bottom_7.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/attack_right_1.png',
            'resource/object/unit/warrior/attack_right_2.png',
            'resource/object/unit/warrior/attack_right_3.png',
            'resource/object/unit/warrior/attack_right_4.png',
            'resource/object/unit/warrior/attack_right_5.png',
            'resource/object/unit/warrior/attack_right_6.png',
            'resource/object/unit/warrior/attack_right_7.png'
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/warrior/attack_left_1.png',
            'resource/object/unit/warrior/attack_left_2.png',
            'resource/object/unit/warrior/attack_left_3.png',
            'resource/object/unit/warrior/attack_left_4.png',
            'resource/object/unit/warrior/attack_left_5.png',
            'resource/object/unit/warrior/attack_left_6.png',
            'resource/object/unit/warrior/attack_left_7.png'
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
        self.set_object_frame(UNIT_FRAME_ATTACK_BOTTOM, 7, 86, 86)
        self.set_object_frame(UNIT_FRAME_ATTACK_RIGHT, 7, 86, 86)
        self.set_object_frame(UNIT_FRAME_ATTACK_LEFT, 7, 86, 86)

        self.status = basic_struct.Status(Unit_Warrior.MAX_HP, Unit_Warrior.MOVE_SPEED, Unit_Warrior.ATTACK_POWER,
                                          Unit_Warrior.ATTACK_SPEED, Unit_Warrior.ATTACK_RANGE)

        self.width = 64
        self.height = 64
