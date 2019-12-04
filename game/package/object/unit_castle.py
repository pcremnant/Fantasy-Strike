from .unit import *


class Unit_PlayerCastle(Unit):
    MAX_HP = 500
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
        for frame_mode in range(UNIT_FRAME_SIZE):
            image_path_list.append([
                'resource/object/unit/player_castle/player_castle.png'
            ])
            image_type_list.append(IMAGE_TYPE_FILES)
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))
            self.set_object_frame(frame_mode, 1, 128, 196)

        self.width = 0
        self.height = 0
        self.status = basic_struct.Status(Unit_PlayerCastle.MAX_HP, Unit_PlayerCastle.MOVE_SPEED,
                                          Unit_PlayerCastle.ATTACK_POWER,
                                          Unit_PlayerCastle.ATTACK_SPEED, Unit_PlayerCastle.ATTACK_RANGE)

    def draw(self):
        self.image_class[0].image[0].clip_draw(0, 0, 128, 196, self.position_on_window.x + 16,
                                               self.position_on_window.y - 16, 256, 192)
        image = pico2d.load_image('resource/UI/hp_bar.png')
        image.clip_draw(0, 0, 64, 64, self.position_on_window.x + 16, self.position_on_window.y - 128,
                        self.status.current_hp / self.status.max_hp * 128, 10)


class Unit_EnemyCastle(Unit):
    MAX_HP = 500
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

        for frame_mode in range(UNIT_FRAME_SIZE):
            image_path_list.append([
                'resource/object/unit/enemy_castle/enemy_castle.png'
            ])
            image_type_list.append(IMAGE_TYPE_FILES)
            self.image_class.append(
                basic_struct.Image(image_path_list[frame_mode], image_type_list[frame_mode]))
            self.set_object_frame(frame_mode, 1, 256, 256)

        self.width = 0
        self.height = 0
        self.status = basic_struct.Status(Unit_EnemyCastle.MAX_HP, Unit_EnemyCastle.MOVE_SPEED,
                                          Unit_EnemyCastle.ATTACK_POWER,
                                          Unit_EnemyCastle.ATTACK_SPEED, Unit_EnemyCastle.ATTACK_RANGE)
        pass

    def draw(self):
        self.image_class[0].image[0].clip_draw(0, 0, 256, 256, self.position_on_window.x + 16,
                                               self.position_on_window.y + 92, 256, 192)
        image = pico2d.load_image('resource/UI/hp_bar.png')
        image.clip_draw(0, 0, 64, 64, self.position_on_window.x + 16, self.position_on_window.y - 16,
                        self.status.current_hp / self.status.max_hp * 128, 10)
