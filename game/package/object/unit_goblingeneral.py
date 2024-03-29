from .unit import *


class Unit_GoblinGeneral(Unit):
    MAX_HP = 100
    MOVE_SPEED = 0.4
    ATTACK_POWER = 9
    ATTACK_RANGE = 0.5
    ATTACK_SPEED = 1.3

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, -1)
        self.frame_mode = UNIT_FRAME_MOVE_DOWN
        self.team = team
        self.is_castle = False
        image_path_list = []
        image_type_list = []

        image_path_list.append([
            'resource/object/unit/goblingeneral/move_top_1.png',
            'resource/object/unit/goblingeneral/move_top_2.png',
            'resource/object/unit/goblingeneral/move_top_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/move_bottom_1.png',
            'resource/object/unit/goblingeneral/move_bottom_2.png',
            'resource/object/unit/goblingeneral/move_bottom_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/move_right_1.png',
            'resource/object/unit/goblingeneral/move_right_2.png',
            'resource/object/unit/goblingeneral/move_right_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/move_left_1.png',
            'resource/object/unit/goblingeneral/move_left_2.png',
            'resource/object/unit/goblingeneral/move_left_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/attack_top_1.png',
            'resource/object/unit/goblingeneral/attack_top_2.png',
            'resource/object/unit/goblingeneral/attack_top_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/attack_bottom_1.png',
            'resource/object/unit/goblingeneral/attack_bottom_2.png',
            'resource/object/unit/goblingeneral/attack_bottom_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/attack_right_1.png',
            'resource/object/unit/goblingeneral/attack_right_2.png',
            'resource/object/unit/goblingeneral/attack_right_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        image_path_list.append([
            'resource/object/unit/goblingeneral/attack_left_1.png',
            'resource/object/unit/goblingeneral/attack_left_2.png',
            'resource/object/unit/goblingeneral/attack_left_3.png',
        ])
        image_type_list.append(IMAGE_TYPE_FILES)

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_TOP, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 3, 64, 64)

        self.set_object_frame(UNIT_FRAME_ATTACK_TOP, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_ATTACK_BOTTOM, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_ATTACK_RIGHT, 3, 64, 64)
        self.set_object_frame(UNIT_FRAME_ATTACK_LEFT, 3, 64, 64)

        self.width = 32
        self.height = 32
        self.status = basic_struct.Status(Unit_GoblinGeneral.MAX_HP, Unit_GoblinGeneral.MOVE_SPEED, Unit_GoblinGeneral.ATTACK_POWER,
                                          Unit_GoblinGeneral.ATTACK_SPEED, Unit_GoblinGeneral.ATTACK_RANGE)

        self.attack_effect_index = EFFECT_INDEX_SWORD_SWING
