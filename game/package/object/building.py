from game.package.object.object import *
from game.package.basic_module.basic_struct import *
from game.package.basic_module.basic_define import *


class Building(Object):
    def __init__(self, x, y, size_x, size_y, image_path, image_type, on_table=False):
        super().__init__(size_x, size_y)
        self.image_class = basic_struct.Image(image_path, image_type)
        self.position = Position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

        # 필요한 자원 리소스들 추가
        self.require_resource = None  # 임시 자원 변수
        self.is_on_table = on_table

    def build_object_on_tile(self, x, y):
        self.set_object_position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

    def draw(self):
        self.image_class.draw_on_map(self.position.x, self.position.y,
                                     BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, self.size_x, self.size_y)
        if self.is_on_table:
            basic_struct.ui.write(11, self.position.x - BUILD_TILE_WIDTH / 2 - 5,
                                  self.position.y - BUILD_TILE_HEIGHT - 5,
                                  '(%(wood)d / %(stone)d)', {'wood': self.require_resource.wood,
                                                             'stone': self.require_resource.stone}, (0, 0, 0))


class Building_WarriorStone(Building):
    def __init__(self, x, y, on_table=False):
        imgPath = "resource/object/build/basic_warrior.png"
        super().__init__(x, y, 2, 2, imgPath, IMAGE_TYPE_SPRITE, on_table)
        self.type = BUILDING_TYPE_BASIC_WARRIOR
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 256)
        self.require_resource = basic_struct.Resource(6, 10)


class Building_Tent(Building):
    def __init__(self, x, y, on_table=False):
        super().__init__(x, y, 2, 2, "resource/object/build/basic_tent.png", IMAGE_TYPE_SPRITE, on_table)
        self.type = BUILDING_TYPE_BASIC_TENT
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 256)
        self.require_resource = basic_struct.Resource(5, 0)


class Building_Timber(Building):
    def __init__(self, x, y, on_table=False):
        super().__init__(x, y, 2, 2, "resource/object/build/timber.png", IMAGE_TYPE_SPRITE, on_table)
        self.type = BUILDING_TYPE_TIMBER
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 196)
        self.require_resource = basic_struct.Resource(5, 3)


class Building_Quarry(Building):
    def __init__(self, x, y, on_table=False):
        super().__init__(x, y, 2, 2, "resource/object/build/quarry.png", IMAGE_TYPE_SPRITE, on_table)
        self.type = BUILDING_TYPE_QUARRY
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 196)
        self.require_resource = basic_struct.Resource(3, 5)


class Building_Pointer(Object):

    def __int__(self, x, y, size_x, size_y, image_path):
        super().__init__(size_x, size_y)

    def get_mouse_position(self, x, y):
        self.set_object_position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

# 마우스 포인터를 받아서 건물을 짓는다
