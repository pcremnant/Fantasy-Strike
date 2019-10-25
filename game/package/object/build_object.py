from game.package.object.OBJECT import *

cBuildMap = STRUCT.SBuild_Coord(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)


class Obj_Unit(Obj):
    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)

    def SetFrameMode(self, action):
        self.imgObject.SetFrameMode(action)
        self.imgObject.nCurFrame = 0


class Obj_Build(Obj):
    global cBuildMap

    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)
        # 필요한 자원 리소스들 추가
        self.nResource = 0  # 임시 자원 변수

    def BuildObject(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        # self.posObject.SetPosition(posMouse.posX - (posMouse.posX % 16), posMouse.posY - (posMouse.posY % 16))
        # 16픽셀 단위로 이동 가능하게 설정


class Obj_BuildPointer(Obj):
    global cBuildMap

    def __int__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)

    def GetMousePosition(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
# 마우스 포인터를 받아서 건물을 짓는다
