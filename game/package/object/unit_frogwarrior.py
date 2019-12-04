from .unit import *


class Unit_Enemy(Unit):
    MAX_HP = 30
    MOVE_SPEED = 0.3
    ATTACK_POWER = 5
    ATTACK_RANGE = 0.5
    ATTACK_SPEED = 1

    def __init__(self, x, y, team):
        super().__init__(x, y, 1, 1)
        self.direction = basic_struct.Position(0, -1)
        self.frame_mode = UNIT_FRAME_MOVE_DOWN
        self.team = team
        self.is_castle = False
        image_path_list = []
        image_type_list = []
        for frame_mode in range(UNIT_FRAME_SIZE):
            image_path_list.append([
                'resource/object/unit/tmp_enemy/enemy_for_test.png'
            ])
            image_type_list.append(IMAGE_TYPE_FILES)
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))
            self.set_object_frame(frame_mode, 1, 64, 64)

        self.width = 32
        self.height = 32
        self.status = basic_struct.Status(Unit_Enemy.MAX_HP, Unit_Enemy.MOVE_SPEED, Unit_Enemy.ATTACK_POWER,
                                          Unit_Enemy.ATTACK_SPEED, Unit_Enemy.ATTACK_RANGE)
