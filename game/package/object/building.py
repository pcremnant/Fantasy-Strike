from game.package.object.object import *
from game.package.basic_module.basic_struct import *


class Building(Object):
    def __init__(self, x, y, size_x, size_y, image_path, image_type):
        super().__init__(size_x, size_y)
        self.image_class = basic_struct.Image(image_path, image_type)
        self.position = Position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

        # 필요한 자원 리소스들 추가
        self.resource = None  # 임시 자원 변수

    def build_object_on_tile(self, x, y):
        self.set_object_position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

    def draw_object(self):
        self.image_class.draw_on_map(self.position.x, self.position.y,
                                     BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, self.size_x, self.size_y)


class Building_BasicWarrior(Building):
    def __init__(self, x, y):
        imgPath = "resource/object/build/basic_warrior.png"
        super().__init__(x, y, 2, 2, imgPath, IMAGE_TYPE_SPRITE)
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 256)


class Building_BasicTent(Building):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, "resource/object/build/basic_tent.png", IMAGE_TYPE_SPRITE)
        self.set_object_frame(FRAME_MODE_NONE, 1, 256, 256)


class Building_Pointer(Object):

    def __int__(self, x, y, size_x, size_y, image_path):
        super().__init__(size_x, size_y)

    def get_mouse_position(self, x, y):
        self.set_object_position(get_build_tile_position_x(x) * BUILD_TILE_WIDTH,
                                 get_build_tile_position_y(y) * BUILD_TILE_HEIGHT)

# 마우스 포인터를 받아서 건물을 짓는다
