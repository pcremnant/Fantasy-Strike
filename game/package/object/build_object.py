from game.package.object.object import *
from game.package.struct.STRUCT import *

cBuildMap = STRUCT.SBuild_Coord()


class Obj_Build(Obj):
    global cBuildMap

    def __init__(self, x, y, sizeX, sizeY, imgPath, imgType):
        super().__init__(sizeX, sizeY, imgPath, imgType)
        self.posObject = STRUCT.SPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        self.imgObject.set_position(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        # 필요한 자원 리소스들 추가
        self.nResource = 0  # 임시 자원 변수

    def BuildObject(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        # self.posObject.SetPosition(posMouse.posX - (posMouse.posX % 16), posMouse.posY - (posMouse.posY % 16))
        # 16픽셀 단위로 이동 가능하게 설정

    def DrawObject(self):
        self.imgObject.draw_on_build_map(cBuildMap.GetTileWidth(), cBuildMap.GetTileHeight(), self.nSizeX, self.nSizeY)


class Obj_Build_Tree(Obj_Build):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, "tmpImage/tree_A.png", IMAGE_TYPE_SPRITE)
        self.SetObjectImage(1, 64, 64)


class Obj_Build_tmp(Obj_Build):
    def __init__(self, x, y):
        imgPath = "tmpImage/tmpb4.png"
        super().__init__(x, y, 2, 2, imgPath, IMAGE_TYPE_SPRITE)
        self.SetObjectImage(1, 256, 256)


class Obj_Build_Tent(Obj_Build):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2, "tmpImage/tmpTent1.png", IMAGE_TYPE_SPRITE)
        self.SetObjectImage(1, 256, 256)


class Obj_BuildPointer(Obj):
    global cBuildMap

    def __int__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(sizeX, sizeY, imgPath)

    def GetMousePosition(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))

# 마우스 포인터를 받아서 건물을 짓는다
