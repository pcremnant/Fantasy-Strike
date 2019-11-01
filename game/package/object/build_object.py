from game.package.object.object import *
from game.package.struct.STRUCT import *


class Object_Build(Object):
    def __init__(self, x, y, sizeX, sizeY, imgPath, imgType):
        super().__init__(sizeX, sizeY, imgPath, imgType)
        self.object_position = STRUCT.Position(get_build_tile_position_x(x), get_build_tile_position_y(y))
        self.class_object_image.set_position(self.object_position.x, self.object_position.y)
        # 필요한 자원 리소스들 추가
        self.resource = None  # 임시 자원 변수

    def build_object_on_tile(self, x, y):
        self.set_object_position(get_build_tile_position_x(x), get_build_tile_position_y(y))

    def draw_object(self):
        self.class_object_image.draw_on_build_map(BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, self.size_x, self.size_y)


class Object_Build_Tree(Object_Build):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, "tmpImage/tree_A.png", IMAGE_TYPE_SPRITE)
        self.set_object_frame(1, 64, 64)


class Object_Build_tmp(Object_Build):
    def __init__(self, x, y):
        imgPath = "tmpImage/tmpb4.png"
        super().__init__(x, y, 2, 2, imgPath, IMAGE_TYPE_SPRITE)
        self.set_object_frame(1, 256, 256)


class Object_Build_Tent(Object_Build):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, "tmpImage/tmpTent1.png", IMAGE_TYPE_SPRITE)
        self.set_object_frame(1, 256, 256)


class Object_Build_Pointer(Object):

    def __int__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(sizeX, sizeY, imgPath)

    def GetMousePosition(self, x, y):
        self.set_object_position(get_build_tile_position_x(x), get_build_tile_position_y(y))

# 마우스 포인터를 받아서 건물을 짓는다
